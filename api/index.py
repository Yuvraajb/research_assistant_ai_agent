from flask import Flask, request, jsonify
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List, Optional
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
import re
import json
# Adjust the import path since tools.py is now in the parent directory
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools import search_tool, wiki_tool

load_dotenv()

# Vercel requires the Flask app instance to be named 'app'
app = Flask(__name__)

class ResearchResponse(BaseModel):
    topic: str = Field(..., description="The topic of the research")
    summary: Optional[str] = Field(None, description="A concise summary of the research")
    sources: Optional[List[str]] = Field(None, description="List of sources used")
    tools_used: List[str] = Field(..., description="List of tools used during research")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a research assistant that helps generate a research paper. "
            "Answer the user's query using necessary tools and provide a descriptive research first draft paper, a detailed and comprehensive summary which is labelled as summary on top, relevant sources, and tools used in the final JSON output. "
            "Output must be raw JSON only, with no markdown or code blocks.\n\n{format_instructions}"
        ),
        ("ai", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}")
    ]
).partial(format_instructions=parser.get_format_instructions())
tools = [search_tool, wiki_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False, handle_parsing_errors=True)

# Define a route for your research endpoint
@app.route('/api/research', methods=['POST'])
def research():
    data = request.get_json()
    query = data.get('query')

    if not query:
        return jsonify({"error": "Query is required"}), 400

    try:
        raw_response = agent_executor.invoke({
            "query": query,
            "chat_history": []
        })

        raw_output = raw_response.get("output", "")
        # Handle potential non-string output gracefully
        if not isinstance(raw_output, str):
            return jsonify({"error": "Received non-string output from agent"}), 500

        clean_output = re.sub(r"```(?:json)?\n(.*?)\n```", r"\1", raw_output, flags=re.DOTALL).strip()

        # Add robustness: Check if clean_output is valid JSON before parsing
        if not clean_output.startswith("{") or not clean_output.endswith("}"):
             return jsonify({"error": f"Failed to extract JSON from agent output: {clean_output}"}), 500

        try:
            # Attempt to load as JSON first
            output_data = json.loads(clean_output)
            pretty_response = ResearchResponse(**output_data)
        except json.JSONDecodeError as json_e:
            return jsonify({"error": f"Failed to parse JSON from agent output: {json_e} - Output: {clean_output}"}), 500
        except Exception as parse_e:
            return jsonify({"error": f"Failed to validate agent output with Pydantic: {parse_e} - Output: {clean_output}"}), 500

        return jsonify(pretty_response.dict())

    except Exception as e:
        print(f"Error during agent execution or parsing: {e}") # Log for debugging
        return jsonify({"error": f"An internal error occurred: {e}"}), 500

# Optional: A root route to confirm the API is running
@app.route('/api', methods=['GET'])
def home():
    return jsonify({"message": "Research Assistant API is running!"})

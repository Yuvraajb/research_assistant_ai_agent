from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
import re
from tools import search_tool,wiki_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str = Field(..., description="The topic of the research")
    summary: str = Field(..., description="A concise summary of the research")
    sources: List[str] = Field(..., description="List of sources used")
    tools_used: List[str] = Field(..., description="List of tools used during research")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a research assistant that helps generate a research paper. "
            "Answer the user's query using necessary tools. "
            "Output must be raw JSON only, with no markdown or code blocks.\n\n{format_instructions}"
        ),
        ("ai", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}")
    ]
).partial(format_instructions=parser.get_format_instructions())
tools = [search_tool,wiki_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False,handle_parsing_errors=True)
query = input("how can i help you today: ")
raw_response = agent_executor.invoke({
    "query": query,
    "chat_history": []
})

raw_output = raw_response.get("output", "")
clean_output = re.sub(r"```(?:json)?\n(.*?)\n```", r"\1", raw_output, flags=re.DOTALL).strip()

pretty_response = parser.parse(clean_output)
print(pretty_response)

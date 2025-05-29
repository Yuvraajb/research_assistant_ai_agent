import React, { useState } from 'react';
import ResearchForm from './ResearchForm'; // Assuming ResearchForm is in the same folder
import './styles.css'; // Import the new CSS file

function App() {
  const [researchData, setResearchData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleResearch = async (query) => {
    setLoading(true);
    setError(null);
    setResearchData(null); // Clear previous results

    try {
      // Use /api/research for production (Vercel handles routing)
      // For local dev, proxy handles it or use http://127.0.0.1:5000/api/research
      const response = await fetch('/api/research', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
      });

      if (!response.ok) {
          const errData = await response.json();
          throw new Error(errData.error || `HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setResearchData(data);
    } catch (error) {
      console.error('Error fetching research data:', error);
      setError(`Failed to fetch research: ${error.message}`);
    } finally {
        setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
          <h1>🤖 AI Research Assistant 🤖</h1>
      </header>
      <main>
          <ResearchForm onResearch={handleResearch} loading={loading} />
          {loading && <div className="loader">Searching the archives... ⏳</div>}
          {error && <div className="error-message">{error}</div>}
          {researchData && (
            <div className="results">
              <h2>{researchData.topic}</h2>
              <p className="summary">{researchData.summary}</p>
              <div className="details">
                  <div className="sources">
                      <h3>Sources:</h3>
                      <ul>
                        {researchData.sources.map((source, index) => (
                          <li key={index}><a href={source} target="_blank" rel="noopener noreferrer">{source}</a></li>
                        ))}
                      </ul>
                  </div>
              </div>
            </div>
          )}
      </main>
      <footer className="App-footer">
          <p>Powered by LangChain & Google Gemini</p>
      </footer>
    </div>
  );
}

export default App;

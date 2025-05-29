import React, { useState } from 'react';

function ResearchForm({ onResearch, loading }) {
  const [query, setQuery] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!query.trim()) return; // Prevent empty submissions
    onResearch(query);
  };

  return (
    <form onSubmit={handleSubmit} className="research-form">
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter your research query here..."
        disabled={loading}
      />
      <button type="submit" disabled={loading}>
          {loading ? 'Researching...' : 'Search'}
      </button>
    </form>
  );
}

export default ResearchForm;

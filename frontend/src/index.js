import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App"; // Ensures App.js is imported

const root = ReactDOM.createRoot(document.getElementById("root")); // Targets the <div id="root">
root.render(
  <React.StrictMode>
    <App /> {/* Renders your main App component */}
  </React.StrictMode>,
);

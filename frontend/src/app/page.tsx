"use client";

import React, { useState, FormEvent } from "react";

interface Message {
  sender: "user" | "bot";
  text: string;
  cypher?: string;
}

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleBuildGraph = async () => {
    setIsLoading(true);
    try {
      const response = await fetch("/api/v1/build-graph", { method: "POST" });
      const data = await response.json();
      if (!response.ok) {
         throw new Error(data.detail || "Failed to build graph");
      }
      alert(`Graph built successfully! Nodes: ${data.nodes_created}, Rels: ${data.relationships_created}`);
    } catch (error) {
      console.error("Build graph error:", error);
      alert(`Error building graph: ${error instanceof Error ? error.message : "Unknown error"}`);
    }
    setIsLoading(false);
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage: Message = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);
    setInput("");

    try {
      const response = await fetch("/api/v1/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: input }),
      });

      if (!response.ok) {
         const errorData = await response.json();
         throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      const botMessage: Message = { sender: "bot", text: data.answer, cypher: data.cypher_query };
      setMessages((prev) => [...prev, botMessage]);

    } catch (error) {
      console.error("Fetch error:", error);
      const errorMessage: Message = { sender: "bot", text: `Error: ${error instanceof Error ? error.message : "An unknown error occurred."}` };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-gray-900 text-white">
      <header className="bg-gray-800 p-4 shadow-md flex justify-between items-center">
        <h1 className="text-xl font-bold">Toot47 GraphRAG Agent</h1>
        <button
          onClick={handleBuildGraph}
          disabled={isLoading}
          className="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded disabled:bg-gray-500"
        >
          {isLoading ? "Processing..." : "Build/Update Graph"}
        </button>
      </header>
      <main className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((msg, index) => (
          <div key={index} className={`flex ${msg.sender === "user" ? "justify-end" : "justify-start"}`}>
            <div className={`max-w-xl p-3 rounded-lg ${msg.sender === "user" ? "bg-indigo-700" : "bg-gray-700"}`}>
              <p className="text-sm">{msg.text}</p>
              {msg.cypher && (
                 <details className="mt-2">
                     <summary className="text-xs text-gray-400 cursor-pointer">Show Cypher Query</summary>
                     <pre className="text-xs bg-gray-800 p-2 rounded-md mt-1 overflow-x-auto"><code>{msg.cypher}</code></pre>
                 </details>
              )}
            </div>
          </div>
        ))}
      </main>
      <footer className="bg-gray-800 p-4">
        <form onSubmit={handleSubmit} className="flex">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask a question about the documents..."
            className="flex-1 bg-gray-700 rounded-l-lg p-2 focus:outline-none focus:ring-2 focus:ring-indigo-500"
            disabled={isLoading}
          />
          <button
            type="submit"
            className="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-r-lg disabled:bg-gray-500"
            disabled={isLoading}
          >
            Send
          </button>
        </form>
      </footer>
    </div>
  );
}

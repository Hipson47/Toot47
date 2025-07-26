"use client";

import React, { useState, FormEvent, useCallback, useRef } from "react";

interface Message {
  sender: "user" | "bot";
  text: string;
  cypher?: string;
  method?: string;
  fallback_used?: boolean;
  source_documents?: string[];
}

interface UploadedFile {
  name: string;
  size: number;
  status: "uploading" | "processed" | "error";
}

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [uploadedFiles, setUploadedFiles] = useState<UploadedFile[]>([]);
  const [isDragOver, setIsDragOver] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [userId] = useState(() => `user_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`);

  const handleBuildGraph = async () => {
    setIsLoading(true);
    try {
      const response = await fetch(`/api/v1/build-graph?user_id=${userId}`, { method: "POST" });
      const data = await response.json();
      if (!response.ok) {
         throw new Error(data.detail || "Failed to build graph");
      }
      
      const successMessage: Message = {
        sender: "bot",
        text: `✅ Graf zbudowany pomyślnie! Utworzono ${data.nodes_created} węzłów i ${data.relationships_created} relacji z plików: ${data.files_processed.join(", ")}`
      };
      setMessages((prev) => [...prev, successMessage]);
    } catch (error) {
      console.error("Build graph error:", error);
      const errorMessage: Message = {
        sender: "bot",
        text: `❌ Błąd podczas budowania grafu: ${error instanceof Error ? error.message : "Nieznany błąd"}`
      };
      setMessages((prev) => [...prev, errorMessage]);
    }
    setIsLoading(false);
  };

  const handleFileUpload = async (files: FileList) => {
    const validFiles = Array.from(files).filter(file => 
      file.type === "text/markdown" || 
      file.name.endsWith(".md") || 
      file.type === "application/pdf" ||
      file.name.endsWith(".pdf")
    );

    if (validFiles.length === 0) {
      alert("Proszę przesłać pliki .md lub .pdf");
      return;
    }

    for (const file of validFiles) {
      const uploadedFile: UploadedFile = {
        name: file.name,
        size: file.size,
        status: "uploading"
      };
      
      setUploadedFiles(prev => [...prev, uploadedFile]);

      try {
        const formData = new FormData();
        formData.append("file", file);
        formData.append("user_id", userId);

        const response = await fetch("/api/v1/upload-file", {
          method: "POST",
          body: formData,
        });

        if (!response.ok) {
          throw new Error(`Failed to upload ${file.name}`);
        }

        setUploadedFiles(prev => 
          prev.map(f => 
            f.name === file.name ? { ...f, status: "processed" } : f
          )
        );

        const successMessage: Message = {
          sender: "bot",
          text: `📄 Plik "${file.name}" został pomyślnie przesłany i dodany do bazy wiedzy!`
        };
        setMessages(prev => [...prev, successMessage]);

      } catch (error) {
        setUploadedFiles(prev => 
          prev.map(f => 
            f.name === file.name ? { ...f, status: "error" } : f
          )
        );
        
        const errorMessage: Message = {
          sender: "bot",
          text: `❌ Błąd podczas przesyłania "${file.name}": ${error instanceof Error ? error.message : "Nieznany błąd"}`
        };
        setMessages(prev => [...prev, errorMessage]);
      }
    }
  };

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragOver(false);
    const files = e.dataTransfer.files;
    if (files.length > 0) {
      handleFileUpload(files);
    }
  }, [userId]);

  const handleDragOver = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragOver(true);
  }, []);

  const handleDragLeave = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragOver(false);
  }, []);

  const handleFileSelect = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (files && files.length > 0) {
      handleFileUpload(files);
    }
    // Reset input value
    if (fileInputRef.current) {
      fileInputRef.current.value = "";
    }
  }, [userId]);

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
        body: JSON.stringify({ question: input, user_id: userId }),
      });

      if (!response.ok) {
         const errorData = await response.json();
         throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      const botMessage: Message = { 
        sender: "bot", 
        text: data.answer, 
        cypher: data.cypher_query,
        method: data.method,
        fallback_used: data.fallback_used,
        source_documents: data.source_documents
      };
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
    <div className="flex h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-indigo-900 text-white">
      {/* Sidebar */}
      <div className="w-80 bg-gray-800/50 backdrop-blur-sm border-r border-gray-700 flex flex-col">
        <div className="p-6 border-b border-gray-700">
          <h1 className="text-2xl font-bold bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent">
            Toot47 AI Agent
          </h1>
          <p className="text-sm text-gray-400 mt-1">Twój inteligentny asystent wiedzy</p>
        </div>
        
        {/* File Upload Area */}
        <div className="p-4 flex-1">
          <h3 className="text-lg font-semibold mb-4">📁 Dodaj pliki</h3>
          
          <div
            className={`border-2 border-dashed rounded-lg p-6 text-center transition-all duration-200 ${
              isDragOver 
                ? "border-blue-500 bg-blue-500/10" 
                : "border-gray-600 hover:border-gray-500"
            }`}
            onDrop={handleDrop}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
          >
            <div className="space-y-3">
              <div className="text-4xl">📄</div>
              <div>
                <p className="text-sm font-medium">Przeciągnij pliki tutaj</p>
                <p className="text-xs text-gray-400">lub kliknij aby wybrać</p>
              </div>
              <input
                ref={fileInputRef}
                type="file"
                multiple
                accept=".md,.pdf"
                onChange={handleFileSelect}
                className="hidden"
              />
              <button
                onClick={() => fileInputRef.current?.click()}
                className="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg text-sm transition-colors"
              >
                Wybierz pliki
              </button>
              <p className="text-xs text-gray-500">Obsługiwane: .md, .pdf</p>
            </div>
          </div>

          {/* Uploaded Files List */}
          {uploadedFiles.length > 0 && (
            <div className="mt-4">
              <h4 className="text-sm font-medium mb-2">Przesłane pliki:</h4>
              <div className="space-y-2 max-h-40 overflow-y-auto">
                {uploadedFiles.map((file, index) => (
                  <div key={index} className="flex items-center space-x-2 text-xs p-2 bg-gray-700/50 rounded">
                    <div className={`w-2 h-2 rounded-full ${
                      file.status === "processed" ? "bg-green-500" :
                      file.status === "error" ? "bg-red-500" : "bg-yellow-500"
                    }`} />
                    <span className="truncate flex-1">{file.name}</span>
                    <span className="text-gray-400">{(file.size / 1024).toFixed(1)}KB</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          <div className="mt-6 space-y-3">
            <button
              onClick={handleBuildGraph}
              disabled={isLoading}
              className="w-full bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 text-white font-medium py-3 rounded-lg transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {isLoading ? "🔄 Przetwarzanie..." : "🚀 Zbuduj bazę wiedzy"}
            </button>
            
            <div className="text-xs text-gray-400 space-y-1">
              <p>👤 User ID: {userId.substring(0, 16)}...</p>
              <p>📊 Plików: {uploadedFiles.filter(f => f.status === "processed").length}</p>
            </div>
          </div>
        </div>
      </div>

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col">
        {/* Chat Messages */}
        <div className="flex-1 overflow-y-auto p-6 space-y-4">
          {messages.length === 0 ? (
            <div className="flex-1 flex items-center justify-center">
              <div className="text-center space-y-4 max-w-md">
                <div className="text-6xl">🤖</div>
                <h2 className="text-2xl font-bold">Witaj w Toot47!</h2>
                <p className="text-gray-400">Przesyłaj pliki i zadawaj pytania o swoją bazę wiedzy.</p>
                <div className="grid grid-cols-1 gap-2 text-sm">
                  <div className="bg-gray-800/50 p-3 rounded-lg">
                    <strong>Przykładowe pytania:</strong>
                    <ul className="text-left mt-1 space-y-1 text-gray-300">
                      <li>• "Opowiedz mi o projekcie Toot47"</li>
                      <li>• "Jakie technologie są używane?"</li>
                      <li>• "Jak działa GraphRAG?"</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          ) : (
            messages.map((msg, index) => (
              <div key={index} className={`flex ${msg.sender === "user" ? "justify-end" : "justify-start"}`}>
                <div className={`max-w-2xl p-4 rounded-xl shadow-lg ${
                  msg.sender === "user" 
                    ? "bg-gradient-to-r from-blue-600 to-purple-600 text-white" 
                    : "bg-gray-800/70 border border-gray-700"
                }`}>
                  <div className="flex items-start space-x-3">
                    <div className="text-2xl">
                      {msg.sender === "user" ? "👤" : "🤖"}
                    </div>
                    <div className="flex-1">
                      <p className="text-sm leading-relaxed">{msg.text}</p>
                      
                      {/* Metadata */}
                      {msg.method && (
                        <div className="mt-2 flex items-center space-x-2 text-xs">
                          <span className={`px-2 py-1 rounded-full ${
                            msg.method === "graph_rag" ? "bg-green-500/20 text-green-400" :
                            msg.method === "vector_rag" ? "bg-blue-500/20 text-blue-400" :
                            "bg-red-500/20 text-red-400"
                          }`}>
                            {msg.method === "graph_rag" ? "📊 GraphRAG" :
                             msg.method === "vector_rag" ? "🔍 VectorRAG" : "❌ Error"}
                          </span>
                          {msg.fallback_used && (
                            <span className="text-yellow-400">⚠️ Fallback</span>
                          )}
                        </div>
                      )}

                      {/* Source Documents */}
                      {msg.source_documents && msg.source_documents.length > 0 && (
                        <details className="mt-2">
                          <summary className="text-xs text-gray-400 cursor-pointer hover:text-gray-300">
                            📚 Źródła ({msg.source_documents.length})
                          </summary>
                          <div className="mt-1 space-y-1">
                            {msg.source_documents.slice(0, 3).map((doc, i) => (
                              <div key={i} className="text-xs bg-gray-900/50 p-2 rounded border-l-2 border-blue-500">
                                {doc.substring(0, 150)}...
                              </div>
                            ))}
                          </div>
                        </details>
                      )}

                      {/* Cypher Query */}
                      {msg.cypher && (
                         <details className="mt-2">
                             <summary className="text-xs text-gray-400 cursor-pointer hover:text-gray-300">
                               🗄️ Zapytanie Cypher
                             </summary>
                             <pre className="text-xs bg-gray-900/70 p-2 rounded-md mt-1 overflow-x-auto border border-gray-700">
                               <code>{msg.cypher}</code>
                             </pre>
                         </details>
                      )}
                    </div>
                  </div>
                </div>
              </div>
            ))
          )}
          {isLoading && (
            <div className="flex justify-start">
              <div className="bg-gray-800/70 border border-gray-700 p-4 rounded-xl">
                <div className="flex items-center space-x-3">
                  <div className="text-2xl">🤖</div>
                  <div className="flex space-x-1">
                    <div className="w-2 h-2 bg-blue-500 rounded-full animate-bounce"></div>
                    <div className="w-2 h-2 bg-blue-500 rounded-full animate-bounce" style={{animationDelay: "0.1s"}}></div>
                    <div className="w-2 h-2 bg-blue-500 rounded-full animate-bounce" style={{animationDelay: "0.2s"}}></div>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Input Area */}
        <div className="border-t border-gray-700 bg-gray-800/30 backdrop-blur-sm p-4">
          <form onSubmit={handleSubmit} className="flex space-x-3">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Zadaj pytanie o swoją bazę wiedzy..."
              className="flex-1 bg-gray-700/50 border border-gray-600 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
              disabled={isLoading}
            />
            <button
              type="submit"
              className="bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white font-medium px-6 py-3 rounded-xl transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
              disabled={isLoading || !input.trim()}
            >
              {isLoading ? "⏳" : "📤"}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

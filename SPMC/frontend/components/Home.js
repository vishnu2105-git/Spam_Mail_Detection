import React, { useState } from 'react';
import axios from 'axios'; 

export const Home = () => {
  const [value, setValue] = useState("");
  const [result, setResult] = useState("---"); 

  const handleResponse = async () => {
    try {
      const res = await axios.post('http://localhost:8000/predict', { message: value });
      setResult(res.data.Predicted_Class || res.data);
    } 
    catch (error) {
      console.error("Error fetching prediction:", error);
      setResult(`Error: ${error.response ? error.response.data.detail : error.message}`);
    }
  };
  

  return (
    <div>
      <header>
        <div className="container">
          <h1>Spam Mail Detector</h1>
        </div>
      </header>
      <main className="container2">
        <section className="input-section">
          <textarea
            onChange={(e) => setValue(e.target.value)} 
            id="messageInput"
            placeholder="Type or paste your message here..."
            value={value} 
          ></textarea>
          <button onClick={handleResponse} id="checkMessageBtn">
            Check Message
          </button>
        </section>
        <section className="result-section" id="resultSection">
          <p id="result">
            Result: {result}
          </p>
        </section>
      </main>
    </div>
  );
};

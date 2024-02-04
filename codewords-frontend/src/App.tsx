
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';



function App() {
  const [codeword, setCodeword] = useState('');
  const [actionId, setActionId] = useState('');
  const [result, setResult] = useState<string | string[]>('');

  const fetchActionId = async () => {
    try {
      const response = await axios.get(`http://localhost:3000/action/by_codeword/${codeword}`);
      setResult(`Action ID: ${response.data.id}`);
      console.log(response.data.codeword); 
    } catch (error) {
      setResult('Action not found');
    }
  };

  const fetchCodewords = async () => {
    try {
      const response = await axios.get(`http://localhost:3000/action/by_id/${actionId}`);
      if (response.data.codeword) {
        setResult(`Codeword: ${response.data.codeword}`);
        console.log(response.data.codeword); 
      } else if (response.data.codewords) {
        setResult(`Codewords: ${response.data.codewords.join(', ')}`);
      }
    } catch (error) {
      setResult('Codewords not found');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <div>
          <input
            type="text"
            value={codeword}
            onChange={(e) => setCodeword(e.target.value)}
            placeholder="Enter Codeword"
          />
          <button onClick={fetchActionId}>Get Action ID</button>
        </div>
        <div>
          <input
            type="text"
            value={actionId}
            onChange={(e) => setActionId(e.target.value)}
            placeholder="Enter Action ID"
          />
          <button onClick={fetchCodewords}>Get Codewords</button>
        </div>
        {result && <p>{result}</p>}
      </header>
    </div>
  );
}

export default App;

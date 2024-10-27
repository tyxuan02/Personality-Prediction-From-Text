import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Home = () => {
  const [inputType, setInputType] = useState('text');
  const [input, setInput] = useState('');
  const [predictedInput, setPredictedInput] = useState('');
  const [output, setOutput] = useState('');
  const [isButtonDisabled, setIsButtonDisabled] = useState(true);

  useEffect(() => {
    if ((inputType === 'text' && input.split(' ').length > 5) || (inputType === 'file' && input.length > 0)) {
      setIsButtonDisabled(false);
    } else {
      setIsButtonDisabled(true);
    }
  }, [inputType, input]);

  const predict = (e) => {
    e.preventDefault();
    axios.post('/predict', { inputType, input })
      .then(res => {
        setOutput(res.data);
        setPredictedInput(input);
      })
      .catch(err => console.log(err));
  };

  return (
    <div className="home-container">
      <h1 className="text-center">Predict MBTI Type</h1>
      <div className="input-container">
        <form className="form-container" action='/' method="post">
          <div className="input-type-container">
            <label className="select-input-label" htmlFor="inputType">Input Type:</label>
            <select className="form-select" id="inputType" name="inputType" value={inputType} onChange={(e) => setInputType(e.target.value)}>
              <option value="text">Text</option>
              <option value="file">File</option>
            </select>
          </div>
          {inputType === 'text' && (
            <div className="input-text-container">
              <textarea className="input-text-area" id="textInput" name="textInput" rows="5" placeholder="Enter your text here..." onChange={(e) => setInput(e.target.value)}></textarea>
            </div>
          )}
          {inputType === 'file' && (
            <div className='input-file-container'>
              <input className="input-file" type="file" id="fileInput" name="fileInput" multiple accept=".csv, .xlsx" />
            </div>
          )}
          <button type="submit" className="predict-btn" style={isButtonDisabled ? { backgroundColor: '#ccc' } : {}} onClick={predict} disabled={isButtonDisabled}>Predict</button>
        </form>
      </div>

      {output && (
        <div className="output-container">
          <h3 className="input-text-header">Input Text</h3>
          <p className="input-text">{predictedInput}</p>
          <h3 className="output-text-header">Predicted MBTI Type</h3>
          <p className="output-text">{output}</p>
        </div>
      )}
    </div>
  );
}

export default Home
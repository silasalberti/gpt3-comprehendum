import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import 'semantic-ui-css/semantic.min.css';
import { Button, Input } from 'semantic-ui-react';
import InputComponent from './InputComponent';

function App() {
  const [searchApiResult, updateSearchApiResult] = useState();
  return (
    <div
      className="App"
      style={{
        backgroundColor: '#F1F7EE',
        height: '100%',
      }}
    >
      <div
        className="header"
        style={{
          height: '20%',
          backgroundColor: '#B0BEA9',
          color: 'white',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'flex-start',
        }}
      >
        <h1
          style={{
            fontSize: '30px',
          }}
        >
          Legal &amp; Compliance Companion
        </h1>
      </div>
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          height: '80%',
          gap: '20px',
          fontSize: '30px',
          paddingBottom: '20%',
        }}
      >
        <InputComponent updateSearchApiResult={updateSearchApiResult} />
      </div>
    </div>
  );
}

export default App;

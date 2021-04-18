import React, { useState, useEffect } from 'react';

import 'semantic-ui-css/semantic.min.css';
import { Loader, Container } from 'semantic-ui-react';
import InputComponent from './InputComponent';

function App() {
  const [searchApiResult, updateSearchApiResult] = useState({
    result: {
      data: {
        answer: '',
      },
    },
    error: {},
    requested: false,
  });
  const [apiCallInProgress, updateApiCallInProgress] = useState(false);
  const { requested, result, error } = searchApiResult;

  useEffect(() => {
    if (apiCallInProgress) {
      //TODO: css transitions
    }
  });
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
          height: '15%',
          backgroundColor: '#B0BEA9',
          color: 'white',
          display: 'flex',
          alignItems: 'flex-end',
          justifyContent: 'flex-start',
          paddingLeft: '10%',
          paddingBottom: '25px',
          gap: '20px',
        }}
      >
        <img
          src="Siemens-logo.svg"
          style={{
            width: '200px',
          }}
        />
        <h1
          style={{
            fontSize: '40px',
            fontFamily: 'Lato',
            fontWeight: 300,
          }}
        >
          Legal &amp; Compliance Companion
        </h1>
      </div>
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          height: '80%',
          gap: '20px',
          fontSize: '30px',
          paddingBottom: '20%',
        }}
      >
        <InputComponent
          updateSearchApiResult={updateSearchApiResult}
          updateApiCallInProgress={updateApiCallInProgress}
        />
        {apiCallInProgress && <Loader style={{ marginTop: '10%' }} active />}
        {!apiCallInProgress && requested && !error && (
          <Container
            text
            style={{
              wordBreak: 'break-all',
            }}
          >
            {result.data.answer}
          </Container>
        )}
      </div>
    </div>
  );
}

export default App;

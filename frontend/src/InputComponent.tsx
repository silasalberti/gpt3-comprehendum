import { render } from '@testing-library/react';
import React, { useState } from 'react';
import axios from 'axios';
import { Input } from 'semantic-ui-react';
import { BASE_URL, QUESTION_ENDPOINT } from './constants/apiEndpoints';

const handleInput = (updateInput: Function) => {
  return (e: any) => {
    updateInput(e.target.value);
  };
};

const handleKeyPress = (input: string, updateSearchApiResult: Function) => {
  return async (e: any) => {
    if (e.key === 'Enter') {
      try {
        const result = await axios.post(`${BASE_URL}${QUESTION_ENDPOINT}`, {
          query: input,
        });
        updateSearchApiResult(result);
      } catch (err) {
        updateSearchApiResult({
          error: err,
        });
      }
    }
  };
};

export default function InputComponent(props: any) {
  const { updateSearchApiResult } = props;
  const [input, updateInput] = useState('');
  return (
    <>
      <Input
        style={{
          width: '80%',
        }}
        value={input}
        onChange={handleInput(updateInput)}
        onKeyPress={handleKeyPress(input, updateSearchApiResult)}
      />
    </>
  );
}

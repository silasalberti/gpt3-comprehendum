import React, { useState } from 'react';
import axios from 'axios';
import { Input, Loader } from 'semantic-ui-react';
import { BASE_URL, QUESTION_ENDPOINT } from './constants/apiEndpoints';

const handleInput = (updateInput: Function) => {
  return (e: any) => {
    updateInput(e.target.value);
  };
};

const handleKeyPress = (
  input: string,
  updateSearchApiResult: Function,
  updateApiCallInProgress: Function
) => {
  return async (e: any) => {
    if (e.key === 'Enter') {
      updateApiCallInProgress(true);
      try {
        const result = await axios.post(`${BASE_URL}${QUESTION_ENDPOINT}`, {
          query: input,
        });
        console.log(result);
        updateSearchApiResult({
          result: result,
          error: false,
          requested: true,
        });
      } catch (err) {
        updateSearchApiResult({
          result: false,
          error: err,
          requested: true,
        });
      }
      updateApiCallInProgress(false);
    }
  };
};

export default function InputComponent(props: any) {
  const { updateSearchApiResult, updateApiCallInProgress } = props;
  const [input, updateInput] = useState('');
  return (
    <>
      <Input
        style={{
          width: '80%',
        }}
        value={input}
        onChange={handleInput(updateInput)}
        onKeyPress={handleKeyPress(
          input,
          updateSearchApiResult,
          updateApiCallInProgress
        )}
      />
    </>
  );
}

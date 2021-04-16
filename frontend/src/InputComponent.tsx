import { render } from '@testing-library/react'
import React, {useState} from 'react'

import {Input} from 'semantic-ui-react'

const handleInput = ((e: any)=>{
    e.target.value 

})

export default function InputComponent(){
    return(
        <div>
            <Input onChange={handleInput} />
        </div>
    );
}


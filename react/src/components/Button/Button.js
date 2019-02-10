import React from 'react';
import './Button.css';

const renderButton = props => {
    return (
        <button 
            className={props.buttonStyle}
            disabled={props.disabled}
            onClick={props.clicked}
        >
            {props.children}
        </button>
    );
}

export default renderButton;
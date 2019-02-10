// external
import React from 'react';
// style
import './Spinner.css';

const spinner = () => (
    <div className={"spinner-wrapper"}>
        <div className={"hollowLoader"}>
            <div className={"largeBox"}></div>
            <div className={"smallBox"}></div>
        </div>
    </div>
);

export default spinner;
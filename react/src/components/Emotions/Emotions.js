// external
import React, { Component, Fragment } from 'react';
// images
import anger from '../../images/Emodji/anger.png';
import fear from '../../images/Emodji/fear.png';
import happiness from '../../images/Emodji/happiness.png';
import neutral from '../../images/Emodji/neutral.png';
import sadness from '../../images/Emodji/sadness.png';
import surprise from '../../images/Emodji/surprise.png';

// style
import './Emotions.css';

const emotionsMap = [
    {name: 'anger', path: anger},
    {name: 'fear', path: fear},
    {name: 'happiness', path: happiness},
    {name: 'neutral', path: neutral},
    {name: 'sadness', path: sadness},
    {name: 'surprise', path: surprise},
];

class Emotions extends Component {
    state = {
        selectedEmotions: []
    }

    toggleEmotion = emotion => {
        const emotions = [...this.state.selectedEmotions];

        if (this.state.selectedEmotions.includes(emotion)) {
            const index = emotions.indexOf(emotion);
            emotions.splice(index, 1);
        } else {
            emotions.push(emotion);
        }

        this.setState({ selectedEmotions: emotions });
    }

    render() {
        const buttonStyle = Boolean(this.state.selectedEmotions.length) ? 'submit-button' : 'submit-button button-opacity';
        return (
            <Fragment>
                <div className={'emotions-title'}>Select Emotions</div>
                <div className={'emotion-wrapper'}>
                    {emotionsMap.map((emotion, index) => {
                        const emotionStyle = this.state.selectedEmotions.includes(emotion.name) ? 'emotion opacity' : 'emotion';

                        return (
                            <div key={index} className={emotionStyle} onClick={() => this.toggleEmotion(emotion.name)}>
                                <span className="popover above">{emotion.name}</span>
                                <img src={emotion.path} alt="emotion" onDragStart={event => event.preventDefault()} />
                            </div>
                        );
                    })}
                </div>
                <button 
                    className={buttonStyle}
                    disabled={!this.state.selectedEmotions.length}
                    onClick={() => this.props.submit(this.state.selectedEmotions)}
                >Submit</button>
            </Fragment>
        );
    }
}

export default Emotions;
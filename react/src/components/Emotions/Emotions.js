// external
import React from 'react';
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

const renderEmotions = props => {
    return (
        <div className={'emotion-wrapper'}>
            {emotionsMap.map((emotion, index) => {
                return (
                    <div key={index} className={'emotion'} onClick={() => props.getEmotionPhotos(emotion)}>
                        <span className="popover above">{emotion.name}</span>
                        <img src={emotion.path} alt="emotion" onDragStart={event => event.preventDefault()} />
                    </div>
                );
            })}
        </div>
    );
};

export default renderEmotions;
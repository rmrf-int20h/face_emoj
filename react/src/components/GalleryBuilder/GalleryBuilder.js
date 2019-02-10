// external
import React from 'react';
// style
import './GalleryBuilder.css';

const galleryBuilder = props => {
    return (
        <main>
            {props.photos.map((photoURL, index) => {
                return <div key={index}><img src={photoURL} alt="int20h" onDragStart={event => event.preventDefault()} /></div>
            })}
        </main>
    );
}

export default galleryBuilder;
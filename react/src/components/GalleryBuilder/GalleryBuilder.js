// external
import React, { Fragment } from 'react';
// internal
import Button from '../Button/Button';
// style
import './GalleryBuilder.css';

const galleryBuilder = props => {
    return (
        <Fragment>
            <Button
                buttonStyle={'return-button'}
                disabled={false}
                clicked={props.returnHandler}
            >Return</Button>
            <main>
                {props.photos.map((photoURL, index) => {
                    return <div key={index}><img src={photoURL} alt="int20h" onDragStart={event => event.preventDefault()} /></div>
                })}
            </main>
        </Fragment>
    );
}

export default galleryBuilder;
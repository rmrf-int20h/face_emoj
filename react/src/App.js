// external
import React, { Component, Fragment } from 'react';
// internal
import Emotions from '../src/components/Emotions/Emotions';
import Spinner from '../src/components/Spinner/Spinner';
import GalleryBuilder from '../src/components/GalleryBuilder/GalleryBuilder';
import axios from './axios';
// style
import './App.css';


class App extends Component {
    state = {
        isLoading: true,
        photos: []
    }

    componentDidMount() {
        const tag = '',
        apiKey = '4a2173dec440a23318af07a5354b082f',
        albumId = 72157674388093532,
        userId = '144522605@N06'

        axios.get(`https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=${apiKey}&photoset_id=${albumId}&user_id=${userId}&tags=${tag}&format=json&nojsoncallback=1`)
            .then(response => {
                const photos = response.data.photos.photo,
                    photoURLs = [];

                photos.forEach(photo => {
                    const photoURL = `http://farm${photo.farm}.staticflickr.com/${photo.server}/${photo.id}_${photo.secret}.jpg`;
                    photoURLs.push(photoURL);
                });

                this.setState({ isLoading: false, photos: photoURLs });
            });
    }

    getEmotionPhotos = emotion => {
        console.log(emotion);
        // TODO: POST method for get photos by emotion type.
    }

    render() {
        let content = <Spinner/>;

        if (!this.state.isLoading) {
            content = (
                <Fragment>
                    <Emotions getEmotionPhotos={this.getEmotionPhotos}/>
                    <GalleryBuilder photos={this.state.photos} />
                </Fragment>
            );
        }

        return content;
    }
}

export default App;

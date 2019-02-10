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
        isShowGallety: false,
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

    submitEmotions = emotions => {
        const selectedEmotions = emotions.join('/'),
            proxyURL = "https://cors-anywhere.herokuapp.com/",
            url = 'http://int20h-face.herokuapp.com/db_select_emotions/';

        this.setState({ isLoading: true });

        axios.get(proxyURL + url + `?emotions=${selectedEmotions}`)
            .then(response => {
                this.setState({ isShowGallety: true, isLoading: false });
            });
    }

    returnHandler = () => {
        this.setState({ isShowGallety: false });
    }

    render() {
        let content = <Spinner/>;

        if (!this.state.isLoading) {
            content = (
                <Fragment>
                    {this.state.isShowGallety ? <GalleryBuilder returnHandler={this.returnHandler} photos={this.state.photos} /> : <Emotions submit={this.submitEmotions}/>}
                </Fragment>
            );
        }

        return content;
    }
}

export default App;

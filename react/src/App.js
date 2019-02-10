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
        isLoading: false,
        isShowGallety: false,
        photos: []
    }

    submitEmotions = emotions => {
        const selectedEmotions = emotions.join('/'),
            proxyURL = "https://cors-anywhere.herokuapp.com/",
            url = 'http://int20h-face.herokuapp.com/db_select_emotions/';

        this.setState({ isLoading: true });

        axios.get(proxyURL + url + `?emotions=${selectedEmotions}`)
            .then(response => {
                const photosURLs = [];

                response.data.forEach(photoData => {
                    photosURLs.push(photoData[1])
                });

                this.setState({
                    isShowGallety: true,
                    isLoading: false,
                    photos: photosURLs
                });
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

import flickrapi
import requests
import logging

logger = logging.getLogger('django.server')


def fetchPhotosAndEmotions():
    photosUrl = fetchPhotosFromFlickr()
    emotionsPerPhoto = getEmotionsForPhotos(photosUrl)
    return emotionsPerPhoto

def fetchPhotosFromFlickr():
    logger.info('Fetching photos URLs from Flickr')

    flickr_api_key = '491f357d68769d6c5dbe169a03d07ab6'
    flickr_secret_key = 'a41ee7c867b26e6c'
    photoset_id = '72157674388093532'
    user_id = '144522605@N06'

    url_get_photoset_photos = "https://api.flickr.com/services/rest/?method=flickr.photosets.getPhotos&api_key=" + flickr_api_key + \
                                   "&format=json&nojsoncallback=1&photoset_id=" + photoset_id + \
                                   "&user_id=" + user_id
    all_photos = set()
    response_photos = requests.post(url_get_photoset_photos, dict())

    JSON_response_photos = response_photos.json()
    photos = JSON_response_photos['photoset']["photo"]
    for photo in photos:
        photo_link = "http://farm" + str(photo["farm"]) + ".staticflickr.com/" + str(photo["server"]) + "/" \
                    + str(photo["id"]) + "_" + str(photo["secret"]) + ".jpg"
        all_photos.add(photo_link)

    logger.info('Photos fetched from Flickr, amount: ' + str(len(all_photos)))
    return all_photos

def getEmotionsForPhotos(urls):
    logger.info('Starting fetching emotions from Face++')
    facepp_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'

    face_api_key = 'agK4O4DmlHM3L2xGEquurPshOi4PcUed'
    face_api_secret = 'LayltWoJGz_-pQznk78V1SA8zTXnEtQ0'

    args = dict()
    args['api_key'] = face_api_key
    args['api_secret'] = face_api_secret
    args['return_attributes'] = 'emotion'

    results = list()

    for url in urls:
        args['image_url'] = url
        response = requests.post(facepp_url, args)
        result = dict()
        result['url'] = url
        emotionOnPhoto = set()
        logger.info('Response from Face++ received')
        logger.info(response.json())

        faces = response.json().get('faces')
        if faces is not None:
            for face in faces:
                attributes = face.get('attributes')
                if attributes is not None:
                    emotionOfFace = attributes.get('emotion')
                    if emotionOfFace is not None:
                        for emotion in emotionOfFace:
                            if emotionOfFace[emotion] >= 50:
                                emotionOnPhoto.add(emotion)
                                break

        if len(emotionOnPhoto) >= 1:
            result['emotions'] = emotionOnPhoto
            results.append(result)
    print(results)
    return results

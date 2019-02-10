from django.shortcuts import render
from django.http import HttpResponse
from server.database import db_worker
from server.api import api_worker

import logging
logger = logging.getLogger('django.server')

# Create your views here.
def index(request):
    return render(request, "index.html")

# API METHODS
def api_flickr(request):
    response = api_worker.fetchPhotosFromFlickr()
    if response:
        logger.info('flickr api called successfully. views.py')
        return HttpResponse(response)
    else:
        logger.error('flickr api call errored. views.py')
        return HttpResponse('error')

def receive_emotions_per_photo(request):
    response = api_worker.fetchPhotosAndEmotions()
    if response:
        logger.info('emotions per photo received successfully. views.py')
        logger.info('start inserting data into DB. views.py')
        for image in response:
            db_worker.insertFullData(image)
            
        return HttpResponse(response)
    else:
        logger.error('receiving emotions per photo errored. views.py')
        return HttpResponse('error')

# DATABASE METHODS
def db_managment(request):
    return render(request, 'database_managment.html')

def db_create_table(request):
    if db_worker.createTable():
        logger.info('Table created successfully. views.py')
        return HttpResponse('success')
    else:
        logger.error('Table creation errored. views.py')
        return HttpResponse('error')
def db_delete_table(request):
    if db_worker.deleteTable():
        logger.info('Table dropped successfully. views.py')
        return HttpResponse('success')
    else:
        logger.error('Table droping errored. views.py')
        return HttpResponse('error')

def db_select_all(request):
    aData = db_worker.selectData();
    return HttpResponse(aData);
def db_select_emotions(request):
    aData = db_worker.selectDataForEmotions(request);
    return HttpResponse(aData);

def db_insert_row(request):
    if db_worker.insertData(request):
        logger.info('Table row inserted successfully. views.py')
        return render(request, 'database_managment.html')
    else:
        logger.error('Table row insertion errored. views.py')
        return HttpResponse('error')

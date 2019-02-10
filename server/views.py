from django.shortcuts import render
from django.http import HttpResponse
from server.database import db_worker

import logging
logger = logging.getLogger('django.server')

# Create your views here.
def index(request):
    return render(request, "index.html")

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

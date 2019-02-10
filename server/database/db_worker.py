import psycopg2
import logging
import json

logger = logging.getLogger('django.server')

def createTable():
    conn = False
    try:
        logger.info('Begin creating table in DB')
        conn = getConnection()
        cursor = conn.cursor()

        # faceCoords array of strings containing width/top/left/height
        create_table_query = '''CREATE TABLE images
                            (id             SERIAL PRIMARY KEY  NOT NULL,
                             url            TEXT    NOT NULL,
                             faceToken      TEXT,
                             faceCoords     VARCHAR[],
                             hasHappiness   BOOLEAN,
                             hasSadness     BOOLEAN,
                             hasNeutral     BOOLEAN,
                             hasDisgust     BOOLEAN,
                             hasAnger       BOOLEAN,
                             hasSurprise    BOOLEAN,
                             hasFear        BOOLEAN);'''

        cursor.execute(create_table_query)
        conn.commit()
        logger.info('Table created successfully in PostgreSQL')
        return True
    except (Exception) as error:
        logger.error('Error while creating PostgreSQL table', error)
    finally:
        closeConnection(conn, cursor)

def deleteTable():
    try:
        logger.info('Deleting table in DB')
        conn = getConnection()
        cursor = conn.cursor()

        drop_table_query = 'DROP TABLE images;'

        cursor.execute(drop_table_query)
        conn.commit()
        logger.info('Table dropped successfully in PostgreSQL')
        return True
    except Exception as error:
        logger.error('Error while deleting PostgreSQL table', error)
    finally:
        closeConnection(conn, cursor)

def selectData():
    try:
        logger.info('Fetching data from DB')
        conn = getConnection()
        cursor = conn.cursor()

        select_table_query = 'SELECT * FROM images;'

        cursor.execute(select_table_query)
        images_records = cursor.fetchall()

        logger.info('Data fetched successfully in PostgreSQL')
        return json.dumps(images_records)
    except Exception as error:
        logger.error('Error while fetching data from PostgreSQL table', error)
    finally:
        closeConnection(conn, cursor)

def selectDataForEmotions(request):
    try:
        logger.info('Fetching data from DB')
        conn = getConnection()
        cursor = conn.cursor()

        emotionsToWhereParts = {
            'happiness': 'hasHappiness = true',
            'sadness': 'hasSadness = true',
            'neutral': 'hasNeutral = true',
            'disgust': 'hasDisgust = true',
            'anger': 'hasAnger = true',
            'surprise': 'hasSurprise = true',
            'fear': 'hasFear = true'
        }

        for key in request.GET:
            logger.info(key + ": " + request.GET.get(key))

        emotions = request.GET.get('emotions').split('/')
        where_part = " "
        for emotion in emotions:
            if emotion in emotionsToWhereParts:
                where_part = appendEmotionToWhere(where_part, emotionsToWhereParts.get(emotion))

        select_table_query = 'SELECT * FROM images WHERE ' + where_part + ';'

        cursor.execute(select_table_query)
        images_records = cursor.fetchall()

        logger.info('Data fetched successfully in PostgreSQL')
        return json.dumps(images_records)
    except Exception as error:
        logger.error('Error while fetching data from PostgreSQL table', error)
    finally:
        closeConnection(conn, cursor)

def insertData(request):
    try:
        logger.info('Inserting data from DB')
        conn = getConnection()
        cursor = conn.cursor()

        insert_query = """INSERT INTO images
            (url, faceToken, hasHappiness, hasSadness, hasNeutral, hasDisgust, hasAnger, hasSurprise, hasFear)
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        record_to_insert = (request.GET.get('url'),
                            request.GET.get('facetoken'),
                            request.GET.get('happiness'),
                            request.GET.get('sadness'),
                            request.GET.get('neutral'),
                            request.GET.get('disgust'),
                            request.GET.get('anger'),
                            request.GET.get('surprise'),
                            request.GET.get('fear'))
        cursor.execute(insert_query, record_to_insert)
        conn.commit()

        logger.info('Data inserted successfully in PostgreSQL', cursor.rowcount)
        return True
    except Exception as error:
        logger.error('Error while inserted data in PostgreSQL table', error)
    finally:
        closeConnection(conn, cursor)


# UTILS METHODS
def getConnection():
    return psycopg2.connect(dbname='dbfqddaq60d6im',
                            user='wxowaxhcpecbzi',
                            password='9bb1e5fa868b59b15139f428e53093270bcd8e24badbbe8769993409a38aa156',
                            port="5432",
                            host='ec2-54-217-208-105.eu-west-1.compute.amazonaws.com')
def closeConnection(connection, cursor):
    if connection:
        cursor.close()
        connection.close()
        logger.info('PostgreSQL connection is closed')
def appendEmotionToWhere(where, clause):
    if len(where) > 1:
        where += ' and ' + clause
    else:
        where += clause
    return where

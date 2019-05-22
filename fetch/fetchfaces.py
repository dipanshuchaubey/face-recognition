import face_recognition
import requests
import numpy as np
import json
from auth import db
import pickle

def fetchAllFaces():

    # setup database connection
    mydb = db.databaseConnection()
    mycursor = mydb.cursor()

    # mysql query
    mycursor.execute("SELECT image, name FROM face_recog")

    # Get the results
    rows = mycursor.fetchall()

    known_face_encodings = []
    face_name = []
    
    for each in rows:

        known_face_encodings.append(pickle.loads(each[0])[0])
        face_name.append(each[1])

    return known_face_encodings, face_name

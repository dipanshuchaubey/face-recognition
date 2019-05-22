import face_recognition
import requests
import numpy as np
import json
from auth import db
import pickle

def findFace(face_locations, face_encodings):

    # setup database connection
    mydb = db.databaseConnection()
    mycursor = mydb.cursor()

    # convert face encoding into BLOB string
    face_pickled_data = pickle.dumps(face_encodings)

    # mysql query
    mycursor.execute("SELECT image, name FROM face_recog")

    # Get the results
    rows = mycursor.fetchall()

    for each in rows:

        known_face_encodings = pickle.loads(each[0])
        face_name = each[1]

        if len(rows) == 0:
            return False

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            if True in matches:
                return face_name

            else:
                break
                        
        

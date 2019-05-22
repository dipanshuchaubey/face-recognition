import face_recognition
import requests
import json
from auth import db
import pickle

# load image
load_image = face_recognition.load_image_file('./img/groups/Dipanshu.jpeg')

# find face locations 
face_locations = face_recognition.face_locations(load_image)

# find face encoding
face_encodings = face_recognition.face_encodings(load_image, face_locations)

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

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        if True in matches:
            print(f'Face matches with {face_name}')
            break

        else:
            break
                        
        

import face_recognition
import requests
import json
from auth import db
from identify import findface
import pickle

# load image
load_image = face_recognition.load_image_file('./img/groups/Dipanshu.jpeg')

# find face locations
face_locations = face_recognition.face_locations(load_image)

# get face encodings
face_encoding = face_recognition.face_encodings(load_image, face_locations)

# search for exsisting faces
exsisting_face_name = findface.findFace(face_locations, face_encoding)

if (exsisting_face_name):
    print("FACE FOUND")
    print(f'Face matches with {exsisting_face_name}')


else:
    print("FACE NOT FOUND")
    # input name
    name = input('Enter the name of person: ')

    # convert name into BLOB string
    face_pickled_data = pickle.dumps(face_encoding)

    # setup database connection
    mydb = db.databaseConnection()
    mycursor = mydb.cursor()

    # mysql query
    sql = "INSERT INTO face_recog (image,name) VALUES (%s, %s)"
    val = (face_pickled_data, name)
    mycursor.execute(sql, val)
    mydb.commit()

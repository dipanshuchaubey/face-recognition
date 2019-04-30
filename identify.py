import face_recognition
import requests
import json
import mysql.connector
import pickle

# load image
load_image = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
load_image1 = face_recognition.load_image_file('./img/unknown/bill-gates-4.jpg')

# find face locations 
face_locations = face_recognition.face_locations(load_image)
face_locations1 = face_recognition.face_locations(load_image1)

# find face encoding
face_encoding = face_recognition.face_encodings(load_image, face_locations)
face_encoding1 = face_recognition.face_encodings(load_image1, face_locations1)


for (top, right, bottom, left), face_encoding in zip(face_locations, face_encoding1):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(face_encoding, face_encoding1)


    # If a match was found in known_face_encodings, just use the first one.
    if True in matches:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="test"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT image, name FROM face_recog")
        rows = mycursor.fetchall()

        ## Get the results
        for each in rows:
            face_data = pickle.loads(each[0])
            print(face_data)
                
    else:
        print('Doesnt work')

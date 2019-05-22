import face_recognition
import requests
import json
from auth import db
import pickle

# Mysql config
mydb = db.databaseConnection()

#################################################################################
load_image      = face_recognition.load_image_file('./img/unknown/bill-gates-4.jpg')
#################################################################################
face_locations  = face_recognition.face_locations(load_image)
face_encoding   = face_recognition.face_encodings(load_image, face_locations)

mycursor = mydb.cursor()

mycursor.execute("SELECT image, name FROM face_recog")
rows = mycursor.fetchall()

## Get the results
for each in rows:
    face_data = pickle.loads(each[0])

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encoding):
        matches = face_recognition.compare_faces([face_encoding], face_data)

        if True in matches:
            print(f'Face matches with {each[1]}')
            break
            
        else:
            print('Face does not match')
            # name = input('Enter the name of person: ')
            # face_pickled_data = pickle.dumps(face_encoding)
            # mycursor = mydb.cursor()
            # sql = "INSERT INTO face_recog (image,name) VALUES (%s, %s)"
            # val = (face_pickled_data, name)
            # mycursor.execute(sql, val)
            # mydb.commit()
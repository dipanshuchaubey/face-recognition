import face_recognition
import requests
import json
import pickle
from auth import db

# load image
load_image = face_recognition.load_image_file('./img/known/Bill Gates.jpg')

# find face locations
face_locations = face_recognition.face_locations(load_image)

# find face encoding
face_encoding = face_recognition.face_encodings(load_image, face_locations)

# print(face_encoding)

# load image
load_image1 = face_recognition.load_image_file(
    './img/unknown/bill-gates-4.jpg')

# find face locations
face_locations1 = face_recognition.face_locations(load_image1)

# find face encoding
face_encoding1 = face_recognition.face_encodings(load_image1, face_locations1)


for (top, right, bottom, left), face_encoding in zip(face_locations, face_encoding):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(face_encoding, face_encoding1)

    # If a match was found in known_face_encodings, just use the first one.
    if True in matches:
        # print('Sahi khel gya BC')
        # face_pickled_data = pickle.dumps(face_encoding)

        mydb = db.databaseConnection()

        mycursor = mydb.cursor()

        # sql = "INSERT INTO face_recog (image,name) VALUES (%s, %s)"
        # val = (face_pickled_data, "name")
        # mycursor.execute(sql, val)

        # mydb.commit()

        mycursor.execute("SELECT image FROM face_recog WHERE name = 'name1'")
        rows = mycursor.fetchall()

        # Get the results
        for each in rows:
            # The result is also in a tuple
            for face_stored_pickled_data in each:
                face_data = pickle.loads(face_stored_pickled_data)
                print(face_data)

    else:
        print('Bhag BC')
# print(face_encoding1)

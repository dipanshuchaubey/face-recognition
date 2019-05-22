import face_recognition
from PIL import Image, ImageDraw

# fetch all face from the database


# Set data array
known_face_encodings = [
    face_encoding1,
    face_encoding2
]

known_face_names = [
    "User1",
    "User2"
]

# Load an image with an unknown face
unknown_image = face_recognition.load_image_file("./img/groups/bill-steve-elon.jpg")

# find face location
face_locations = face_recognition.face_locations(unknown_image)

# get face encodings
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Convert the image to a PIL-format image so that we can draw on top of it
pil_image = Image.fromarray(unknown_image)

# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown"

    # If a match was found in known_face_encodings, just use the first one.
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


del draw

pil_image.show()

# pil_image.save("image_with_boxes.jpg")
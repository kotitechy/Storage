import sqlite3
from PIL import Image
from io import BytesIO

db = sqlite3.connect('ellenki.db')
cr = db.cursor()

# Assuming you have a specific ID for the image you want to retrieve
# image_id = input('Enter the ID of the image you want to retrieve: ')

# Execute a SELECT query to retrieve the image data for the specified ID
cr.execute('SELECT profile FROM students WHERE id = 1')
result = cr.fetchone()

if result is not None:
    # Retrieve the binary image data from the query result
    image_binary = result[1]
    # print(result[0])

    # Create an image from the binary data using Pillow
    img = Image.open(BytesIO(image_binary))
    print(img)
    # Display the image
    img.show()
else:
    print('Image not found for the specified ID.')
db.close()

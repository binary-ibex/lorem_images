from flask import Flask, send_file
from PIL import Image
import io 
import random 
import re

app = Flask(__name__)

@app.route('/')
@app.route('/<int:width>')
@app.route('/<int:width>/<int:height>')
def index(width=0, height=0):

    expression = r'\b\d{1,4}\b'
    width = int(width)
    height = int(height)

    if not re.findall(expression , str(width)) and re.findall(expression , str(height)):
        return "Error in input"
    if width > 2000 or height > 2000:
        return "image dimension should not exced 2000px"
        
    if width == height==0:
        width = 100
        height = 100
    elif width == 0:
        width = height
    elif height == 0:
        height = width

    return get_image(width, height)


def get_correct_image(width, height):
    images = {
        'square':['square1.jpg', 'square2.jpg', 'square3.jpg', 'square4.jpg'],
        'portrait':['portrait1.jpg', 'portrait2.jpg', 'portrait3.jpg'],
        'landscape':['landscape1.jpg', 'landscape2.jpg', 'landscape3.jpg']
    }

    if width == height:
        return 'images/square/' + random.choice(images['square'])
    
    if width>height:
        return 'images/landscape/' + random.choice(images['landscape'])
    
    if width<height:
        return 'images/portrait/' + random.choice(images['portrait'])


def get_image(width, height):
    image  = Image.open(get_correct_image(width, height))
    new_image = image.resize((width, height))

    #temp memory buffer 
    image_mem = io.BytesIO()
    new_im = new_image.save(image_mem, 'JPEG')
    image_mem.seek(0,0)

    return send_file(image_mem,mimetype='image/gif', as_attachment=False)

if __name__=='__main__':
    app.run(port=8000, debug=True)
from flask import Flask, send_file
from PIL import Image
import io 

app = Flask(__name__)

@app.route('/')
@app.route('/<int:width>')
@app.route('/<int:width>/<int:height>')
def index(width=0, height=0):
    return get_image(width, height)

def get_image(width, height):
    image  = Image.open('images/image1.jpg')
    new_image = image.resize((width, height))

    #temp memory buffer 
    image_mem = io.BytesIO()
    new_im = new_image.save(image_mem, 'JPEG')
    image_mem.seek(0,0)

    return send_file(image_mem,mimetype='image/gif', as_attachment=False)

if __name__=='__main__':
    app.run(port=8000, debug=True)
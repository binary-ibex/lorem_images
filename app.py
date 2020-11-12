from flask import Flask 


app = Flask(__name__)

@app.route('/')
@app.route('/<int:width>')
@app.route('/<int:width>/<int:height>')
def index(width=0, height=0):
    return "width = {0} and height = {1}".format(width, height)



if __name__=='__main__':
    app.run(port=8000)
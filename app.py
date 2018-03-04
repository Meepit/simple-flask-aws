from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
import boto3
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket('playing-with-flask-aws')
    return render_template('index.html', my_bucket=my_bucket)


@app.route('/upload', methods=['POST'])
def upload_file():
    print(request.files)
    f = request.files['img']
    _upload_img(f)
    return redirect(url_for('index'))

def _upload_img(img):
    s3 = boto3.resource('s3')
    try:
        name = ''.join([random.choice(string.ascii_letters) for i in range(10)])
        print(name)
        s3.Bucket('playing-with-flask-aws').put_object(Key="{0}.png".format(name), Body=img, ContentType='image')
        print("File successfully uploaded")
    except:
        print("Something went wrong")

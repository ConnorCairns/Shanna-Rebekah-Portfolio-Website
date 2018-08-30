import boto3
import os
from PIL import Image
from flask import current_app, url_for

#S3 Stuff
client = boto3.Session(
    aws_access_key_id=os.environ.get('shanna_aws_access'),
    aws_secret_access_key=os.environ.get('shanna_aws_secret'),
)
s3 = client.resource('s3')

def s3_upload(name):
    path = "app/static/temp/" + name + ".JPG"
    image = open(path, 'rb')
    s3.Bucket('shanna-rebekah-photography').put_object(Key=f'{name}.JPG', ContentType='image/png',Body=image)
    #with open(picture, 'rb') as data:
    #    s3.upload_fileobj(data, 'shanna-rebekah-photography', name)


def save_pic(picture, name):
    fname = name + '.JPG'
    path = os.path.join(current_app.root_path, 'static', 'temp' , fname)
    image = Image.open(picture)
    image.save(path)
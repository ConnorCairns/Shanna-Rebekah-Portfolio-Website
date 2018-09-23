import boto3, os, time
from PIL import Image
from flask import current_app, url_for

#S3 Stuff
client = boto3.Session(
    aws_access_key_id=os.environ.get('shanna_aws_access'),
    aws_secret_access_key=os.environ.get('shanna_aws_secret'),
)
s3 = client.resource('s3')

def s3_upload(name):
    name = name.lower()
    path = f"app/static/temp/{name}.JPG"
    image = open(path, 'rb')
    s3.Bucket('shanna-rebekah-photography').put_object(Key=f'{name}.JPG', ContentType='image/png',Body=image)


def save_pic(picture, name):
    name = name.lower()
    fname = name + '.JPG'
    path = os.path.join(current_app.root_path, 'static', 'temp' , fname)
    image = Image.open(picture)
    image.save(path)

def del_pic(name):
    name = name.lower()
    path = f"app/static/temp/{name}.JPG"
    os.remove(path)

def s3_download(data):
    ndata = data+'.JPG'
    path = os.path.join(current_app.root_path, 'static', 'temp' , ndata)
    s3.Bucket('shanna-rebekah-photography').download_file(ndata, path)
    #s3_temp_delete(path)

#def s3_temp_delete(path):
#    time.sleep(5)
#    os.remove(path)
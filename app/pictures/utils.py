import boto3

#S3 Stuff
client = boto3.Session(
    aws_access_key_id='AKIAJYRUBLXBMAWUZFNA',
    aws_secret_access_key='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',
)
s3 = client.resource('s3')

def s3_upload(picture, name):
    image = open(picture, 'rb')
    s3.Bucket('shanna-rebekah-photography').put_object(Key=f'{name}.JPG', ContentType='image/png',Body=image)
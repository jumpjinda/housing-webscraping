def load_csv_to_s3(state):
    import boto3

    #Creating Session With Boto3.
    session = boto3.Session(
    aws_access_key_id='<your access key>',
    aws_secret_access_key='<your secret access key>'
    )

    #Creating S3 Resource From the Session.
    s3 = session.resource('s3')
    s3.create_bucket(Bucket="<your bucket name>")
    s3.Bucket('<your bucket name>').upload_file('housing-webscraping-to-postgress-mongodb-s3\output-csv\housing_' + state + '.csv', 'housing_' + state + '.csv')
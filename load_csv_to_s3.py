import boto3

#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='AKIATDWH7XUL2PHJ5OOM',
aws_secret_access_key='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'
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')

state_list = ['al', 'ak', 'ar', 'az', 'ca', 'co', 'ct', 'de', 'dc', 'fl', 'ga', 'hi', 'id', 'il', 'in_', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi' ,'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd' , 'oh', 'ok', 'or_', 'pa', 'ri', 'sc', 'sd', 'tn', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']

s3.create_bucket(Bucket="jumpjindahousing")


for state in state_list:
    s3.Bucket('jumpjindahousing').upload_file('housing-webscraping-to-postgress-mongodb\output-csv\housing_' + state + '.csv', 'housing_' + state + '.csv')
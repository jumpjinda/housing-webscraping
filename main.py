from scrape_zillow_to_csv_and_json import *
from load_csv_to_postgres import *
from load_json_to_mongodb import *
from load_csv_to_s3 import *

state_list = ['al', 'ak', 'ar', 'az', 'ca', 'co', 'ct', 'de', 'dc', 'fl', 'ga', 'hi', 'id', 'il', 'in_', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi' ,'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd' , 'oh', 'ok', 'or_', 'pa', 'ri', 'sc', 'sd', 'tn', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']

for state in state_list:
    zillow_housing_scrape(state, 21)
    
for state in state_list:
    load_csv_to_postgres('housing', state)
    
for state in state_list:
    load_json_to_mongodb(state)
    
for state in state_list:
    load_csv_to_s3(state)
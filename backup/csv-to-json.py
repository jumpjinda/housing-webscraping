import csv
import json

state_list = ['al', 'ak', 'ar', 'az', 'ca', 'co', 'ct', 'de', 'dc', 'fl', 'ga', 'hi', 'id', 'il', 'in_', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi' ,'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd' , 'oh', 'ok', 'or_', 'pa', 'ri', 'sc', 'sd', 'tn', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']
for state in state_list:
    dict_list = []

    with open('D:\Data_Engineer\project\housing-webscraping-to-postgress-mongodb\output-csv\housing_' + state + '.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dict_list.append({
                "price_usd": int(row[0]),
                "price_baht": int(row[1]),
                "bed": int(row[2]),
                "bath": int(row[3]),
                "sqft": int(row[4]),
                "sq_wah": float(row[5]),
                "house_type": row[6],
                "address": row[7],
                "link": row[8],
            })

    with open('D:\Data_Engineer\project\housing-webscraping-to-postgress-mongodb\output-json\housing_'+ state + '.json', 'w') as outfile:
        json.dump(dict_list, outfile, indent = 4) # indent เยื้อง
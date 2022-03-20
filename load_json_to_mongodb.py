def load_json_to_mongodb(state):

    from pymongo import MongoClient
    import json

    connection_string = 'mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false'

    client = MongoClient(connection_string)

    state_list = ['al', 'ak', 'ar', 'az', 'ca', 'co', 'ct', 'de', 'dc', 'fl', 'ga', 'hi', 'id', 'il', 'in_', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi' ,'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd' , 'oh', 'ok', 'or_', 'pa', 'ri', 'sc', 'sd', 'tn', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']

    for state in state_list:
        with open('housing-webscraping-to-postgress-mongodb\output-json\housing_' + state + '.json', 'r') as file:
            file_data = json.load(file)
            # print(file_data[0])
            client["housing"][state].insert_many(file_data)
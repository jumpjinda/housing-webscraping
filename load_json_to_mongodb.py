def load_json_to_mongodb(state):

    from pymongo import MongoClient
    import json

    connection_string = '<your connection>'

    client = MongoClient(connection_string)

    with open('housing-webscraping-to-postgress-mongodb-s3\output-json\housing_' + state + '.json', 'r') as file:
        file_data = json.load(file)
        # print(file_data[0])
        client["housing"][state].insert_many(file_data)

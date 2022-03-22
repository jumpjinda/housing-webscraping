import csv
import pandas as pd

state_list = ['al', 'ak', 'ar', 'az', 'ca', 'co', 'ct', 'de', 'dc', 'fl', 'ga', 'hi', 'id', 'il', 'in_', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi' ,'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd' , 'oh', 'ok', 'or_', 'pa', 'ri', 'sc', 'sd', 'tn', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']

for state in state_list:
    test = pd.read_csv('output-csv/housing_' + state + '.csv', header=None)
    test = pd.DataFrame(test)
    test.drop(test.columns[0], inplace=True, axis=1)
    test.to_csv('output-csv/housing_' + state + '.csv', header=None, index=False)
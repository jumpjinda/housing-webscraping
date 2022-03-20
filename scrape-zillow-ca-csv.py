from bs4 import BeautifulSoup as soup
import requests
import time
import csv
import pandas as pd
    
    
pages = []

for i in range(1, 21):
    pages.append(i)

bed = []
bath = []
sqft = []
address = []
price = []

for i in pages:
    PAUSE_SECONDS = 5

    url = 'https://www.zillow.com/ca/house,apartment_duplex,mobile,townhouse_type/' + \
        str(i) + '_p'
    print(url)

    req_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    time.sleep(PAUSE_SECONDS)

    with requests.Session() as s:
        response = s.get(url, headers=req_headers)

    data = soup(response.content, 'html.parser')

    bed_bath_sqft_raw = data.find_all('ul', {'class': 'list-card-details'})
    # print(bed_bath_sqft_raw[0].text)

    for i in bed_bath_sqft_raw:

        i = i.text.replace('bds', '|').replace('ba', '|').replace('sqft', '|').replace(',', '')\
            .replace('House for sale', '').replace('Condo for sale', '').replace('Townhouse for sale', '')\
            .replace('Home for sale', '').replace('New construction', '').replace('Coming soon', '')\
            .replace('Auction', '').replace('Studio', '').replace('Multi-family home for sale', '')\
            .replace('Foreclosure', '').replace('-', '').replace('\\"\\', '').replace(' ', '').replace('|', ',')\
            

        i = i[:-2]

        bd = i[0]
        bt = i[2]
        sq = i[4:]

        bed.append(bd)
        bath.append(bt)
        sqft.append(sq)

        # print(bed, '\n', bath, '\n', sqft)

        address_raw = data.find_all('address', {'class': 'list-card-addr'})


        for i in address_raw:

            i = i.text.replace(',', '').replace('#', '')
            address.append(str(i))

        # for i in address:
        #     print(i)

    price_raw = data.find_all('div', {'class': 'list-card-price'})


    for i in price_raw:

        i = i.text.replace('$', '').replace(',', '').replace(
            '+', '').replace('K', '000').replace('k', '000')
        price.append(int(i))

        # print(price)


with open("extract_files/california_houses_for_sale_raw.csv", "w", newline='') as f:
    writer = csv.writer(f)
    for i in range(len(bed)):
            content = [bed[int(i)], bath[int(i)], sqft[int(i)], price[int(i)], address[i]]
            writer.writerow(content)

file = pd.read_csv('extract_files\california_houses_for_sale_raw.csv')
# print(file)

file.columns = ['bed', 'bath', 'sqft', 'price', 'address']

file = file.query('bath != "d"')
file = file.query('sqft != "--"')
file = file.query('sqft != 0')
file = file.query('price < 1000000')
file = file.query('bed != "-"')
file = file.query('address != "1311 School St Folsom CA 95630"')

file.to_csv('transformed_files/california_houses_for_sale.csv', index=False, header=None)
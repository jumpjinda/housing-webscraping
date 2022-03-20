def zillow_housing_scrape(city='ca', page_range=2):
    from bs4 import BeautifulSoup as soup
    import requests
    import time
    import csv
        
    # Generate page number put into pages
    pages = []
    for i in range(1, page_range): # how many page range do you want?
        pages.append(i)

    prices = []
    beds = []
    baths = []
    sqfts = []
    house_types = []
    addresses = []
    links = []

    for i in pages:
        PAUSE_SECONDS = 5

        url = "https://www.zillow.com/" + city + "/house,apartment_duplex,mobile,townhouse_type/" + str(i) + "_p"
        print(url)

        req_headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.8",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        }

        time.sleep(PAUSE_SECONDS)

        with requests.Session() as s:
            response = s.get(url, headers=req_headers)

        data = soup(response.text, "html.parser")

        price_raw = data.select(".list-card-price")
        house_details = data.select(".list-card-details") # It's holded bed, bath, sqft, house_type
        address_raw = data.select(".list-card-addr")
        links_raw = data.select(".list-card-link")

        house_details_raw = [] # It's holded bed, bath, sqft, house_type
        for i in house_details:
        #     print(i)
            for item in i:
                item = item.text
        #         print(item)
                house_details_raw.append(item)
            
        # print(house_details_raw)

        bed_raw = house_details_raw[0::4]
        bath_raw = house_details_raw[1::4]
        sqft_raw = house_details_raw[2::4]
        house_type_raw = house_details_raw[3::4]


        for price in price_raw:
            price = int(price.get_text().replace("$", "").replace(",", "").replace("+", "")\
                            .replace("K", "000").replace("k", "000").replace("--", "0"))
            prices.append(price)

        for bed in bed_raw:
            bed = int(bed.replace("bds", "").replace("bd", "").replace("--", "0").replace("Studio", "0").replace(" ", ""))
            beds.append(bed)
            
        for bath in bath_raw:
            # some error from website, they put float number in bath, we use round to remove digit after dot and convert number to int
            bath = int(round(float(bath.replace("ba", "").replace("--", "0").replace(" ", ""))))
            baths.append(bath)
            
        for sqft in sqft_raw:
            sqft = int(sqft.replace(",", "").replace(" ", "").replace("sqft", "")\
                        .replace("--", "0"))
            sqfts.append(sqft)

        for house_type in house_type_raw:
            house_type = house_type[2:] # remove first 2 char (white space and -)
            house_types.append(house_type)
            
        for address in address_raw:
            address = address.text
            addresses.append(address)

        for index, item in enumerate(links_raw):
            item = str(item.get("href"))
            # print(item)
            if item != "None"and index % 2 != 0: # remove None and duplicate links
                links.append(item)

        # print("prices", len(prices), prices)
        # print("beds", len(beds),beds)
        # print("baths", len(baths), baths)
        # print("sqfts", len(sqfts), sqfts)
        # print("house_types", len(house_types), house_types)
        # print("addresses" ,len(addresses), addresses)
        # print("links", len(links), links)

    with open('D:/Data_Engineer/project/housing-webscraping-to-postgress-mongodb/output-csv/housing_' + city + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(0, len(prices)):
            price_baht = prices[i] * 33
            square_wah = sqfts[i] * 0.093 * 0.25 
            content = [prices[i], price_baht, beds[i], baths[i], sqfts[i], square_wah, house_types[i],\
                    addresses[i],links[i]]
            writer.writerow(content)
def sqft_to_square_wah(sqft):
    square_wah = (sqft * 0.093) * 0.25
    print(sqft, 'sqft =', square_wah, 'square_wah')
    return square_wah

sqft_to_square_wah(2730)
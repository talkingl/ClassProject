import time
import pandas as pd
import xlrd

states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
          'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
          'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
          'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
          'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']



df = pd.read_excel('tax_percent_calc.xls')
while True:

    file_open = open("prng-service.txt", "r")
    reader = file_open.readline()
    file_open.close()
    for i in range(0, len(df)):
        if df['ABBV'][i] == reader:
            writer = open("tax-service.txt", "w")
            new_data_state = f"{df['State'][i]}"
            new_data_tax = f"{df['Tax_percent'][i]}"
            writer.write(new_data_tax)
            # writer.write(df['State'][i], df['Tax-percent'])
            writer.close()
            writer2 = open("state-service.txt", "w")
            writer2.write(new_data_state)
            # writer.write(df['State'][i], df['Tax-percent'])
            writer2.close()
            time.sleep(1)

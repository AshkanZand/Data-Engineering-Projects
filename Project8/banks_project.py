# Code for ETL operations on Country-GDP data

import requests
import sqlite3
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from datetime import datetime

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open ('code_log.txt','a') as f:
        f.write(timestamp + ' : '+ message + '\n')


def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')
    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')
    df = pd.DataFrame(columns=table_attribs)  
    for row in rows:
        col = row.find_all('td')
        if len(col) !=0:
            data_dict = {'Name' : col[1].find_all('a')[1]['title'],
                        'MC_USD_Billion' : float(col[2].contents[0][:-1])}
            df1 =pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1],ignore_index=True)
    return df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''

    exchange_rate =pd.read_csv(csv_path)
    exchange_rate = exchange_rate.set_index('Currency').to_dict()['Rate']
    df['MC_GBP_Billion'] = round(df[['MC_USD_Billion']]*exchange_rate['GBP'],2)
    df['MC_EUR_Billion'] = round(df[['MC_USD_Billion']]*exchange_rate['EUR'],2)
    df['MC_INR_Billion'] = round(df[['MC_USD_Billion']]*exchange_rate['INR'],2)

    return df 

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)  

''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''

# Preliminaries
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attributes_final = ['Name', 'MC_USD_Billion', 'MC_GBP_Billion', 'MC_EUR_Billion', 'MC_INR_Billion']
table_attributes_extraction = ['Name', 'MC_USD_Billion']
csv_path = "Largest_banks_data.csv"
rate_csv = 'exchange_rate.csv'
db_name = "Banks.db"
table_name = "Largest_banks"

# Execution

log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url,table_attributes_extraction)
print(df)

log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df, rate_csv)
#print(df)
print("df['MC_EUR_Billion'][4] :", df['MC_EUR_Billion'][4],)

log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df, csv_path)

log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect(db_name)

log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, table_name)

log_progress('Data loaded to Database as table. Running the query')

query_statement = f"SELECT * FROM {table_name}"
run_query(query_statement, sql_connection)

query_statement = f"SELECT AVG(MC_GBP_Billion) FROM {table_name}"
run_query(query_statement, sql_connection)

query_statement = f"SELECT Name from  {table_name} LIMIT 5"
run_query(query_statement, sql_connection)

log_progress('Process Complete.')

sql_connection.close()

log_progress('Server Connection clsed.')
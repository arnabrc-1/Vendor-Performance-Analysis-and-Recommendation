import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level= logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s",
    filemode="a"
)


engine=create_engine('sqlite:///inventory.db')


def ingest_db(df, table_name, engine, replace=False):
    df.to_sql(
        table_name,
        con=engine,
        if_exists='replace' if replace else 'append',
        index=False,
        chunksize=10000
    )




def load_raw_data():
    """this function will load the CSVs as dataframe and ingest into db in chunks"""
    start = time.time()
    
    for file in os.listdir('data'):
        if file.endswith('.csv'):
            table_name = file[:-4]
            first = True
            
            logging.info(f'Ingesting {file} in db')
            
            # read and ingest in chunks
            for chunk in pd.read_csv('data/' + file, chunksize=50000):
                ingest_db(chunk, table_name, engine, replace=first)
                first = False

    end = time.time()
    total_time = (end - start) / 60
    logging.info('--------------Ingestion Complete------------')
    logging.info(f'\nTotal Time Taken: {total_time} minutes')

if __name__ == '__main__':
    load_raw_data()

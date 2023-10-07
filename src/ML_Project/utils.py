import os
import pickle
import sys
from src.ML_Project.logger import logging
from src.ML_Project.exception import CustomException
import pandas as pd
import pymysql
from dotenv import load_dotenv

load_dotenv()
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')

#reading data from mysql databases

def read_sql_data():
    logging.info('Reading sql database started')

    try:
        mydb = pymysql.connect(
            host = host,
            user = user,
            password = password,
            db = db


        )
        
        logging.info("connection established with" , mydb)
        df = pd.read_sql_query("select * from student" , mydb)
        print(df.head())
        

        return df




    except Exception as e:
        raise CustomException(e,sys)


def save_object(file_path ,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok = True)

        with open(file_path ,"wb") as file_obj:
            pickle.dump(obj ,file_obj)

        



    except Exception as e:
        raise CustomException(e,sys)

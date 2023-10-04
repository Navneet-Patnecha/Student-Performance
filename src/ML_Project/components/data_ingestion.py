## (MySQL) Database --> Data --> Train-test split
import os
import sys
from src.ML_Project.logger import logging
from src.ML_Project.exception import CustomException
from src.ML_Project.utils import read_sql_data
from sklearn.model_selection import train_test_split

from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts' , 'train_data.csv')
    test_data_path:str = os.path.join('artifacts' , 'test_data.csv')
    raw_data_path:str = os.path.join('artifacts' , 'raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:
            # reading code from mysql databases
            df = read_sql_data()
            logging.info("reading completed mysql databases")


            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            #os.makedirs(os.path.dirname(self.ingestion_config.test_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,header=True,index=False)
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,header=True,index=False)
            test_set.to_csv(self.ingestion_config.test_data_path,header=True,index=False)


            logging.info('data ingestion is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            




        except Exception as e:
            raise CustomException(e,sys)







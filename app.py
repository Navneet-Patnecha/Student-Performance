from src.ML_Project.logger import logging
from src.ML_Project.exception import CustomException
import sys
from src.ML_Project.components.data_ingestion import DataIngestion
from src.ML_Project.components.data_ingestion import DataIngestionConfig





if __name__=="__main__":
    logging.info("the execution has started")

    try:
        #data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
        
    
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
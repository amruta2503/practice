import logging
import os.path

from pandas import DataFrame
import pandas as pd
from pymongo.mongo_client import MongoClient
from source.logger import logging
from source.exception import ChurnException

class DataIngestion:

    def __init__(self,utility_config):
        self.utility_config = utility_config

    def export_data_into_feature_store(self) -> DataFrame:
        try:
            logging.info("Start:Data load from mongodb")

            client = MongoClient(self.utility_config.mongodb_url_key)
            database = client[self.utility_config.database_name]
            collection = database[self.utility_config.collection_name]

            cursor = collection.find()

            data = pd.DataFrame(list(cursor))

            dir_path = os.path.dirname(self.utility_config.feature_store_dir)
            os.makedirs(dir_path,exist_ok=True)
            data.to_csv(self.utility_config.feature_store_dir,index=False)

            logging.info("complete:Data load from mongodb")

            return data
        except ChurnException as e:
            logging.error(e)
            raise e
    def split_data_train_test(self):
        pass

    def initiate_data_ingestion(self):
        self.export_data_into_feature_store()
        self.split_data_train_test()
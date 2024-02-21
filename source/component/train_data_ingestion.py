import logging
import os.path
from sklearn.model_selection import train_test_split
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
    def split_data_train_test(self,data:DataFrame)->None:
        try:
            logging.info("start:split data train test")

            train_set,test_set = train_test_split(data,test_size=self.utility_config.train_test_split_ratio,random_state=45)

            dir_name = os.path.dirname(self.utility_config.train_file_name)
            os.makedirs(dir_name,exist_ok=True)

            test_set.to_csv(self.utility_config.train_file_name,index=False)

            train_set.to_csv(self.utility_config.test_file_name,index=False)

            logging.info("complete:split data train test")

        except ChurnException as e:
            raise e

    def clean_data(self,data):
        try:
            logging.info("start:data clean")

            data = data.drop_duplicates()

            drop_column = []

            data = data.loc[:,data.nunique()>1]

            for col in data.select_dtypes(include="object").columns:
                unique_count = data[col].nunique()

                if unique_count/len(data)>0.5:
                    data.drop(col,axis=1,inplace=True)
                    drop_column.append(col)

            logging.info("complete:data clean")
            return data
        except ChurnException as e:
            raise e

    def initiate_data_ingestion(self):
        data=self.export_data_into_feature_store()
        data=self.clean_data(data)
        self.split_data_train_test(data)
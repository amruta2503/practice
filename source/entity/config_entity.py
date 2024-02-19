import os
from source.constant import constant_train
from datetime import datetime
class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.target_column = constant_train.TARGET_COLUMN
        self.train_pipeline_name = constant_train.TRAIN_PIPELINE_NAME
        self.artifact_dir = os.path.join(constant_train.ARTIFACT_DIR,timestamp)
        self.di_dir = os.path.join(self.artifact_dir,constant_train.DI_DIR)
        self.feature_store_dir = os.path.join(self.di_dir,constant_train.DI_FEATURE_STORE_DIR,constant_train.FILE_NAME)
        self.train_file_name = os.path.join(self.di_dir,constant_train.DI_INGESTED_DIR,constant_train.TRAIN_FILE_NAME)
        self.test_file_name = os.path.join(self.di_dir, constant_train.DI_INGESTED_DIR, constant_train.TEST_FILE_NAME)
        self.mongodb_url_key = constant_train.MONGODB_URL_KEY
        self.database_name = constant_train.DATABASE_NAME
        self.collection_name = constant_train.DI_COLLECTION_NAME
        self.train_test_split_ratio = constant_train.DI_TRAIN_TEST_SPLIT_RATIO



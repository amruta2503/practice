from source.component.train_data_ingestion import DataIngestion
from source.entity.config_entity import TrainingPipelineConfig

class TrainPipeline:

    def __init__(self,global_timestamp):
        self.utility_config = TrainingPipelineConfig(global_timestamp)

    def start_dataingestion(self):
        dataingestion_obj = DataIngestion(self.utility_config)
        dataingestion_obj.initiate_data_ingestion()

    def run_train_pipeline(self):
        self.start_dataingestion()


import logging
from source.pipeline.train_pipeline import TrainPipeline
from source.entity.config_entity import TrainingPipelineConfig
from source.utility.utility import generate_global_timestamp
from source.logger import setup_logger

if __name__ == '__main__':

  global_timestamp = generate_global_timestamp()

  setup_logger(global_timestamp)

  logging.info("logger timetstamp setup complete")

  #train_pipeline_config = TrainingPipelineConfig(global_timestamp)
  #print(train_pipeline_config.__dict__)

  logging.info("train pipeline config created")

  train_pipeline_obj = TrainPipeline(global_timestamp)
  train_pipeline_obj.run_train_pipeline()


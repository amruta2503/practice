from source.entity.config_entity import TrainingPipelineConfig


if __name__ == '__main__':
  train_pipeline_obj = TrainingPipelineConfig()
  print(train_pipeline_obj.__dict__)
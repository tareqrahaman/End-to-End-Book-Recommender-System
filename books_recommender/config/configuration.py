import os
import sys
from books_recommender.logger.log import logging
from books_recommender.exception.exception_handler import AppException
from books_recommender.entity.config_entity import DataIngestionConfig
from books_recommender.constant import CONFIG_FILE_PATH
from books_recommender.utils.util import read_yaml_file

class APPConfiguration:
  def __init__(self, config_file_path:str = CONFIG_FILE_PATH):
    try:
      self.configs_info = read_yaml_file(config_file_path) # read_yaml_file returning configbox
    except Exception as e:
      raise AppException(e, sys) from e
  
  def get_data_ingestion_config(self) -> DataIngestionConfig:
    try:
      artifacts_dir = self.configs_info.artifacts_config.artifacts_dir
      data_ingestion_config = self.configs_info.data_ingestion_config
      dataset_dir = data_ingestion_config.dataset_dir
      dataset_download_url = data_ingestion_config.dataset_download_url

      ingested_data_dir = os.path.join(artifacts_dir,dataset_dir,data_ingestion_config.ingested_data_dir)
      raw_data_dir = os.path.join(artifacts_dir,dataset_dir,data_ingestion_config.raw_data_dir)

      response = DataIngestionConfig(
        dataset_download_url = dataset_download_url,
        ingested_data_dir = ingested_data_dir,
        raw_data_dir = raw_data_dir
      )

      logging.info(f"Data Ingestion Config: {response}")
      return response

    except Exception as e:
      raise AppException(e, sys) from e
    
      
import os
import sys
import pickle
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from books_recommender.logger.log import logging
from books_recommender.config.configuration import APPConfiguration
from books_recommender.exception.exception_handler import AppException


class ModelTraining():
  def __init__(self, app_config = APPConfiguration()):
    self.model_trainer_config = app_config.get_model_trainer_config()

  def training(self):
    try:
      book_pivot = pickle.load(open(self.model_trainer_config.transformed_data_file_dir, 'rb'))
      book_sparse = csr_matrix(book_pivot)
      model = NearestNeighbors(algorithm= 'brute')
      model.fit(book_sparse)

      #saving model object for recommendation
      os.makedirs(self.model_trainer_config.trained_model_dir, exist_ok=True)
      file_name = os.path.join(self.model_trainer_config.trained_model_dir,self.model_trainer_config.trained_model_name)
      pickle.dump(model,open(file_name,"wb"))
      logging.info(f"saving file model to {file_name}")

    except Exception as e:
      raise AppException(e, sys) from e
    
    
  def initiate_model_training(self):
    try:
      logging.info(f"{'='*20} Model Training log Started. {'='*20}")
      self.training()
      logging.info(f"{'='*20} Model Training log Finished. {'='*20} \n\n")

    except Exception as e:
      raise AppException(e, sys) from e


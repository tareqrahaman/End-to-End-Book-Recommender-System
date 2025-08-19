from books_recommender.logger.log import logging
from books_recommender.exception.exception_handler import AppException
import sys

#logging.info("Book System")

try:
  4/0
except Exception as e:
  logging.info(e)  # Default Exception
  raise AppException(e, sys) from e # Custom Excepiton
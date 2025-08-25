import yaml
import sys
from books_recommender.exception.exception_handler import AppException
from box import ConfigBox

def read_yaml_file(file_path: str) -> ConfigBox:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except Exception as e:
        raise AppException(e, sys) from e


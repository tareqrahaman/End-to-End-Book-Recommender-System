from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig", ['dataset_download_url',
                                                   'ingested_data_dir',
                                                   'raw_data_dir'])

DataValidationConfig = namedtuple("DataValidationConfig", ["clean_data_dir",
                                                          "books_csv_file", 
                                                          "ratings_csv_file",
                                                          "serialized_obj_dir"])

DataTransformationConfig = namedtuple("DataTransformationConfig", ["clean_data_path",
                                                                   "transformed_data_dir"])

ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["transformed_data_file_dir",
                                                      "trained_model_dir",
                                                      "trained_model_name"])


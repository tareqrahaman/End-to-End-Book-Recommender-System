from collections import namedtuple

DataIngestionConfig = namedtuple("DatasetConfig", ['dataset_download_url',
                                                   'ingested_data_dir',
                                                   'raw_data_dir'])


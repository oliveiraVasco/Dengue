import numpy as np
import ast
class DataManagement:
    '''
    Class to manage and collect data from csv files.
    '''
    # First index of the second city on train data
    TRAIN_CITY_INDEX = 936

    # First index of the second city on test data
    TEST_CITY_INDEX = 260

    def __init__(self):
        '''
        Constructor reads data from files
        self.train_data: features for training
        self.test_data: features for testing
        self.label_data: labels for training data
        self.info_train_data: cities, weeks years and dates from training data
        self.info_test_data: cities, weeks years and dates from testing data
        self.features_names: names of features
        '''
        # Loading features
        self.train_data = np.genfromtxt(open("data/dengue_features_train.csv"),
                                        delimiter=',',
                                        dtype='float',
                                        skip_header=1)

        self.test_data = np.genfromtxt(open("data/dengue_features_test.csv"),
                                 delimiter=',',
                                 dtype='float',
                                 skip_header=1)
        # Loading labels
        self.label_data = np.genfromtxt(open("data/dengue_labels_train.csv"),
                                  delimiter=',',
                                  dtype='float',
                                  skip_header=1)
        # Loading test and train info (dates, years, weeks and cities)
        with open('data/dtype_info.csv', 'r') as f:
            reading_info_type = ast.literal_eval(f.read())

        self.info_train_data = np.genfromtxt(open("data/info_train.csv"),
                                      delimiter=',',
                                      dtype=reading_info_type,
                                      skip_header=1)

        self.info_test_data = np.genfromtxt(open("data/info_test.csv"),
                                     delimiter=',',
                                     dtype=reading_info_type,
                                     skip_header=1)

        # Read features names
        with open('data/dengue_features_train.csv', 'r') as f:
            str_names = f.readline()

        str_names = str_names.rstrip('\n')

        self.features_names = str_names.split(',')

    def get_city(self, city, train):
        '''
        Get train/test data by city

        :param city: sj (san juan) or iq (iquitos)
        :param train: True to return train_data, False to return test data
        :return: segmented ndarray
        '''
        if train == True:
            if city == 'sj':
                return self.train_data[0:self.TRAIN_CITY_INDEX, :]
            elif city == 'iq':
                return self.train_data[self.TRAIN_CITY_INDEX:, :]
        else:
            if city == 'sj':
                return self.test_data[0:self.TEST_CITY_INDEX, :]
            elif city == 'iq':
                return self.test_data[self.TEST_CITY_INDEX:, :]




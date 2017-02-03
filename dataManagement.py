import numpy as np
import ast

class DataObject:
    '''
    Class to manage collect data from files
    '''

    def __init__(self, train_bool):
        '''
        Constructor reads data from files
        :param train_bool: collects training data if true or testing data if false

        self.data: features
        self.labels: labels for training data
        self.info_data: cities, weeks years and dates
        self.features_names: names of features
        self.city_index: first index of the second city
        '''
        if train_bool == True:
            file = "train"
            # Loading labels ( only available if train_bool is true)
            self.labels = np.genfromtxt(open("data/dengue_labels_train.csv"),
                                            delimiter=',',
                                            dtype='float',
                                            skip_header=1)
        else:
            file = "test"
            self.labels = None

        # Loading features
        self.data = np.genfromtxt(open("data/dengue_features_" + file + ".csv"),
                                        delimiter=',',
                                        dtype='float',
                                        skip_header=1)

        with open('data/dtype_info.csv', 'r') as f:
            reading_info_type = ast.literal_eval(f.read())

        self.info_data = np.genfromtxt(open("data/info_" + file + ".csv"),
                                      delimiter=',',
                                      dtype=reading_info_type,
                                      skip_header=1)

        # Read features names
        with open("data/dengue_features_" + file + ".csv", 'r') as f:
            str_names = f.readline()

        str_names = str_names.rstrip('\n')

        self.features_names = str_names.split(',')

        for i in range(1, self.info_data.shape[0]):
            if self.info_data[i][0] != self.info_data[i-1][0]:
                self.city_index = i
                break

    def get_city(self, city):
        '''
        Get data by city

        :param city: sj (san juan) or iq (iquitos)
        :return: segmented ndarray
        '''
        if city == 'sj':
            return self.data[0:self.city_index, :]
        elif city == 'iq':
            return self.data[self.city_index:, :]
        else:
            print "City not available."
            return None

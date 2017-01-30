from matplotlib import pyplot as plt


class Plotting:
    '''
    Performs multiple and single plots
    '''
    def __init__(self, label, features, features_names):
        '''
        Constructor receives label data, features and names

        :param label: numpy.ndarray with label values
        :param features: numpy.ndarray with all features
        :param features_names: list with all names
        '''
        self.label = label
        self.features = features
        self.features_names = features_names

    def simple_plot(self, index, name, display):
        '''
        Plots a single feature (x axis)
        Labels on y axis

        :param index: integer, index of the feature
        :param name: name to be written on xlabel
        :param display: if true shows the plot, if false saves the image
        :return:
        '''
        plot_feature = self.features[:, index]
        plt.xlabel(name)
        plt.ylabel("Dengue cases")
        plt.plot(plot_feature, self.label, 'ro')
        if display == True:
            plt.show()
        else:
            plt.savefig('images/cases_'+name+'.png')
            plt.close()

    def multiple_plot(self, display):
        '''
        Plots all features

        :param display: if true shows the plot, if false saves the image
        :return:
        '''
        for i in range(self.features.shape[1]):
            self.simple_plot(i, self.features_names[i], display)


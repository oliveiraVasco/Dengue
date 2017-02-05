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

    def simple_plot(self, index_y, index_x, display, lag):
        '''
        Plots two series with index on input

        :param index_y: -1 for self.label, other for the respetive index
        :param index_x: index of x axis series
        :param name_x: name to show on x label
        :param name_y: name to show on y label
        :param display: if true shows the plot, if false saves the image
        :param lag: lags from x to y
        :return:
        '''

        if index_y == -1:
            plot_y = self.label
            name_y = "Dengue_Cases"
        elif index_y in range(self.features.shape[1]):
            plot_y = self.features[:, index_y]
            name_y = self.features_names[index_y]
        else:
            print "Index y out of range."
            return

        plot_x = self.features[:, index_x]
        name_x = self.features_names[index_x]

        if lag > 0:
            plot_y = plot_y[lag:, :]
            plot_x = plot_x[:lag, :]


        plt.xlabel(name_x)
        plt.ylabel(name_y)
        plt.plot(plot_x, plot_y, 'ro')
        if display == True:
            plt.show()
        else:
            plt.savefig('images/' + name_y + '_' + name_x + '.png')
            plt.close()

    def multiple_plot(self, display):
        '''
        Plots all features

        :param display: if true shows the plot, if false saves the image
        :return:
        '''
        for i in range(self.features.shape[1]):
            self.simple_plot(-1, i, display, 0)


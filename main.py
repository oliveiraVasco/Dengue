import preAnalysis as pa
from dataManagement import DataManagement


def main():
    # Data collection
    data_object = DataManagement()

    # Plot object definition
    plot_object = pa.Plotting(data_object.label_data,
                          data_object.train_data,
                          data_object.features_names)

    # Multiple plot draw
    plot_object.multiple_plot(False)


if __name__=="__main__":
    main()
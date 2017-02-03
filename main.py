import preAnalysis as pa
from dataManagement import DataObject


def main():
    # Data collection
    train_object = DataObject(True)
    test_object = DataObject(False)

    # Plot object definition
    plot_object = pa.Plotting(train_object.labels,
                              train_object.data,
                              train_object.features_names)

    # Multiple plot draw
    plot_object.multiple_plot(True)


if __name__=="__main__":
    main()
import pandas as pd
import matplotlib.pyplot as plt
def summary_feature(data, feat):
    '''
    Function used for determining how many non-zero values exist on a feature of the data set, the unique values in that
    column and a summary of its datatypes, null and memory usage of a feature per each scenario. Arguments:
    - data = dataset from pickle file to analyze 
    - feat = feature to analyze (column)
    '''
    import pandas as pd
    print("There are {} non-zero values out of {} in '{}'".format((data[feat] != 0).sum(), len(data[feat]), feat))
    print("Number of unique values: {}".format(data[feat].nunique())) #change for data[feature].nunique()
    print("Unique Values: {}".format(data[feat].unique()))
    print("")
    return data[feat].info()


def check_hyphen(data, feat):
    '''
    Function used for determining how many '-' values exist on a feature of the data set. Arguments:
    - data = dataset from pickle file to analyze 
    - feat = feature to analyze (column)
    '''
    print("")
    print("There are {} '-' values out of {} in '{}'".format((data[feat] == '-').sum(), len(data[feat]), feat))
    
def plot_hist(feat, gl1, gl2, unit_dict, bins):
    '''
    Function to plot histograms based on label and label2 distributions
    '''
    import matplotlib.pyplot as plt
    #Plotting label histogram with legends (0: Bening, 1: Malicious)
    fig, ax = plt.subplots(1,2, figsize=(18,8))
    gl1[feat].hist(bins=bins, alpha=0.4, legend='label', ax=ax[0])
    ax[0].set_title("Network Flows (0, 1), Feature: '{}'".format(feat), fontsize=15)
    ax[0].set_xlabel(unit_dict[feat], fontsize=12)
    ax[0].set_ylabel('Counts', fontsize=12)
    #Plotting label2 histogram with legends (0 - 8 Types of Bots)
    gl2[feat].hist(bins=bins, alpha=0.4, legend='label2', ax=ax[1])
    ax[1].set_title("Bot Types (0 - 8), Feature: '{}'".format(feat), fontsize=15)
    ax[1].set_xlabel(unit_dict[feat], fontsize=12)
    ax[1].set_ylabel('Counts', fontsize=12)
    plt.show()
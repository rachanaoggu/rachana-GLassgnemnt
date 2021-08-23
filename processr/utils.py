import os
import pickle
from sklearn.naive_bayes import GaussianNB

# define the class encodings and reverse encodings
classes = {0: "class_0", 1: "class_1", 2: "class_2"}
r_classes = {y: x for x, y in classes.items()}

# function to process data and return it in correct format
def process_data(data):
    processed = [
        {
            "Alcohol": d.Alcohol,
            "Malic_acid": d.Malic_acid,
            "Ash": d.Ash,
            "Alcalinity_of_ash": d.Alcalinity_of_ash,
            "Magnesium": d.Magnesium,
            "Total_phenols": d.Total_phenols,
            "Flavanoids": d.Flavanoids,
            "Nonflavanoid_phenols": d.Nonflavanoid_phenols,
            "Proanthocyanins": d.Proanthocyanins,
            "Color_intensity": d.Color_intensity,
            "Hue": d.Hue,
            "OD280_OD315_of_diluted_wines": d.OD280_OD315_of_diluted_wines,
            "Proline": d.Proline,
            "Alcohol_class": d.Alcohol_class,
        }
        for d in data
    ]

    return processed

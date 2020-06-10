#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load((open("../final_project/final_project_dataset_unix.pkl", "rb")),fix_imports=True)
keys_list = list(enron_data)
values = enron_data.values()
values_list = list(values)

import numpy as np
ct2 = 0
for val in range(len(values_list)):
    if values_list[val]["email_address"] == 'NaN' :
        ct2 += 1
import csv
import pandas as pd
import numpy as np



def write_to_csv(time,age, bloodPressure, sugar, pusCell, pusCellClumps, sodium, hemoglobin,hypertension,diabetesMelitus,result):

    with open('dataset/records.csv', 'r') as f:
        reader = csv.reader(f)
        for header in reader:
            break
    with open('dataset/records.csv', "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        dict = {'time':time,'age':age,'bloodPressure':bloodPressure,'sugar':sugar,'pusCell':pusCell,
                'pusCellClumps':pusCellClumps,'sodium':sodium,'hemoglobin':hemoglobin,'hypertension':hypertension,
                'diabetesMelitus':diabetesMelitus,'result':result}
        writer.writerow(dict)
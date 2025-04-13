import csv
import os



def load_csv(filename="iris.csv"):
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, '..', 'data', filename)
    data = []

    with open(filepath, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            
        col_names = [col.strip().strip('"') for col in next(reader)]

        next(reader, None)

        for line in reader:
            cleaned_line = [item.strip().strip('"') for item in line]
            cleaned_line = [float(cleaned_line[0]),
                            float(cleaned_line[1]),
                            float(cleaned_line[2]), 
                            float(cleaned_line[3]), 
                            cleaned_line[4]
                            ]
            data.append(cleaned_line)

    return data, col_names
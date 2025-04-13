import csv

def save_csv(filename, data):
    with open(filename, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # for row in data:
        writer.writerows(data)

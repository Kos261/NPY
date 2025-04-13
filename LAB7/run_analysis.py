from iris_analysis.io.load import load_csv
from iris_analysis.io.save import save_csv
from iris_analysis.calculate import make_columns, std, mean, median
import argparse
'''
File iris_analysis/io/load.py should contain functions needed to load and parse data/iris.csv. File iris_analysis/io/save.py should contain functions needed to save result to .csv file. File iris_analysis/calculate.py should contain functions needed for statistic calculation. File run_analysis.py should be script which import proper functions from iris_analysis package and call them to calculate statistics. Each task should be performed using code from module with proper semantic name. Script should have two arguments: path to ada file and path to result file.

Example run:

$ python run_analysis.py data/iris.csv result.csv
'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help="Takes csv filename from data directory")
    parser.add_argument('to_write_name', help="Takes name for output file ")
    args = parser.parse_args()

    data, col_names = load_csv(args.filename)

    # print(col_names)
    for i in range(5):
        print(data[i])

    print("\t\t.\n\t\t.\n\t\t.")
        
    #I know I know, we can load data as columns directly but this is just transposition. 
    # We can need data in both shapes

    columns = make_columns(data)
    rows_to_write = [["Mean", "Standard deviation", "Median", "Columns"]]

    for i, col in enumerate(columns):
        avg = mean(col)
        standard_deviation = std(col)
        med = median(col)
        rows_to_write.append([avg, standard_deviation, med, col_names[i]])

    save_csv(args.to_write_name, rows_to_write)
def make_columns(data):
    col0, col1, col2, col3 = [],[],[],[]
    for row in data:
        col0.append(row[0])
        col1.append(row[1])
        col2.append(row[2])
        col3.append(row[3])

    return col0, col1, col2, col3


def mean(column):
    sum_col = sum(column)
    return sum_col/len(column)

def median(column):
    n = len(column)
    if n % 2 == 0:
        ans = (column[n/2] + column[n/2 - 1])/2
    else:
        ans = column[n//2]
    return ans

def std(column):
    mn = mean(column)
    errs = 0
    for item in column:
        errs += item - mn

    return errs
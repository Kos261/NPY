def print_info(val: int):
    if val < 0:
        print("Value need to beat least 0, not, val, file=sys.stderr")
    if val % 2 == 0:
        print(f"Value {val} is even")
    else:
        print(f"Value {val} is odd")

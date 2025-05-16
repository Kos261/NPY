import argparse
from alco_analysis.stats import summary

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="This is package for alcohol concesion data analysis in Poland")
    parser.add_argument("--summary", help="Show short summary of data (mean, median etc.)")
    parser.add_argument("--filein", help="Provide data file path")

    args = parser.parse_args()
    if args.summary:
        summary(args.filein)

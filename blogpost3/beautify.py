import click
from tabulate import tabulate
import csv


@click.command()
@click.option("-f", "--file", default=None, help="Name csv file to beautify.")
def beautify(file):
    # Initialize data
    column_names = []
    rows = []

    # Read the csv file
    with open(file, "rt") as data:
        data_reader = csv.reader(data)

        # Get the column names
        column_names = next(data_reader)

        # Extract the rows
        for row in data_reader:
            rows.append(row)

    # Time to print the data
    print(tabulate(rows, headers=column_names))


if __name__ == '__main__':
    beautify()

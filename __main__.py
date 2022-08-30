import argparse
from dataclasses import replace
from posixpath import basename
import sys
from io import open
import csv
from os import path

__version__ = 1.0

class Recipe:

    def __init__(self) -> None:
        pass

    @staticmethod
    def _modify(path: str, output_path: str):

        try:

            with open(path, "r", encoding="utf-8-sig") as processfile:
                new_recipe = []
                
                series = csv.reader(processfile, delimiter=";")
                header = next(series)
                
                index_begin = header.index('время, с')
                index_end = index_begin + 1

                header.insert(index_end, 'время в конце, с')
                header[index_begin] = 'время в начале, с'
                
                new_recipe.append(header)
                
                for row in series:
                    row.insert(index_end,row[index_begin])
                    new_recipe.append(row)
                    
            with open(output_path + basename(path), "w", encoding="utf-8-sig", newline='') as new_recipe_file:
                            writer = csv.writer(new_recipe_file, delimiter=";")
                            writer.writerows(new_recipe)
                            print("Wrote file: " + output_path + basename(path))
        
        except ValueError:
            print("Unable to find matching columns")


def main(self) -> None:

    parser = argparse.ArgumentParser(usage="%(prog)s [options]", description='This is a tool to modify recipe from\
     etching machine ICP200E')

    parser.add_argument(
        "path", metavar='/path/to/your.file', type=str, nargs='+',
        help="input path to '.csv' files to extract data to work with"
    )
    parser.add_argument(
        "--output", "-o",
        action="store",
        help="custom output path to save results, if not provided input file dir is used by default"
    )
    parser.add_argument(
        "--version", "-v",
        action="version",
        version='%(prog)s ' + str(__version__)
    )

    output_path = ""

    args = parser.parse_args()
    input_file = args.path

    if args.output:
        output_path = args.output 

    if not args.output:
        process = Recipe()
        for eachfile in input_file:
            process._modify(eachfile, output_path)

    elif path.isdir(str(output_path)):
        process = Recipe()
        for eachfile in input_file:
            process._modify(eachfile, output_path)

    else:
        print("Given output path: " + str(output_path) + " does not exist")

if __name__ == '__main__':
    main(sys.argv)

#!/bin/python3

#Script to convert csv sequences to fasta
#save your file in csv format
#The run the script
#Change column names to the suitable file column names in your csv file
# Copyright (C) 2020  Mike J. Mwanga <mikemwanga6@gmail.com>

import sys
import csv

if len(sys.argv)!=3:
    print("USAGE ERROR:csv_to_fasta.py input_file outputfile")
    sys.exit()

inputfile=sys.argv[1]
outputfile=sys.argv[2]


with open(inputfile, 'r') as infile:
    with open(outputfile, 'w') as outfile:
        read_file = csv.DictReader(infile, delimiter=',')
        for line in read_file:
            sequence = '>'+line['column_name1'] +'\n'+line['sequence_column_name']+'\n'
            outfile.write(sequence)


print('STOP using microsoft word to edit/analyse/visualize sequences/data. Just stop!')
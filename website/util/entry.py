#!/usr/bin/env python
"""Entry of open reading frame searching tool
Use -v or --version to get the version, -h or --help for help.
"""
import sys
from optparse import OptionParser
import orf_tool

usage = """Use as follows:
$ python entry.py -i input_seq_file -l length_of_designated_match
"""
parser = OptionParser(usage=usage)
parser.add_option('-i', '--input', dest='input',
                  default=None, help='Input sequences filename',
                  metavar="FILE")
parser.add_option("-l", "--length", dest="length",
                  default=100,
                  help="Set the length of designated match, length is the percentage of the longest match")
parser.add_option("-f", "--format", dest="format",
                  default="fasta",
                  help="Set the format of input file")
parser.add_option("-v", "--version", dest="version",
                  default=False, action="store_true",
                  help="Show version and quit")

options, args = parser.parse_args()

print(options)

if options.version:
    print("v0.1.0")
    sys.exit(0)

else:
    orf_tool.exec_tool(options)



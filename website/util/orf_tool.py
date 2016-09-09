"""Actual function class of open reading frame searching tool
   Served as a bridge between util class and entry.
"""
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import ORFFinder
import os
import GTranslator


def exec_tool(options):
    if options.format and options.format == "fasta":
        exec_fasta(options.input, options.length)
    elif options.format and options.format == "fastq":
        print("Process Fastq File(TODO:Not Implemented)")
    elif options.format and options.format == "sam":
        print("Process Sam File(TODO:Not Implemented)")
    elif options.format and options.format == "bam":
        print("Process Bam File(TODO:Not Implemented)")


# TODO: Seq and Rev_seq need to be process in the same time
def exec_fasta(in_file, length):

    input_file = open(in_file, "rU")
    all_mth_file = open(os.path.splitext(in_file)[0] + "_all_matches.fasta", "w+")
    desi_file = open(os.path.splitext(in_file)[0] + "_designated_matches.fasta", "w+")

    for record in SeqIO.parse(input_file, "fasta"):

        seq = record.seq
        result = ORFFinder.get_all_orf(str(seq), False)
        pairs = ORFFinder.find_all_orf(result)
        rev_seq = seq[::-1]
        rev_result = ORFFinder.get_all_orf(str(rev_seq), True)
        rev_pairs = ORFFinder.find_all_orf(rev_result)

        longest_match = ORFFinder.get_longest_pair(pairs, rev_pairs)

        match_length = int(longest_match * int(length) / 100)

        all_frags = []
        desi_frags = []

        for pair in pairs[:-1]:
            frag = SeqRecord(GTranslator.nucleotide_to_polypeptide(record.seq[pair[0]:pair[1]], False), record.id + "|" + str(pair[0]) + "-" + str(pair[1]),
                             '', '')
            all_frags.append(frag)

        for pair2 in rev_pairs[:-1]:
            frag = SeqRecord(GTranslator.nucleotide_to_polypeptide(rev_seq[pair2[0]:pair2[1]], True),
                             record.id + "|" + str(len(rev_seq) - pair2[0]) + "-" + str(len(rev_seq) - pair2[1]),
                             '', '')
            all_frags.append(frag)

        desi_pairs = []
        rev_desi_pairs = []

        desi_pairs = ORFFinder.get_desi_pairs(pairs, match_length)
        rev_desi_pairs = ORFFinder.get_desi_pairs(rev_pairs, match_length)

        for pair in desi_pairs:
            frag = SeqRecord(GTranslator.nucleotide_to_polypeptide(seq[pair[0]:pair[1]], False),
                             record.id + "|" + str(pair[0]) + "-" + str(pair[1]), '', '')
            desi_frags.append(frag)

        for pair in rev_desi_pairs:
            frag = SeqRecord(GTranslator.nucleotide_to_polypeptide(rev_seq[pair[0]:pair[1]], True),
                             record.id + "|" + str(len(rev_seq) - pair[0]) + "-" + str(len(rev_seq) - pair[1]),
                             '', '')
            desi_frags.append(frag)

        SeqIO.write(all_frags, all_mth_file, "fasta")
        SeqIO.write(desi_frags, desi_file, "fasta")

    input_file.close()
    all_mth_file.close()
    desi_file.close()

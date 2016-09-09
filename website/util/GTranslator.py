from Bio.Alphabet import generic_protein
from Bio.Seq import Seq


def condon_table():
    c_table = dict()

    c_table["TTT"] = "F"
    c_table["TTC"] = "F"
    c_table["TTA"] = "L"
    c_table["TTG"] = "L"
    c_table["CTT"] = "L"
    c_table["CTC"] = "L"
    c_table["CTA"] = "L"
    c_table["CTG"] = "L"
    c_table["ATT"] = "I"
    c_table["ATC"] = "I"
    c_table["ATA"] = "I"
    c_table["ATG"] = "M"
    c_table["GTT"] = "V"
    c_table["GTC"] = "V"
    c_table["GTA"] = "V"
    c_table["GTG"] = "V"
    c_table["TCT"] = "S"
    c_table["TCA"] = "S"
    c_table["TCC"] = "S"
    c_table["TCG"] = "S"
    c_table["CCT"] = "P"
    c_table["CCC"] = "P"
    c_table["CCA"] = "P"
    c_table["CCG"] = "P"
    c_table["ACT"] = "T"
    c_table["ACC"] = "T"
    c_table["ACA"] = "T"
    c_table["ACG"] = "T"
    c_table["GCT"] = "A"
    c_table["GCC"] = "A"
    c_table["GCA"] = "A"
    c_table["GCG"] = "A"
    c_table["TAT"] = "Y"
    c_table["TAC"] = "Y"
    c_table["TAA"] = "stop"
    c_table["TAG"] = "stop"
    c_table["CAT"] = "H"
    c_table["CAC"] = "H"
    c_table["CAA"] = "Q"
    c_table["CAG"] = "Q"
    c_table["AAT"] = "N"
    c_table["AAC"] = "N"
    c_table["AAA"] = "K"
    c_table["AAG"] = "K"
    c_table["GAT"] = "D"
    c_table["GAC"] = "D"
    c_table["GAA"] = "E"
    c_table["GAG"] = "E"
    c_table["TGT"] = "C"
    c_table["TGC"] = "C"
    c_table["TGA"] = "stop"
    c_table["TGG"] = "W"
    c_table["CGT"] = "R"
    c_table["CGC"] = "R"
    c_table["CGA"] = "R"
    c_table["CGG"] = "R"
    c_table["AGT"] = "S"
    c_table["AGC"] = "S"
    c_table["AGA"] = "R"
    c_table["AGG"] = "R"
    c_table["GGT"] = "G"
    c_table["GGC"] = "G"
    c_table["GGA"] = "G"
    c_table["GGG"] = "G"
    c_table.update(dict((c_table[i], i) for i in c_table))

    return c_table


def rev_condon_table():

    c_table = dict()

    c_table["AAA"] = "F"
    c_table["AAG"] = "F"
    c_table["AAT"] = "L"
    c_table["AAC"] = "L"
    c_table["GAA"] = "L"
    c_table["GAG"] = "L"
    c_table["GAT"] = "L"
    c_table["GAC"] = "L"
    c_table["TAA"] = "I"
    c_table["TAG"] = "I"
    c_table["TAT"] = "I"
    c_table["TAC"] = "M"
    c_table["CAA"] = "V"
    c_table["CAG"] = "V"
    c_table["CAT"] = "V"
    c_table["CAC"] = "V"
    c_table["AGA"] = "S"
    c_table["AGT"] = "S"
    c_table["AGG"] = "S"
    c_table["AGC"] = "S"
    c_table["GGA"] = "P"
    c_table["GGG"] = "P"
    c_table["GGT"] = "P"
    c_table["GGC"] = "P"
    c_table["TGA"] = "T"
    c_table["TGG"] = "T"
    c_table["TGT"] = "T"
    c_table["TGC"] = "T"
    c_table["CGA"] = "A"
    c_table["CGG"] = "A"
    c_table["CGT"] = "A"
    c_table["CGC"] = "A"
    c_table["ATA"] = "Y"
    c_table["ATG"] = "Y"
    c_table["ATT"] = "stop"
    c_table["ATC"] = "stop"
    c_table["GTA"] = "H"
    c_table["GTG"] = "H"
    c_table["GTT"] = "Q"
    c_table["GTC"] = "Q"
    c_table["TTA"] = "N"
    c_table["TTG"] = "N"
    c_table["TTT"] = "K"
    c_table["TTC"] = "K"
    c_table["CTA"] = "D"
    c_table["CTG"] = "D"
    c_table["CTT"] = "E"
    c_table["CTC"] = "E"
    c_table["ACA"] = "C"
    c_table["ACG"] = "C"
    c_table["ACT"] = "stop"
    c_table["ACC"] = "W"
    c_table["GCA"] = "R"
    c_table["GCG"] = "R"
    c_table["GCT"] = "R"
    c_table["GCC"] = "R"
    c_table["TCA"] = "S"
    c_table["TCG"] = "S"
    c_table["TCT"] = "R"
    c_table["TCC"] = "R"
    c_table["CCA"] = "G"
    c_table["CCG"] = "G"
    c_table["CCT"] = "G"
    c_table["CCC"] = "G"
    c_table.update(dict((c_table[i], i) for i in c_table))

    return c_table


def check_seq(seq):

    if len(seq) % 3 == 0:
        return True
    else:
        return False


def nucleotide_to_polypeptide(seq, rev):

    poly_seq = ""

    if rev:
        c_table = rev_condon_table()
    else:
        c_table = condon_table()

    if check_seq(seq):
        for i in xrange(0, len(seq) - 3, 3):
            poly_seq += c_table[seq[i:i+3]]
    return Seq(poly_seq, generic_protein)





"""Find open reading frame base on sequence.
"""
import re


def find_locations(seq, tag):
    starts = []
    for m in re.finditer(tag, seq):
        starts.append(m.start())
    return starts


def get_all_orf(seq, rev):
    result = dict()

    if rev:
        sta = "TAC"
        end_1 = "ATT"
        end_2 = "ACT"
        end_3 = "ATC"
    else:
        sta = "ATG"
        end_1 = "TAA"
        end_2 = "TGA"
        end_3 = "TAG"

    result["starts"] = find_locations(seq, sta)
    result["ends"] = find_locations(seq, end_1)
    result["ends"] += find_locations(seq, end_2)
    result["ends"] += find_locations(seq, end_3)
    result["ends"].sort()
    print(result["ends"])
    return result


def find_all_orf(pos_dic):
    starts = pos_dic["starts"]
    ends = pos_dic["ends"]

    result = []

    max_pair = []

    index_end = 0

    for start in starts:
        while index_end < len(ends):
            end = ends[index_end]
            if start < end and (end - start) % 3 == 0:
                result.append([start, end + 3])
                if len(max_pair) == 0:
                    max_pair = [start, end + 3]
                elif (max_pair[1] - max_pair[0]) < (end + 3 - start):
                    max_pair = [start, end + 3]
                index_end += 1
                break
            else:
                index_end += 1
        index_end = 0
    result.append(max_pair)
    return result


def get_desi_pairs(pairs, length):
    desi_pairs = []
    for pair in pairs[:-1]:
        if pair[1] - pair[0] >= length:
            desi_pairs.append(pair)

    return desi_pairs


# TODO: Temporary use, need replace by formal method
def get_longest_pair(pairs, rev_pairs):

    pos_longest = pairs[-1][1] - pairs[-1][0]
    rev_longest = rev_pairs[-1][1] - rev_pairs[-1][0]
    return max(pos_longest, rev_longest)











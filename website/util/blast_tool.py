from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML


def blast_call(in_file, out_file):

    input_file = open(in_file, "rU")
    output_file = open(out_file, "w+")

    fasta_string = input_file.read()
    print(fasta_string)
    result_handle = NCBIWWW.qblast("blastp", "nr", fasta_string)
    result = result_handle.read()

    print("executed")

    output_file.write(result)


def blast_call_text(in_text):

    result_handle = NCBIWWW.qblast("blastp", "nr", in_text)

    print("executed")

    return result_handle


def read_blast_result(blast_xml):

    result_file = open(blast_xml)
    blast_record = NCBIXML.read(result_file)

    E_VALUE_THRESH = 0.04

    result_dict = dict()

    result_dict['hits': len(blast_record.alignments)]
    aligns = list()
    for alignment in blast_record.alignments:
        hsps = list()
        for hsp in alignment.hsps:

            if hsp.expect < E_VALUE_THRESH:
                hsp_dict = dict()
                hsp_dict['seq'] = alignment.title
                hsp_dict['len'] = alignment.length
                hsp_dict['eval'] = hsp.expect
                hsp_dict['ident'] = int(round(hsp.identities * float(100) / alignment.length))
                hsp_dict['query'] = hsp.query
                hsp_dict['match'] = hsp.match
                hsp_dict['sbjct'] = hsp.sbjct
            hsps.append(hsp_dict)
        aligns.append(hsps)

    result_dict['alignments', aligns]
    return result_dict


def read_blast_result_text(blast_handle):

    blast_record = NCBIXML.read(blast_handle)

    E_VALUE_THRESH = 0.04

    result_dict = dict()

    result_dict['hits'] =  len(blast_record.alignments)
    aligns = list()
    for alignment in blast_record.alignments:
        hsps = list()
        for hsp in alignment.hsps:

            if hsp.expect < E_VALUE_THRESH:
                hsp_dict = dict()
                hsp_dict['seq'] = alignment.title
                hsp_dict['len'] = alignment.length
                hsp_dict['eval'] = hsp.expect
                hsp_dict['ident'] = int(round(hsp.identities * float(100) / alignment.length))
                hsp_dict['query'] = hsp.query
                hsp_dict['match'] = hsp.match
                hsp_dict['sbjct'] = hsp.sbjct
            hsps.append(hsp_dict)
        aligns.append(hsps)

    result_dict['alignments'] = aligns
    return result_dict


def test():

    result = blast_call_text('MTSQTTINKPGPGDGSPAGSAPAKGWRGHPWVTLVTVAVGVMMVALDGTIVAIANPAIQD\
                            DLDASLADVQWITNAYFLALAVALITAGKLGDRFGHRQTFLIGVAGFAASSGAIGLSGSI\
                            AAVIVFRVFQGLFGALLMPAALGLLRATFPAEKLNMAIGIWGMVIGASTAGGPILGGVLV\
                            EHVNWQSVFFINVPVGIVAVVLGVMILLDHRAANAPRSFDVVGIVLLSASMFALVWALIK\
                            APEWGWGSGQTWVYIGGSVVGFVLFSVWETKVKEPLIPLAMFRSVPLSAGVVLMVLMAIA\
                            FMGGLFFVTFYLQNVHGMSPVDAGLHLLPLTGMMIVASPLAGAMITKVGPRIPLAGGMVC\
                            TAVAMFGISTLETDTGSGLMSIWFGLLGLGLAPVMVGATEVIVGNAPMELSGVAGGLQQA\
                            AMQIGGSLGTAVLGAVMASKVDSDLAGNWKDAGLPELTPQQADQASEAVRVGVPPVAPGT\
                            PAEVAGKITDVAHDTFISGMSLASLVAAGVAVVAVFVAFLTKRGENAEAGAGVGHI'
                            )

    re_dict = read_blast_result_text(result)

    print(re_dict['hits'])
    for alignments in re_dict['alignments']:
        for hsp in alignments:
            print(hsp['seq'])
            print(hsp['len'])
            print(hsp['eval'])
            print(hsp['ident'])
            print(hsp['query'][0:75] + "...")
            print(hsp['match'][0:75] + "...")
            print(hsp['sbjct'][0:75] + "...")




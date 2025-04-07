import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as json_file:
        sequential_data = json.load(json_file)

    return sequential_data[field]

#naivni algoritmus
def linear_search(seq, number):
    """
    Implementujte algoritmus sekvenčního vyhledávání, který v neseřazeném seznamu nalezne
    pozice a četnost výskytu zadaného čísla.
    ● V modulu searching.py vytvořte funkci linear_search(). Funkce bude mít dva
    vstupní parametry – prohledávanou sekvenci a hledané číslo.
    ● Funkce vrátí slovník se dvěma klíči. Pod prvním klíčem positions bude uložen
    seznam pozic (indexů). Pod druhým klíčem count bude uložen počet výskytů
    hledaného čísla.
    ● Volání funkce a korektnost její implementace ověřte voláním z hlavní funkce main().
    V hlavní funkci definujte také vyhledávané číslo.
    ● Vytvořte novou revizi (commit) a změny nahrajte na svůj vzdálený repozitář (push).
    :param sequence:
    :param number:
    :return:
    """
    # seznam_pozic = []
    # for idx, cislo in enumerate(sequence):
    #     if cislo == number:
    #         seznam_pozic.append(idx)
    #     else:
    #         continue
    # pocet_vyskytu = len(seznam_pozic)
    # slovnik = {"positions":seznam_pozic, "count":pocet_vyskytu}
    # return slovnik
    indices = []
    count = 0
    idx = 0
    while idx < len(seq):
        if seq[idx] == number:
            indices.append(idx)
            count += 1
        idx += 1

    return {"positions":indices, "count":count,}

# def pattern_search(seq_dna, vzor):
#     """
#     Funkce vrátí množinu, ve které budou uloženy pozice (indexy) výskytu vzoru v sekvenci.
#     :param seq_dna:
#     :param vzor:
#     :return:
#     """
#     pozice = set()
#     idx_seq = 0
#     while idx_seq < len(seq_dna):
#         delka_vzoru = len(vzor)
#         if seq_dna[idx_seq:idx_seq+delka_vzoru] == vzor:
#             pozice.add((idx_seq, idx_seq+delka_vzoru-1))
#         idx_seq += 1
#     return pozice

def pattern_search(seq, pattern):
    indices = set()
    pattern_size = len(pattern)
    left_idx = 0
    right_idx = pattern_size
    while right_idx < len(seq):
        for idx in range(pattern_size):
            #for pro uvedomeni, ze jde o linearni vyhledavani pri porovnani dvou sekvenci
            if pattern[idx] != seq[left_idx + idx]:
                break
        else:
            indices.add(left_idx + pattern_size // 2)

        left_idx += 1
        right_idx += 1
    return indices


def main():
    file_name = "sequential.json"
    seq = read_data(file_name, field="unordered_numbers")
    print(seq)
    vyhledavani = linear_search(seq, 0)
    print(vyhledavani)
    seq_dna = read_data(file_name, field="dna_sequence")
    #print(seq_dna)
    # seq_dna = "ATGACGGAATATAAGCTAGGTGGTGGCTGGGCAGTCCGCGCTGATAGGGCAAGAGTGCGCGTACCATACCACGCTAAGCCATATAGGGCATCAGTCAGCCTGGCA"
    vyhledani_vzoru = pattern_search(seq_dna, "GAC")
    print(vyhledani_vzoru)




if __name__ == '__main__':
    main()
import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field): #klic specific pro nase data
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_name) as data_file:
        data = json.load(data_file)
        #print(data)
        searchin = data[field]
    if field in data.keys():
        return searchin
    else:
        return None
        #relativni cesta je nazev toho souboru, absolutni vede od zacatku
file_name = "sequential.json"
field = "unordered_numbers"

#print(read_data(file_name, field)) #[54, 2, 18, 5, 3, 31, 20, 65, -10, 300, 17, 5, -1, 0, 0, 102, 7, 8, 9, 9, -3, -5, 0, 1, 63, 82, -36, -5]



def linear_search(seq, searched_number):
    nalezene_pozice = list() #probehne jednou
    for pozice, number in enumerate(seq): #probehne nkrát dle poctu hodnot v seq
        if number == searched_number: #proběhne n krat
            nalezene_pozice.append(pozice) #proběhne n krat
    slovnik = dict()
    slovnik["positions"] = nalezene_pozice
    slovnik["counts"] = len(nalezene_pozice) #dokupy 3
    #v nejhorsim pripade 3n+4 --o(n)

    return slovnik #{"positions": "hodnota", "count": "pocet vyskytu"} v returnu

#nejlepe podm ifu ani jednou --celkem 2n+4....O(n)
#sequence = read_data(file_name, field)
#print(linear_search(sequence, 2)) #{'positions': [1], 'counts': 1}

# field2 = "dna_sequence"
# dna = read_data("sequential.json", "dna_sequence")
# print(dna)
# seq = dna
# pattern = "GAC"
#
# def pattern_search(seq, pattern):
#     nalezene_pozice = []
#     n = len(seq)
#     m = len(pattern)
#     iterace = n - (m - 1) #4 řádky
#     #iterace = len(seq) - (len(pattern) -1)
#     for pozice_v_seq in range(iterace): #3*(n-(m-1)) pro 61, a nevim.
#         #print(pozice_v_seq) #cisla poradi
#         pocitadlo = 0
#         for pozice_ve_vzoru in range(len(pattern)):
#             pismenko_v_sekvenci = seq[pozice_v_seq + pozice_ve_vzoru] #kontrola treti a ctvrte
#             pismenko_ve_vzoru = pattern[pozice_ve_vzoru]
#             if pismenko_v_sekvenci == pismenko_ve_vzoru:
#                 pocitadlo +=1
#         if pocitadlo == m:
#             nalezene_pozice.append(pozice_v_seq)
#     return nalezene_pozice
#5(m(n-(m-1))) nevim kde

#secist #tři řádky a ne 4, bo vrátil zpet iteraci --nepojmenovaval to pro cyklus for
#3+3(n-(m-1))+5(m(n-(m-1)))
#3+3n-3m-3+5mn-5m^2+5m ---délka O(mn)
#je to dluhe, kdyz prvni nesedi, nemusim kontrolovat cely vzor

#uprava final:
# def pattern_search(seq, pattern):
#     nalezene_pozice = []
#     n = len(seq)
#     m = len(pattern)
#     iterace = n - (m - 1) #4 řádky
#     #iterace = len(seq) - (len(pattern) -1)
#     for pozice_v_seq in range(iterace): #3*(n-(m-1)) pro 61, a nevim.
#         #print(pozice_v_seq) #cisla poradi
#         pocitadlo = 0
#         for pozice_ve_vzoru in range(len(pattern)):
#             pismenko_v_sekvenci = seq[pozice_v_seq + pozice_ve_vzoru] #kontrola treti a ctvrte
#             pismenko_ve_vzoru = pattern[pozice_ve_vzoru]
#             if pismenko_v_sekvenci == pismenko_ve_vzoru: #urceni shody, v ne zastav for
#                 pocitadlo +=1
#             else:
#                 break
#         if pocitadlo == m:
#             nalezene_pozice.append(pozice_v_seq)
#     return nalezene_pozice
# #vypocetni narocnost-v nejhorsim nic, v nejlepsim vnitrni probehne jen jednou
# #3+3(n-(m-1))+5(1(n-(m-1))) ---O(n)
# print(pattern_search(dna, "GAC"))


# seq = [6, 12, 17, 23, 38, 45, 77, 84, 90]
# search_nmb = 45
# levy = 0#seq[0]
# pravy = len(seq)#[seq[-1]]
#
# while True:
#     middle = (pravy + levy) // 2
#     cislo = seq[middle]
#     if cislo < search_nmb:
#         #divam doprava, posunu levy
#         levy = middle + 1
#     elif cislo > search_nmb:
#         pravy = middle - 1
#     else:
#         print(middle)
#         print(cislo)
#         break

#co kdyz cislo nebude? --pobezi to porad
#chci zastavit, jak se leva rovna prave


def binary_search(seq, search_nmb): #pozice leva a prava a pak zajem o stredy
    levy = 0  # seq[0]
    pravy = len(seq)  # [seq[-1]]

    while True:
        middle = (pravy + levy) // 2
        cislo = seq[middle]
        if cislo < search_nmb:
            # divam doprava, posunu levy
            levy = middle + 1
        elif cislo > search_nmb:
            pravy = middle - 1
        else:
            return middle
    middle = (pravy + levy) // 2
    cislo = seq[middle]
    if cislo < search_nmb:
        # divam doprava, posunu levy
        levy = middle + 1
    elif cislo > search_nmb:
        pravy = middle - 1
    else:
        return middle


seq = [6, 12, 17, 23, 38, 45, 77, 84, 90]
search_nmb = 6
print(binary_search(seq, search_nmb))

#cyklus co puli, puli, puli, da log. slozitost a to je TOP TIER!!!

def main():
    pass


if __name__ == '__main__':
    main()



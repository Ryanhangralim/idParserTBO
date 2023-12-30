TABEL_CYK = {}

#membuka file dan import grammar
def get_grammar():
    #buka file dan import lhs dan rhs dari rule cnf
    RESULT = {}
    RESULT.clear()
    f = open("rules.txt", "r", encoding="utf-8")
    for lines in f:
        line = lines.splitlines()
        line = line[0].split(" -> ")
        lhs = line[0]
        rhs = line[1].split(" | ")
        if lhs in RESULT.keys():
            RESULT[lhs].extend(rhs)
        else:
            RESULT[lhs] = rhs
    f.close()

    #convert PropNoun (nama) menjadi huruf kecil
    for key, value in RESULT.items():
        if key == "PropNoun":
            tempList = []
            for val in value:
                if val not in tempList:
                    tempList.append(val.lower())
            RESULT[key] = tempList
    return RESULT

#mengecek apakah string diterima atau tidak
def is_accepted(inputString):
    global TABEL_CYK
    TABEL_CYK.clear()
    grammar = get_grammar()
    inputString = inputString.lower().split(" ")

    #inisialisasi tabel cyk
    for i in range(1,len(inputString)+1):
        for j in range(i, len(inputString)+1):
            TABEL_CYK[(i,j)] = set()

    for i in reversed(range(1, len(inputString)+1)):
        for j in range(1, i+1):
            #mengisi baris paling bawah tabel segitiga
            if (j == j + len(inputString) - i):
                tempList = set()
                for key, value in grammar.items():
                    for val in value:
                        if (val == inputString[j-1]):
                            tempList.add(key)
                TABEL_CYK[(j, j + len(inputString) - i)] = tempList
            #mengisi baris sampai paling atas
            else:
                tempList = set()
                resultList = set()
                for k in range(len(inputString) - i):
                    first = TABEL_CYK[(j,j+k)]
                    second = TABEL_CYK[(j+k+1,j+len(inputString) - i)]
                    for fi in first:
                        for se in second:
                            tempList.add(fi + " " + se)
                for key, value in grammar.items():
                    for val in value:
                        if (val in tempList):
                            resultList.add(key)
                TABEL_CYK[(j,j+len(inputString) - i)] = list(resultList)
    if "K" in TABEL_CYK[(1, len(inputString))]:
        return True
    else:
        return False

#mengembalikan tabel
def get_table_element(inputString):
    global TABEL_CYK
    result = []
    n = len(inputString.split(" "))
    for i in range(1, n+1):
        temp = []
        for j in range(i):
            res = TABEL_CYK[(j+1, n-i+j+1)]
            if len(res) == 0:
                temp.append("\u2205")
            else:
                temp.append("{" + ", ".join(res) + "}")
        result.append(temp)
    result.append(inputString.split(" "))
    return result


def read_text():
    file = open("program.txt", "r")
    rows = []
    for line in file:
        words = line.split()
        rows.append(words)
    return rows
def get_binary(decimal_number):
    binary = bin(decimal_number)
    binary = binary[2:]
    while (len(binary) <= 9):
        binary = "0"+binary
    return binary[2:]
def write_binary_resutl(lines):
    file = open("result.txt","w")
    for line in lines: file.write(line)
    file.close()
def get_opcode(opcole):
    if opcole == "RST":
        return get_binary(1)
    elif opcole == "SAVR":
        return get_binary(2)
    elif opcole == "SAVM":
        return get_binary(3)
    elif opcole == "MVMR":
        return get_binary(4)
    elif opcole == "MVRR":
        return get_binary(5)
    elif opcole == "MVRM":
        return get_binary(6)
    elif opcole == "PRNM":
        return get_binary(7)
    elif opcole == "PRNR":
        return get_binary(8)
    elif opcole == "ADD":
        return get_binary(9)
    elif opcole == "SUB":
        return get_binary(10)
    elif opcole == "MUL":
        return get_binary(11)
    elif opcole == "AND":
        return get_binary(12)
    elif opcole == "OR":
        return get_binary(13)
    elif opcole == "NOT":
        return get_binary(14)
    elif opcole == "CMP":
        return get_binary(15)
    elif opcole == "JG":
        return get_binary(16)
    elif opcole == "JE":
        return get_binary(17)
    elif opcole == "JL":
        return get_binary(18)
    elif opcole == "JGE":
        return get_binary(19)
    elif opcole == "JLE":
        return get_binary(20)
    elif opcole == "JNE":
        return get_binary(21)
    elif opcole == "JU":
        return get_binary(22)
    elif opcole == "FIN":
        return get_binary(23)
    elif opcole == "INC":
        return get_binary(24)    
    else:
        return "no_opcode_found"
    
def traslator(lines):
    binarylines = []
    
    for line in lines: 
        if(line[2] == ","):
            word = get_opcode(line[0])+ get_binary(int(line[1])) + get_binary(int(line[3]))+"\n"
            binarylines.append(word)
    return binarylines

write_binary_resutl(traslator(read_text()))


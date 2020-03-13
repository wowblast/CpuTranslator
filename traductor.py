
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
    if opcole == "MVRR":
        return get_binary(5)
    else:
        return get_binary(0)
    
def traslator(lines):
    binarylines = []
    
    for line in lines: 
        if(line[2] == ","):
            word = get_opcode(line[0])+ get_binary(int(line[1])) + get_binary(int(line[3]))+"\n"
            binarylines.append(word)
    return binarylines

write_binary_resutl(traslator(read_text()))


def length(string):
    length_of_line = int(string[1])
    length_of_letter = int(string[2])
    length_of_string = len(string[0])
    l =  0
    r = length_of_line//length_of_letter
    m = r
    lt = []
    for i in range((length_of_string//m)+1):
        lt.append(string[0][l:r])
        l = r
        r += length_of_line//length_of_letter

    for x in lt:
        print(x)

string = "testprogram 6 3".split()
length(string)
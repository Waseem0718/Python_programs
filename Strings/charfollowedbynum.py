#input = a1b10 output = abbbbbbbbbb
def charfollowedbynum(string):
    result = []
    
    for i in range(len(string)):
        if string[i].isalpha():
             char = string[i]
             i += 1
             num_str = ""
             while i < len(string) and string[i].isdigit():
                 num_str += string[i]
                 i += 1

             num = int(num_str) 
             result.append(char*num)

    return ''.join(result)

string = "a09b10c5"
print(charfollowedbynum(string))

                 
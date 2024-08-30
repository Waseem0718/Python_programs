# def printstring(str):
     
#     result = ""

#     for ch in str:
#         if ch.isalpha():
#                x = ch
#         else:
#             d = int(ch)
#             result += x*d
    
#     return result

# str = "a4b3c2"
# print(printstring(str))

def abc(str1):
     
     char_count = {}
     for ch in str1:
          if ch in char_count:
               char_count[ch] = char_count.get(ch,0) + 1 
          else:
               char_count[ch] = 1


    
     output = ""
     for key,value in char_count.items():
         output += str(value)+key

     return output    
          
     

str1 = "aaaabbbbcccz"
print(abc(str1))
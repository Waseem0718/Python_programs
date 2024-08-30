def petrol(distance,rem,initial):
     
    for i in range(0,len(distance)):
          initial = (initial - distance[i]) + rem[i]
          if initial < 0:
               return "not enough petrol to travel"
     
          
    return initial
     
distance = [1,5,3]
rem = [6,4,2]
initial = 2
print(petrol(distance,rem,initial)) 













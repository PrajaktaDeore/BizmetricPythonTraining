# 8.	Create city = “Pune” 

city = "Pune"

# •	Convert to int  
# output = int(city)
# print(type(output))

#    output = int(city)
#              ^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'Pune'
   
# •	Convert float
# fl = float(city)
# print(type(f1)) 

#    fl = float(city)
#          ^^^^^^^^^^^
# ValueError: could not convert string to float: 'Pune'

# •	Convert list
li = list(city)
print(type(li))

#output : <class 'list'>

# •	Convert tuple
tu = tuple(city)
print(type(tu)) 

#output : <class 'tuple'>

# •	Convert dict
# dict = dict(city)
# print(type(dict))

#  File "c:\Users\sudar\OneDrive\Desktop\Praju Bizmetric\python practice\assessmentfromeighteen.py", line 34, in <module>
#     dict = dict(city)
#            ^^^^^^^^^^
# ValueError: dictionary update sequence element #0 has length 1; 2 is required

# •	Convert set 

set = set(city)
print(type(set))

# <class 'set'>


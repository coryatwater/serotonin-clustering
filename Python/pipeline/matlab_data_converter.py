x = open("scanned_indices/xc.py", "r").read()
y = open("scanned_indices/yc.py", "r").read()
z = open("scanned_indices/zc.py", "r").read()

matlab_data = open('matlab_data.m', 'w')
data_string = ''
data_string += x + '\n'
data_string += y + '\n'
data_string += z + '\n'

data_string = data_string.replace("[","{") 
data_string = data_string.replace("]","}") 
data_string = data_string.replace("(","[") 
data_string = data_string.replace(")","]") 

matlab_data.write(data_string)

I have a python 2.7 code where it reads a list of numbers separated by commas from a text file and it returns the amount of decimal places from each number in the list separated by a tab and if there is a space in between the number and comma then it will return white space, if there is no white space then it returns no error. What I need now is to detect if there is a tab in between the number and comma, it should return "Tab return detected". Also, on the last line of the list of numbers, there should be no carriage return so it should return on the last line "No carriage return found" 

import re 

with open('file.txt', 'r') as f_in: 
line_no = 1 
for line in f_in: 
if not line.strip(): 
continue 
print('Line {}:'.format(line_no)) 
print('\t'.join(str(len(g)) for g in re.findall(r'\d+\.?(\d+)?', line) )) 
print('white space found' if re.findall(r',(\s+)\d', line) else 'no error found') 
line_no += 1 

List of numbers from Text File: 

1.0, 2.02,1.123 
1.0, 2.02, 1.123 
1 
Expected: 

Line 1: 1"tab"2"tab"3"tab" No error 
Line 2: 1"tab""2"tab"3"tab" white space detected tab detected 
Line 3: 0 No Carriage return No error 

Actual: 

Line 1: 1 2 3 
No error 
Line 2: 1 2 3 
Whitespace detected 
Line 3: 0 
No error
"""
If we want to write a list to a file, we cannot make use of f.write(list_var)
Using the above line will throw the following error message:

TypeError: argument 1 must be string or read-only character buffer, not list

We can either use pickle dump (machine readable format) or json dump for human readable format

"""
import json

num_list = [1,2,3,4,5]
str_list = ["string 1", "string 2", "string 3", 4, "staahhpp!!"]
file_obj = open("filename.txt", "w") 

json.dump(num_list, file_obj)
file_obj.write("\n")
json.dump(str_list, file_obj)
file_obj.write("\n")
print "\n Printing the contents of the file \n"
file_obj.close()

file_obj = open("filename.txt", "r") 
for line in file_obj:
    print line

file_obj.close()


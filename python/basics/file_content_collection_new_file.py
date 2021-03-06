#merging_text_files.py

###################    program 1 start ###################
#collect content from specific files and output their content in filename w/date of creation
# import datetime

# filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
# # characters = [" ",":"]
# # for c in characters:
# # 	filename = filename.replace(c,"-")

# print (filename)


# with open("file1.txt","r") as content1:
# 	cont1 = content1.read()

# #print (cont1)

# with open("file2.txt","r") as content2:
# 	cont2 = content2.read()

# #print (cont2)

# with open("file3.txt","r") as content3:
# 	cont3 = content3.read()

# #print (cont3)


# with open (filename+".txt","w") as myfile:
# 	myfile.write(cont1+'\n'+ cont2+'\n' + cont3+'\n')

###################    program 1 end ###################


###################    program 2 start ##################
#find all files in directory with "f" in filename
#collect content and output in "resulting_file"

import datetime
import glob2
import os
import getpass

#delete output file
os.remove("resulting_file.txt")

#get new timestamp for output file
new_file = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")

#determine all source files
filenames = glob2.glob("*f*.txt")

#create header in new output file
with open ("resulting_file.txt","w") as results:
	results.write(new_file + ' created by '+ getpass.getuser()+'\n\n')

#get content from all source files and append in output file
for file in filenames:
	with open (file,"r") as content:
		cont = content.read()
		with open ("resulting_file.txt","a") as results:
			results.write (file +": " + cont + '\n')

###################    program 2 end ###################

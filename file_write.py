file_name = "My_file.txt"
file_name_new = "My_file_2.txt"
#When using with no need of close()
with open(file_name,'a') as f:
	f.write("Gud mrng\n")
	f.write("Have a breakfast\n")

#here close() is necessary
f1 = open(file_name_new,'a')
f1.write("Good Morning\n")
f1.write("Have a brreakfast\n")
f1.close()


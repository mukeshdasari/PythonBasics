def print_msg(msg,error="no error",**kwargs):
	print("Log : "+msg+" : "+error+" : ")
	print(kwargs)
print_msg("Hello world",key1="1",key2="2", key3="3")

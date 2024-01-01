#  Python script to cancatenate following dictionaries to create a new one

dict_1={'a':100,'b':200,'c':300}
dict_2={'d':400,'e':500,'f':600}
# ** double asterick is used to unpack the dict
adding = {**dict_1,**dict_2}

print(adding)
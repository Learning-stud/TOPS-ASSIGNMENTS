# find the highest 3 values in a dictionary

my_dictionary ={'a':10 , 'b':20 , 'c':35 , 'd':50 , 'e':40}

highest = sorted(my_dictionary.values(),reverse=True)[:3]  # sorting descending order mein hoga, yaani sabse badi value se lekar sabse chhoti value tak  isliye reverse true diya he .
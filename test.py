# import json 

# tmp_dict = {
# 	"reham" : 122
# }

# with open('songs.txt','w') as f :

# 	tmp_dict['sara'] = 222
# 	f.write('{')

# 	f.write('\n\t"names": [')

# 	f.write(",\n\t\t\t\"{}\"".format( str(tmp_dict['sara'])))
# 	f.write(",\n\t\t\t\"{}\"".format( str(tmp_dict['reham'])))

# 	f.write("\n\t\t],")

	
# 	f.write('\n\t"names": [')

# 	f.write(",\n\t\t\t\"{}\"".format( str(tmp_dict['sara'])))
# 	f.write(",\n\t\t\t\"{}\"".format( str(tmp_dict['reham'])))

# 	f.write("\n\t\t],")




# 	f.write("\n}")

A = [17, 3, 9, 28, 16, 12, 4, 6]
i = 1
n = len(A)
x = 12

while i <= n and A[i] != x:
	i += 1

print(i)
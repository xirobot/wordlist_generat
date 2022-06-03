from itertools import product


Z = '\033[1;31m'
L = '\033[1;37m'

print('''

░██╗░░░░░░░██╗██╗░░░░░░░░░░░░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
░██║░░██╗░░██║██║░░░░░░░░░░░██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
░╚██╗████╗██╔╝██║░░░░░█████╗██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
░░████╔═████║░██║░░░░░╚════╝██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
░░╚██╔╝░╚██╔╝░███████╗░░░░░░╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚══════╝░░░░░░░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
''')
print(Z+'''
                                                  INSTA:@vi_ox7
''')


min_len = int(input((Z+'[+]')+(L+' Enter The mini Length : ')))
max_len = int(input((Z+'[+]')+(L+' Enter The max Length : ')))
counter = 0
charater = str(input((Z+'[+]')+(L+' Enter The Charter : ')))
file_name = str(input((Z+'[+]')+(L+' Enter File Name : ')))

file_open = open(file_name,'w')

for i in range(min_len,max_len+1):
    for j in product(charater,repeat=i):
        word = "".join(j)
        file_open.write(word)
        file_open.write('\n')
        counter+=1
print(("Your Wordlist Of {} Passwords Ready".format(counter)))

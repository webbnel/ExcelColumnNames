col = input("How many columns?\n")

d = {}

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for x in range(int(col)):
    if(x < len(letters)):
        d[x] = letters[x]
    else:
        first = letters[x//len(letters)-1]
        second = letters[x % len(letters)]
        d[x]= first+second

print (d)
f = open("file1.txt", "w")
f.write("this is my file with My Info i.e. name is Ruchil Patel Roll is 20124108 DOB is 15 11 2001. \n new line")
f.close()
file=open("file1.txt","r")
NOL=0
NOW=0
NOC=0
NOWS=0
UC=0
LC=0
DG=0
WS=0
for line in file:
     NOL+=1
     word='Y'  
     for letter in line:
         if (letter != ' ' and word == 'Y'):
             NOW+= 1
             word ='N'
         elif (letter == ' '):
             NOWS+= 1
             word = 'Y'
         for i in letter:  
              if(i !=" " and i !="\n"):
                  NOC+=1
file.close()
file=open("file1.txt","r")
data=file.readlines()
for data in data:
    for character in data:
        if character.isupper():
            UC+= 1
        elif character.islower():
            LC+= 1
        elif character.isspace():
            WS+=1
        elif character.isdigit():
            DG+=1
print("Number of words in text file: ",NOW)
print("Number of lines in text file: ",NOL)
print('Number of characters in text file: ',NOC)
print('The whitespace count is',NOWS)
print('The uppercase count is',UC)
print('The lowercase count is',LC)
print('The digit count is',DG)

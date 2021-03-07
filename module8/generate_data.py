#Writes a .txt file with 0-99999
myfile = open('data.txt', 'w')
for num in range(100000):
    myfile.write(str(num)+ '\n')

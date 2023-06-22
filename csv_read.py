file = open('csv_data#3.txt', 'r')
lines = file.readlines()
file.close()

lines =[line.strip() for line in lines[1:]] #used to remove\n.
print(lines)


for line in lines:
    #print(line)
    person_data = line.split(',')
    #print(person_data)
    name = person_data[0]
    age = person_data[1]
    university = person_data[2]
    degree = person_data[3]
    
    print(f'{name} is {age}, studying {degree} at {university}')
    
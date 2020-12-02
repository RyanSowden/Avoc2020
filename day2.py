pas = [line.rstrip('\n') for line in open("day2.txt")]

x = 0

for i in range(len(pas)):
    numbers = pas[i].split()[0].split("-") #get both numbers (first and second)
    char = pas[i].split()[1].strip(":") #get letter
    passw = pas[i].split()[2] #get password
    firstN = int(numbers[0])-1 #first number
    secondN = int(numbers[1])-1 #second number
    if passw[firstN] != passw[secondN] and (passw[firstN] == char or passw[secondN] == char):
        x += 1
 
print("The are", x, "valid passwords")

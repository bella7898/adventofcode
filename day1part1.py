with open("input.txt", "r") as file: 
  numList = []
  final = 0
  
  for line in file: 
    numLineDigits = 0
    lineNumbers = []
    print(line)
    for char in line: 
      print(char)
      if char.isdigit():
        numLineDigits += 1
        lineNumbers.append(str(char))
    print(lineNumbers)
    print(numLineDigits)  
    firstNum = lineNumbers[0]
    lastNum = lineNumbers[numLineDigits-1]
    print(firstNum)
    print(lastNum)
    numList.append(str(firstNum) + str(lastNum))
        

for item in numList: 
 number = int(item)
 final += number
print(final)
file.close()

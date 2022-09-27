
_letters = [["а","б","в","г","д","е"],["ж","з","и","й","к","л"],["м","н","о","п","р","с"],["т","у","ф","х","ц","ч"],["ш","щ","ъ","ы","ь","э"],["ю","я",".","_",",","-"]]

_str = ""

print("1 - расшифровка\n2 - шифровка")
choice = int(input())
_word = input()
_word = list(_word)
_coordinates = [1] * (len(_word)*2)
if(choice == 1):
  for x in range(len(_word)):
    for i in range(len(_letters)):
      for j in range(len(_letters[i])):
        if(_word[x] == _letters[i][j]):
          _str += str(j+1) + str(i+1)
  _output = ""

  for d in range(len(_str)//2):
    _output +=_letters[int(_str[d+len(_str)//2])-1][int(_str[d])-1]
  print(_output)
else:
  for i in range(len(_word)):
    for j in range(6):
        for k in range(6):
          if(_word[i] == _letters[j][k]):
            _coordinates[i] = k
            _coordinates[i + len(_word)] = j
  _message = ""
  for i in range(0,len(_word)*2,2):
    _message += _letters[_coordinates[i+1]][_coordinates[i]]
  print(_message)

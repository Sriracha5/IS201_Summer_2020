print("for-Break")
for letter in 'Python':
    if letter == 'h ':
        break
    print ('Current Letter :', letter)

print("\nWhile-Break")
var = 10 
while var > 0:
    print ('current variable value :', var)
    var = var -1
    if var == 5:
        break
    print ("Goof bye!")
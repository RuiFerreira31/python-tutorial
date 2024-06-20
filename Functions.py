def calculation(a,b, sign):
    if sign == "+":
        return a+b
    elif sign == "-":
        return a-b


x = calculation(3,5, "+")
print(x)

print("###############")

def showEmployee(name, salary):
    print("Employee " + name + " salary is: " + salary)


showEmployee("Rui","1")

print("###############")

def outer(a,b):
    def inner(a,b):
        return a+b
    x = inner(a,b)
    return x+8

print(outer(5,6))


print("###############")

def isPalindrome(word):
    i = len(word) -1
    reversedWord = ""
    while i >= 0:
        reversedWord = reversedWord + word[i]
        i = i-1
    print(reversedWord)
    print(word)
    j = 0
    while j <= len(word) -1:
        print(word[j])
        print(reversedWord[j])
        if word[j] != reversedWord[j]:
            return False
        j = j +1
    return True


checkPalindrome = isPalindrome("boat")

print(checkPalindrome)



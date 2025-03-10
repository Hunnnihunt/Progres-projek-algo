#MATERI RECURSIVE DAN PALINDROM

hasil = 1
angka = 5
for i in range (1,angka+1):
    hasil = hasil * i  
print(hasil)


# def faktorial(n):
#     if in == 0:
#         return 1
#     else:
#         return n * faktorial(n-1)
# print(faktorial(5))

def tailrecrusive( total, value ):
    if (value<=0):
        return total
    else:
        return tailrecrusive(total*value, value-1)

print(tailrecrusive(1,5))

def ispalindrome(s):
    s = s.lower()
    l = len(s)
    print(s)
    if l < 2:
        return True
    elif s[0] == s[l-1]:
        return ispalindrome(s[1:l-1])
    else:
        return False
print(ispalindrome("malam"))

palindrom = "malam. .malam"
for x in range(len(palindrom)//2):
    if palindrom[x] != palindrom[len(palindrom)-x-1]:
        print(False)
        break
else:
    print(True)

palindrom = 'kasur rusak'
# palindrom = "".join([x for x in palindrom if x != ""])
palindrom2 = []
for i in palindrom:
    if i != " ":
        palindrom2 += i
print(palindrom2)

# palindrom.strip()
# print(palindrom)

for x in range(len(palindrom)//2):
    if palindrom[x] != palindrom[len(palindrom)-x-1]:
        print(False)
        break
else:
    print(True)

def pangkatR(n,p):
    if p == 0:
        return 1
    elif p > 0:
        return n * pangkatR(n, p-1)
    else:
        return 1 / pangkatR(n, 0-p)
print (pangkatR(2,2))
print (pangkatR(5,2))

# r = input("masukkan kalimat : ")
# reversed = r[::-1]

# if r == reversed:
#     print("itu kalimat palindrome")
# else:
#     print("itu bukan kalimat palindrome")

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Testing the function
print(fibonacci(5))  # Output: 5
print(fibonacci(7))  # Output: 13

def balik_kata(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + balik_kata(s[:-1])

# Testing the function
print(balik_kata("hello"))  # Output: "olleh"
print(balik_kata("python"))  # Output: "nohtyp"

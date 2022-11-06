#HOMEWORK


name = input("WHAT IS YOUR NAME?")
GetName()

int a = input()
int b = input()
int c = input()
int d = input()
print (a + b + c)
print (a * b * c * d)


def isPalindrome(s):
    return s == s[::-1]
s = "malayalam"
ans = isPalindrome(s)
if ans:
    print("True")
else:
    print("False")


 def bubble(lst, a=False):
    if a:
      for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    elif not a:
      for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
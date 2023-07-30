import re

x = "From: using the : character"
y = re.findall("^F.*:", x)
z = re.findall("^F.*?:", x)
# print(y)
# print(z)


line = "From jingru@email.com Fri July"
text = re.findall("\S+@\S+", line)
text1 = re.findall("^From (\S*@*\S)", line)
# print(text)
# print(text1)


# to show only email.com
text2 = re.findall("@([^ ]*)", line)
# or

# text3 = re.findall("^From .*@([^ ]*)", line)
# print(text2)


# escape Character

a = "we just received $100.00 for snack."
b = re.findall("\$[0-9.]+", a)
print(b)

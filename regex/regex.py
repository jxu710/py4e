import re

x = "From: using the : character"
y = re.findall("^F.*:", x)
z = re.findall("^F.*?:", x)
# print(y)
# print(z)


line = "From jingru@email.com Fri July"
text = re.findall("\S+@\S+", line)
text1 = re.findall("^From (\S*@*\S)", line)
print(text1)

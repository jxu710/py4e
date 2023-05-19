# my answer:
hour = input("what hour")
rate = input("how much u earn")

try:
    if int(hour) > 40:
        extratime = int(hour) - 40
        pay = 40 * int(rate) + extratime * int(rate) * 1.5
        print("ur ovetime overall pay is", pay)
    else:
        pay = int(hour) * int(rate)
        print("ur weekly pay is", pay)
except:
    print("not a number")

# instructor's answer

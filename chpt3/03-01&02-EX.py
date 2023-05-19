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
    quit()

# instructor's answer

sh = input("Enter Hours:")
sr = input("Enter Rate:")

try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric number")
    quit()

if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fr * fh
print("pay:", xp)

def computepay(hours, rate):
    if hours > 40:
        reg = hours * rate
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp

    else:
        pay = hours * rate

    return pay


sh = input("Enter Hours:")
sr = input("Enter Rate:")
fh = float(sh)
fr = float(sr)

print("Your pay is:", computepay(fh, fr))

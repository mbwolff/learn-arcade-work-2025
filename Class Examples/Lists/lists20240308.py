months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number: "))
m = months[3*(n-1):3*(n-1)+3]

print(f"The month is {m}.")

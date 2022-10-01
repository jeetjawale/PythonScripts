with open("E:\Coding\ALL Projects\currencyData.txt") as f:
    lines = f.readlines()

curr = {}
for line in lines:
    parsed = line.split("\t")
    # print(parsed)
    curr[parsed[0]] = parsed[1]

print(curr)
amt = int(input("Enter the amount: "))
print("Enter the amount you want to convert the amount to? Available Options:\n")
[print(i) for i in curr.keys()]

currency = input("Enter the currency: ")

print(f"{amt} INR is {amt * float(curr[currency])} {currency}")

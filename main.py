myage = 45
myage = 54
print(myage)
if myage>18:
    print("Du bist erwachsen.")
elif myage==18:
    print("Glückwunsch, du bist gerade erwachsen geworden.")
else:
    print(" Bist noch ein Kind.")
for i in range(5):
    print(i)
def print_account(bank_accont_info):
    for bank_accont_info in bank_balances:
        print(bank_accont_info)

bank_balances = [1234.4,50344.00, -12.33]
print_account(bank_balances)



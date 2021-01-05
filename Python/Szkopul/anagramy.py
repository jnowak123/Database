og_slowo = sorted(input().strip())
test_slowo = sorted(input().strip())

for letter in range(len(og_slowo)):
    if og_slowo[letter] != test_slowo[letter]:
        print("NIE")
        quit()

print("TAK")
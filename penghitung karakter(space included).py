import os
print("Masukkan kalimat atau kata yang ingin dihitung")
print("")
Input = input("=> ")

raw_data = list(Input)
passed_input = []

for chara in raw_data:
    if chara in passed_input:
        pass
    elif chara == " ":
        pass
    else:
        passed_input.append(chara)
os.system("cls")
print("Jumlah karakter dari", Input, "adalah", len(passed_input))
print("")
input("press ENTER to exit")




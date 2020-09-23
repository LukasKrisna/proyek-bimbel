print("Bimbel BP")
print("Biar Pinter")
print("1. SMP")
print("2. SMA")
BIMBEL = int(input("Pilih nomer untuk jenjang: "))
if (BIMBEL == 1):
    import main_smp
elif (BIMBEL == 2):
    import main_sma
else:
    print("Maaf, menu tidak tersedia")

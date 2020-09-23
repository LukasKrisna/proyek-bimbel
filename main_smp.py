import member_smp
print("1. Daftar")
print("2. Ubah Data Member")
print("3. Hapus Member")
print("4. Tampilkan Seluruh Member")
menu2= int (input('Pilih nomer='))
if (menu2==1):
    nama=input("Nama:")
    alamat=input("Alamat:")
    paket=input("Paket 1/2/3:")
    kelas=input("Kelas:")
    asal_sekolah=input("Asal Sekolah:")
    no_hp=input("Nomer HP:")
    data=[nama,alamat,paket,kelas,asal_sekolah,no_hp]
    member_smp.add(data)
elif(menu2==2):
    id_member=input("No Member:")
    nama=input('Nama:')
    alamat=input('Alamat:')
    paket=input('Paket 1/2/3:')
    kelas=input("Kelas:")
    asal_sekolah=input("Asal Sekolah:")
    no_hp=input("Nomer HP:")
    data=[nama,alamat,paket,kelas,asal_sekolah,no_hp,id_member]
    member_smp.edit(data)
elif (menu2==3):
    id_member=input('No. member:')
    data=[id_member]
    confirm=input('Yakin menghapus member ini?[y/n]')
    if(confirm=="y"):
        member_smp.delete(data)
    else:
        print('Data batal di hapus')
elif (menu2==4):
    member_smp.show()

else:
    print('Menu tidak tersedia')

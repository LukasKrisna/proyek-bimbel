import mysql.connector
import connect

db = connect.koneksi()

#menambahkan data
def add(data):
    cursor = db.cursor()
    sql="""INSERT INTO member (nama,alamat,paket,kelas,asal_sekolah,no_hp) VALUES (%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data member berhasil ditambahkan!'.format(cursor.rowcount))

#menaampilkan seluruh data
def show():
    cursor=db.cursor()
    sql="""SELECT*FROM member"""
    cursor.execute(sql)
    result=cursor.fetchall()
    print("|---|-------------------------------------------|---------------------------------------|-----------|-------|-----------------------------------|------------------|")
    print("|ID |Nama\t\t\t\t\t|Alamat\t\t\t\t\t|Paket\t    |Kelas  |Asal Sekolah\t\t\t|Nomer Hp\t\t")
    print("|---|-------------------------------------------|---------------------------------------|-----------|-------|-----------------------------------|------------------|")
    for data in result:
        print("|",data[0],"|",data[1],"\t\t\t|",data[2],"\t\t\t\t|",data[3],"\t\t|",data[4],"\t|",data[5],"\t\t\t|",data[6])
        print("|---|-------------------------------------------|---------------------------------------|-----------|-------|-----------------------------------|------------------|")

#mengubah data dalam tabel
def edit(data):
    cursor = db.cursor()
    sql="""UPDATE member SET nama=%s,alamat=%s,paket=%s,kelas=%s,asal_sekolah=%s,no_hp=%s WHERE id=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data member berhasil dirubah!'.format(cursor.rowcount))

#meghapus data dari tabel member
def delete(data):
    cursor=db.cursor()
    sql="""DELETE FROM member WHERE id=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data member berhasil dihapus!'.format(cursor.rowcount))

    

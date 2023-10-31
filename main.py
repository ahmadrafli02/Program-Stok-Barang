import os
import mysql.connector

if __name__ == "__main__":
   os.system("cls")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_barang"
)

mycursor = mydb.cursor()


def tampilkan_barang():
    sql = "SELECT * FROM tbl_barang"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print ("======================")
    for data in result :
        print("1. ID Barang : ",data[0])
        print("2. Nama Barang : ",data[1])
        print("3. Harga Barang : ",data[2])
        print("4. Stok Barang : ",data[3])
        print ("======================")

def tambah_barang():
    id = int(input("Masukkan Id : "))
    nama = str(input("Masukkan Nama Barang : "))
    harga = int(input("Masukkan Harga Barang : "))
    stok = int(input("Masukkan Stok Barang : "))

    sql = "INSERT INTO tbl_barang (id, nama, harga, stok ) VALUES (%s, %s, %s, %s)"
    val = (id, nama, harga, stok)
    mycursor.execute(sql, val)

    mydb.commit()

    print ("Data berhasil ditambahkan!")

def update_barang():
    id = int(input("Masukan Id Barang Yang Ingin Di Update : "))
    sql= "SELECT id FROM tbl_barang WHERE id = '%s'"
    val = [id]
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    for data in result :
        dataa = data
        print("Update Barang ID ",dataa)
        nama = str(input("Masukkan Nama Barang : "))
        harga = int(input("Masukkan Harga Barang : "))
        stok = int(input("Masukkan Stok Barang : "))
        sql = "UPDATE tbl_barang SET nama = %s, harga = %s, stok = %s WHERE id = '%s'"
        val = (nama, harga, stok, id)
        mycursor.execute(sql, val)

        mydb.commit()

        print("Data berhasil diupdate!")

def hapus_barang():
    id = int(input("Masukkan Id Barang Yang Akan DiHapus : "))
    sql = "DELETE FROM tbl_barang WHERE id = '%s' "
    val = [id]
    mycursor.execute(sql, val)

    mydb.commit()

    print("Data berhasil dihapus!")
    

while True:
    print ("===================")
    print ("PROGRAM STOK BARANG")
    print ("===================\n")

    print ("1. Tampilkan Barang")
    print ("2. Tambah Barang")
    print ("3. Update Barang")
    print ("4. Hapus Barang\n")

    pilih = int(input("Pilih Menu : "))

    if pilih == 1 :
        tampilkan_barang()

    elif pilih == 2 :
        tambah_barang()
    
    elif pilih == 3 :
        update_barang()
    
    elif pilih == 4 :
        hapus_barang()

    done = str(input("Apakah anda ingin menggunakan program ini lagi (y/n) ? : "))
    if done == "n" or done == "N" :
        break
print("Terima Kasih telah menggunakan Program ini!")



















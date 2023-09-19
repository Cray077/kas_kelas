import sqlite3
import datetime

conn = sqlite3.connect("kas_kelas.db")
cur = conn.cursor()
#########################################
# TO-DO
# Delete
# Edit
# Outcome
############## SQL CODE #################

################ SQL KAS #########################


def create_table():
  cur.execute('''
    CREATE TABLE IF NOT EXISTS kas_table (
    id INTEGER PRIMARY KEY,
    nama TEXT NOT NULL,
    jumlah_kas INTEGER NOT NULL
    );''')
  conn.commit()


def tambah_siswa(id_siswa, nama, jumlah_kas):
  cur.execute("INSERT INTO kas_table (id, nama, jumlah_kas) VALUES (?,?,?)",
              (id_siswa, nama, jumlah_kas))
  print("Added", id_siswa, nama, jumlah_kas)
  conn.commit()


def update_kas(id, jumlah_kas):
  cur.execute("UPDATE kas_table SET jumlah_kas = ? WHERE id = ?",
              (jumlah_kas, id))
  print("Updated")
  conn.commit()


def edit_nama(id, nama_baru):
  cur.execute("UPDATE kas_table SET nama = ? WHERE id = ?", (nama_baru, id))
  print("Edited")
  conn.commit()


def delete_data(id):
  cur.execute("DELETE FROM kas_table WHERE id = ?", (id, ))
  print("Deleted")
  conn.commit()


def rearrange_id(list_nama):
  id = 1
  for x in list_nama:
    nama = x[1]
    print(id, nama)
    cur.execute("UPDATE kas_table SET id = ? WHERE nama = ?", (id, nama))
    id += 1
  conn.commit()
  print("Rearranged")


def get_list_kas():
  cur.execute("SELECT * FROM kas_table")
  return cur.fetchall()


###################### SQL PENGELUARAN(OUTPUT) #############################


def create_table_pengeluaran():
  cur.execute('''
    CREATE TABLE IF NOT EXISTS pengeluaran_table (
    id_pengeluaran INTEGER PRIMARY KEY AUTOINCREMENT,
    hari INTEGER NOT NULL,
    bulan INTEGER NOT NULL,
    tahun INTEGER NOT NULL,
    keperluan TEXT NOT NULL,
    biaya INT NOT NULL,
    deskripsi TEXT
    );''')
  conn.commit()


def tambah_pengeluaran(keperluan, biaya, deskripsi):
  time = str(datetime.date.today())
  tanggal = time.split("-")
  tahun, bulan, hari = tanggal
  cur.execute(
      """INSERT INTO pengeluaran_table (hari, bulan, tahun, keperluan, biaya, deskripsi)
      VALUES (?,?,?,?,?,?)""",
      (hari, bulan, tahun, keperluan, biaya, deskripsi))
  conn.commit()


def list_pengeluaran():
  cur.execute("SELECT * FROM pengeluaran_table")
  pengeluaran = cur.fetchall()
  for x in pengeluaran:
    print(x[0], x[1], x[2], x[3], x[4], x[5], x[6])


def edit_keperluan_pengeluaran(id, keperluan):
  cur.execute(
      "UPDATE pengeluaran_table SET keperluan = ? WHERE id_pengeluaran = ?",
      (keperluan, id))
  print("Edited")
  conn.commit()


def edit_deskripsi_pengeluaran(id, deskripsi):
  cur.execute(
      "UPDATE pengeluaran_table SET deskripsi = ? WHERE id_pengeluaran = ?",
      (deskripsi, id))
  print("Edited")
  conn.commit()


def edit_biaya_pengeluaran(id, biaya):
  cur.execute(
      "UPDATE pengeluaran_table SET biaya = ? WHERE id_pengeluaran = ?",
      (biaya, id))
  print("Edited")
  conn.commit()


def delete_pengeluaran(id):
  cur.execute("DELETE FROM pengeluaran_table WHERE id_pengeluaran = ?", (id, ))
  print("Deleted")
  conn.commit()


############### Python Code #######################
create_table()
create_table_pengeluaran()


def list_nama(list_kas):
  print("ID", "Nama", "Kas")
  for x in list_kas:
    print(x[0], x[1], x[2])


def get_total_kas():
  pass


def main_menu_kas():

  try:
    get_list_kas()
  except sqlite3.OperationalError:
    print("No Table")

  command = ""

  while command != "0":
    list_kas = get_list_kas()

    print("""
    0 Exit
    1 Tambah Kas
    2 Tambah Siswa
    3 List Nama
    4 Hapus Nama
    5 Edit Nama
    6 Atur Ulang ID
    """)

    command = input("Enter Command: ")

    if command == "1":  #Tambah Kas
      list_nama(list_kas)
      nomor = int(input("Nomor: "))
      jumlah_kas = int(input("Kas: "))
      jumlah = list_kas[nomor - 1][2] + jumlah_kas
      update_kas(nomor, jumlah)
      print(jumlah)

    elif command == "2":  #Tambah Siswa
      nomor = int(input("Nomor: "))
      nama = input("Nama: ")
      kas = 0
      tambah_siswa(nomor, nama, kas)

    elif command == "3":  # List nama
      list_nama(get_list_kas())

    elif command == "4":  # Hapus Nama
      list_nama(list_kas)
      nomor = int(input("Nomor yang akan dihapus: "))
      delete_data(nomor)

    elif command == "5":  # Edit nama
      nomor = int(input("Nomor yang akan diedit: "))
      nama_baru = input("Nama baru: ")
      edit_nama(nomor, nama_baru)

    elif command == "6":  # Atur ulang ID / Reset ID
      rearrange_id(list_kas)


def main_menu_pengeluaran():
  command = ""
  while command != "0":
    print("""
    0 Exit
    1 Tambah Pengeluaran
    2 Daftar Pengeluaran
    3 Ubah Pengeluaran
    4 Hapus Pengeluaran
    """)

    command = input("Enter Command: ")
    if command == "1":  #Tambah Pengeluaran
      keperluan = input("Keperluan: ")
      biaya = input("Biaya: ")
      deskripsi = input("Deskripsi: ")
      tambah_pengeluaran(keperluan, biaya, deskripsi)

    elif command == "2":  #Daftar Pengeluaran
      list_pengeluaran()

    elif command == "3":
      print("Apa yang diubah ?")
      print("""
      1. keperluan
      2. biaya
      3. deskripsi
      """)
      pilih = int(input(">>: "))
      list_pengeluaran()
      if pilih == 1:
        nomor = int(input("id: "))
        keperluan = int(input("Keperluan: "))
        edit_keperluan_pengeluaran(nomor, keperluan)
      elif pilih == 2:
        nomor = int(input("id: "))
        biaya = int(input("Biaya: "))
        edit_biaya_pengeluaran(nomor, biaya)

      elif pilih == 3:
        nomor = int(input("id: "))
        deskripsi = int(input("Deskripsi: "))
        edit_deskripsi_pengeluaran(nomor, deskripsi)

    elif command == "4":
      list_pengeluaran()
      nomor = int(input("id: "))
      delete_pengeluaran(nomor)


def auto_add():
  list_nama_siswa = [
      "ADITYA GALANG SAPUTRA",
      "AHMAD ARIFIN",
      "AHMAD FARIST HABIBI",
      "ALVINA MAULIDIA",
      "ARISMA AULIA BELLA",
      "BERNANDO SYAHPUTRA WIJAYA",
      "DHAVA NADYKA ALGAMA",
      "DIRGA OLIVIO DANY PEDROSA",
      "DIRGA PAS YA CAHYONO",
      "I PUTU RAKA ABHISAR DANENDRA",
      "ILHAM DANUARTA ATMAJA",
      "IRFAN MAULANA PRADITYA",
      "IZZATH HAYDEN DIO",
      "JANSEN NADIKA PRATAMA",
      "LILI NUR INDAH SARI",
      "M.GIBRAN FIRDAUS",
      "MOCH. REZA ARDIANSYAH",
      "MOCHAMAD FAREL REVANZA ADRIANO",
      "MOCHAMAD YONGKY PUTRA ENDYLYONE",
      "MOHAMMAD YUDHA ANDRIANSYAH",
      "MUAMMAR KADAFI",
      "MUHAMAD IMRON HABIBI",
      "MUHAMAD SYAMSUDIN ROMDHANI",
      "MUHAMMAD ADITYA IMANSYAH",
      "MUHAMMAD AHTUR DAVARA",
      "MUHAMMAD HABIB ZAMZAMY",
      "MUHAMMAD RIZAL MAULANA",
      "NABILA AULIA PUTRI",
      "RAHMAT DINO SAPUTRA",
      "RAZZANATHA DWI UTAMA",
      "RIZAL ANINDHITA MURDIAWAN",
      "RIZKI MUHAMMAD HERLAMBANG",
      "SALIS PUJI NUGROHO",
      "SHOLIHUL HADZIQ IHDA",
      "SILVIA ANGEL APRILIANA",
      "SITI LAILATUL KHUSNA",
      "SONI IRAWAN",
      "YOSI SAPUTRA",
      "YUSUFA FARIZ ZAHRO'I",
  ]
  nomor_absen = 1
  for x in list_nama_siswa:
    tambah_siswa(nomor_absen, x, 0)
    nomor_absen += 1


def main():
  print("""
  1. KAS
  2. PENGELUARAN
  """)
  pilih = int(input(">>>: "))
  if pilih == 1:
    main_menu_kas()
  elif pilih == 2:
    main_menu_pengeluaran()
  elif pilih == 3:
    auto_add()


main()
###########################################

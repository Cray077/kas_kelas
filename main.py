import sqlite3

conn = sqlite3.connect("kas_kelas.db")
cur = conn.cursor()

############## SQL CODE #################


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


def get_list_kas():
  cur.execute("SELECT * FROM kas_table")
  return cur.fetchall()


###################################################

############### Python Code #######################
try:
  list_kas = get_list_kas()
except sqlite3.OperationalError:
  print("No Table")

  


def list_nama():
  list_kas = get_list_kas()
  for x in list_kas:
    print(x[0], x[1], x[2])


def tambah_kas(nomor, jumlah_kas):
  jumlah = list_kas[nomor - 1][2] + jumlah_kas
  update_kas(nomor, jumlah)
  print(jumlah)


def main():
  command = ""

  while command != "0":
    command = input("Enter Command: ")

    if command == "1":
      list_nama()
      nomor = int(input("Nomor: "))
      jumlah_kas = int(input("Kas: "))
      tambah_kas(nomor, jumlah_kas)

    elif command == "2":
      nomor = int(input("Nomor: "))
      nama = input("Nama: ")
      kas = 0
      tambah_siswa(nomor, nama, kas)
    elif command == "3":
      list_nama()


def auto_add():
  list_nama = [
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
  for x in list_nama:
    tambah_siswa(nomor_absen, x, 0)
    nomor_absen += 1


###########################################
create_table()
#auto_add()
main()

from process import Process
from view import View

proses = Process()
view = View()

while True:
    print("\n=== MENU UTAMA ===")
    print("1. Tambah Data")
    print("2. Tampilkan Semua Data")
    print("3. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        try:
            nama = input("Masukkan nama mahasiswa : ")
            nilai = input("Masukkan nilai         : ")
            proses.tambah(nama, nilai)
            print("✔ Data berhasil ditambahkan!")
        except Exception as e:
            print(f"✖ Error: {e}")

    elif pilih == "2":
        view.tampilkan(proses.get_all())

    elif pilih == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
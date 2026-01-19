from data import Mahasiswa

class Process:
    def _init_(self):
        self.database = []

    def tambah(self, nama, nilai):
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong!")

        try:
            nilai = float(nilai)
        except:
            raise ValueError("Nilai harus berupa angka!")

        if nilai < 0 or nilai > 100:
            raise ValueError("Nilai harus antara 0–100!")

        self.database.append(Mahasiswa(nama, nilai))

    def get_all(self):
        return self.database
class View:
    def tampilkan(self, data):
        print("\n=== TABEL DATA MAHASISWA ===")
        print(f"{'No':<4}{'Nama':<20}{'Nilai':<10}")
        print("-" * 36)

        for i, mhs in enumerate(data, 1):
            print(f"{i:<4}{mhs.nama:<20}{mhs.nilai:<10}")

        print("-" * 36)
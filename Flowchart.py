# Inisialisasi nilai terbesar
terbesar = float('-inf')  # Nilai awal untuk perbandingan

while True:
    N = float(input("Masukkan bilangan (masukkan 0 untuk selesai): "))
    
    # Jika N adalah 0, keluarkan bilangan terbesar dan akhiri program
    if N == 0:
        if terbesar == float('-inf'):
            print("Tidak ada bilangan yang dimasukkan.")
        else:
            print(f"Bilangan terbesar adalah: {terbesar}")
        break
    
    # Bandingkan N dengan nilai terbesar saat ini
    if N > terbesar:
        terbesar = N

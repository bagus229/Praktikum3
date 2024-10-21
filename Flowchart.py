# Input tiga bilangan
A = float(input("Masukkan bilangan A: "))
B = float(input("Masukkan bilangan B: "))
C = float(input("Masukkan bilangan C: "))
# Bandingkan bilangan A dan B
if A > B:
    # Jika A > B, bandingkan A dengan C
    if A > C:
        print(f"Output: Bilangan terbesar adalah A = {A}")
    else:
        print(f"Output: Bilangan terbesar adalah C = {C}")
else:
    # Jika B >= A, bandingkan B dengan C
    if B > C:
        print(f"Output: Bilangan terbesar adalah B = {B}")
    else:
        print(f"Output: Bilangan terbesar adalah C = {C}")


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

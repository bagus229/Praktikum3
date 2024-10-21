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
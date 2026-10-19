
# Praktik: Analisis Nilai Mahasiswa

def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    hasil = []
    for x in data:
        if x >= batas:
            hasil.append(x)
    return hasil

# Batas kelulusan adalah nilai minimal 60
# Data nilai 10 mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Mengambil daftar nilai yang lulus
lulus = nilai_lulus(nilai)



print(f"Data nilai       : {nilai}")
print(f"Banyak data      : {len(nilai)}")
print(f"Total nilai      : {sum(nilai)}")
print(f"Rata-rata        : {rata_rata(nilai):.2f}")
print(f"Nilai minimum    : {min(nilai)}")
print(f"Nilai maksimum   : {max(nilai)}")
print(f"Daftar nilai lulus: {lulus}")
print(f"Jumlah lulus     : {len(lulus)}")
print(f"Belum lulus      : {len(nilai) - len(lulus)}")

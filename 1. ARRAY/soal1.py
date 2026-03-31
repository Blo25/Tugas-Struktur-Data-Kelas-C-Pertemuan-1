import statistics  # untuk mean (rata-rata)
import matplotlib.pyplot as plt


nilai = []
for i in range (10):
    n = int(input(f"Masukkan Nilai ke-{i+1} : "))
    nilai.append(n)

nt = max(nilai)
nte = min(nilai)
rr = sum(nilai) / len(nilai)

l = 0
tl = 0

for n in nilai:
    if n >=60:
        l +=1
    else:
        tl +=1
        
print("\nHasil Analisis Nilai")
print("Nilai Tertinggi : ", nt)
print("Nilai Terendah : ", nte)
print("Nilai Rata-Rata : ", rr)
print("Jumlah Lulus : ", l)
print("Jumlah Tidak Lulus : ", tl)

plt.figure(figsize=(8, 5))

kategori = ['Terendah', 'Rata-rata', 'Tertinggi']
nilai_grafik = [nte, rr, nt]

bars = plt.bar(kategori, nilai_grafik, color=["#FC0303", "#73FF00", "#0011FF"])
plt.ylim(0, 100)
plt.title('Ringkasan Nilai Kelas (Min - Avg - Max)', fontsize=14)
plt.ylabel('Nilai')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1.5, f'{yval:.1f}',
             ha='center', va='bottom', fontsize=11)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

plt.figure(figsize=(5,4))
plt.pie([l, tl], labels=["Lulus", "Tidak Lulus"], autopct="%1.1f%%", colors=["blue","orange"])
plt.title("Persentase Kelulusan Mahasiswa")
plt.show()
#belajar operator aritmatika

nama_karyawan = input("masukkan nama karyawan :")
banyak_anak = int(input("masukkan banyak anak :"))
gaji_pokok = int(input("masukkan gaji pokok :"))

Tunjangan_istri = 20/100
Tunjangan_anak = 5/100
pajak = 10/100


tunjangan_istri = gaji_pokok * 20/100
tunjangan_anak  = gaji_pokok * 5/100
total_tunjangan = tunjangan_istri + (tunjangan_anak)
gaji_kotor = gaji_pokok + total_tunjangan
pajak = gaji_kotor * 10/100
gaji_bersih = gaji_kotor - pajak


print("tunjangan_istri:",tunjangan_istri)
print("tunjangan/anak :",tunjangan_anak)
print("total_tunjangan:",total_tunjangan)
print("gaji_kotor     :",gaji_kotor)
print("pajak 10%      :",pajak)
print("gaji_bersih    :",gaji_bersih)

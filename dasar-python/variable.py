# Variable
# variable digunakan untuk menampung nilai.
# nilai di sini bisa kata,angka,pecahan,ataupun bolean.
# kata,angka,pecahan,dan juga bolean disebut sebagai tipe data.berikut adalah tipe data pada python :

# -string : digunakan untuk menampung huruf,kata,dan kalimat.
# contoh penulisan nama = "sandi"

# -integer : adalah tipe data untuk menampung bilangan bulat seeprti 10, dan -10.
# contoh penulisan x = 2

# - Float : digunakan untuk menampung bilangan pecahan seperti 3,14;1,2 dan lain sebagainya.
# contoh penulisan vi = 3,14

# -bolean : adalah tipe data yang berisi benar(false)atau salah(true).
# contoh penulisan pelajar = true

#contoh kode menggunaka variable

nama = "Sandi"
usia = 19
tinggi = 158.5
pelajar = False

print(f"Halo namaku {nama}") # untuk menampilkan variable dalam print()kita harus memasukan f srtelah kurung buka dan menyisipkanya nama variablenya dalam kurung kurawal.
print(f"Usiaku {usia}")
print(f"Tinggi badanku {tinggi}")
#Untuk bolean sendiri jarang dipanggil secara langsung.karenabiasanya itu untuk algoritma pemrograman. Berikut contohnya:
if pelajar == False : #membuat sebuah kondisi
  print("Aku sudah lulus!")#ketika kondisi terpenuhi
else :# jika kondisi tidak terpenuhi
  print("Aku seorang pelajar")
  
  # Kamu bisa mengganti variable pelajar menjadi True dan jalankan lagi programnya.
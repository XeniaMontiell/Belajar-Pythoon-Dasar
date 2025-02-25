# Daftar Minuman
T01 = 'Es Teh'
T02 = 'Es Jeruk'
T03 = 'Es Campur'
T04 = 'Es Teh Lemon'
T05 = 'Espresso'
T06 = 'Mojito'

# Daftar Makanan
S01 = 'Nasi Padang'
S02 = 'Nasi Goreng'
S03 = 'Ayam Bakar'
S04 = 'Ayam Goreng'
S05 = 'Ayam Geprek'
S06 = 'Ayam Penyet'

# Total Harga Makanan dan Minuman
harga_makanan = {
    'Nasi Padang': 25000,
    'Nasi Goreng': 20000,
    'Ayam Bakar': 15000,
    'Ayam Goreng': 18000,
    'Ayam Geprek': 10000,
    'Ayam Penyet': 15000
}

harga_minuman = {
    'Es Teh': 5000,
    'Es Jeruk': 5000,
    'Es Campur': 5000,
    'Es Teh Lemon': 50000,
    'Espresso': 18000,
    'Mojito': 25000
}

print("\nDaftar Menu Makanan:")
for makanan, harga in harga_makanan.items():
    print(f"- {makanan}: Rp {harga}")

print("\nDaftar Menu Minuman:")
for minuman, harga in harga_minuman.items():
    print(f"- {minuman}: Rp {harga}")

# Input pilihan makanan dan minuman
pilihan_makanan = input("\nMasukkan makanan yang dipilih (pisahkan dengan koma jika lebih dari satu): ").split(', ')
pilihan_minuman = input("Masukkan minuman yang dipilih (pisahkan dengan koma jika lebih dari satu): ").split(', ')

# Menentukan harga total
total_harga = 0

print("\nAnda memilih:")
print("Makanan:")
for makanan in pilihan_makanan:
    if makanan in harga_makanan:
        print(f"- {makanan}: Rp {harga_makanan[makanan]}")
        total_harga += harga_makanan[makanan]
    else:
        print(f"- {makanan}: Tidak tersedia")

print("\nMinuman:")
for minuman in pilihan_minuman:
    if minuman in harga_minuman:
        print(f"- {minuman}: Rp {harga_minuman[minuman]}")
        total_harga += harga_minuman[minuman]
    else:
        print(f"- {minuman}: Tidak tersedia")

konfirmasi = input("\nApakah pilihan sudah sesuai? (ya/tidak): ")
if konfirmasi.lower() == 'ya':
    print("Total yang harus dibayar: Rp", total_harga)
else:
    print("Silakan input ulang pesanan Anda.")

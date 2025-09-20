# Program: Ayo Beli Kopi ke Kantin (Versi Antrian Harian)
# By: Dhinoa 😎☕

import datetime
import os

# File penyimpan tanggal & antrian
file_antrian = "antrian.txt"

# Cek apakah ada file antrian dari hari sebelumnya
today = datetime.date.today().strftime("%Y-%m-%d")
nomor_antrian = 1

if os.path.exists(file_antrian):
    with open(file_antrian, "r") as f:
        data = f.read().strip().split("|")
        if len(data) == 2 and data[0] == today:
            nomor_antrian = int(data[1]) + 1  # lanjut dari nomor terakhir hari ini

def simpan_antrian(nomor):
    with open(file_antrian, "w") as f:
        f.write(f"{today}|{nomor}")

def tampilkan_menu():
    print("=== Selamat Datang di Kantin Kopi Kampus ===")
    print("Menu Kopi Hari Ini:")
    print("1. Kopi Hitam ........ Rp 5.000")
    print("2. Cappuccino ........ Rp 10.000")
    print("3. Kopi Susu ......... Rp 8.000")
    print("4. Es Kopi Kekinian .. Rp 12.000")
    print("===========================================")

def beli_kopi():
    menu = {
        1: ("Kopi Hitam", 5000),
        2: ("Cappuccino", 10000),
        3: ("Kopi Susu", 8000),
        4: ("Es Kopi Kekinian", 12000)
    }

    keranjang = []

    while True:
        tampilkan_menu()
        pilihan = input("Pilih nomor kopi (atau ketik 'selesai'): ")

        if pilihan.lower() == "selesai":
            break

        try:
            pilihan = int(pilihan)
            if pilihan in menu:
                nama, harga = menu[pilihan]
                jumlah = int(input(f"Berapa gelas {nama}? "))
                total = harga * jumlah
                keranjang.append((nama, jumlah, total))
                print(f"✅ {jumlah} gelas {nama} masuk ke keranjang!\n")
            else:
                print("❌ Pilihan tidak ada di menu.\n")
        except ValueError:
            print("⚠️ Input salah, coba lagi.\n")

    return keranjang

def hitung_total(keranjang):
    global nomor_antrian
    print("\n=== Struk Pembelian Kopi ===")
    print("Tanggal:", datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

    grand_total = 0
    for item in keranjang:
        nama, jumlah, total = item
        print(f"{nama} x{jumlah} = Rp {total}")
        grand_total += total

    # Terapkan diskon mahasiswa
    diskon = 0
    if grand_total > 30000:
        diskon = int(grand_total * 0.1)
        print(f"Diskon Mahasiswa 10% = -Rp {diskon}")

    total_bayar = grand_total - diskon
    print("-----------------------------")
    print(f"Total Bayar: Rp {total_bayar}")

    # Pilih metode pembayaran
    print("\n=== Pilih Metode Pembayaran ===")
    print("1. Cash")
    print("2. QRIS")
    print("3. E-Wallet")
    metode = input("Masukkan nomor metode pembayaran: ")

    metode_dict = {
        "1": "Cash",
        "2": "QRIS",
        "3": "E-Wallet"
    }

    metode_pembayaran = metode_dict.get(metode, "Cash")  # default Cash kalau salah input
    print(f"\n💳 Pembayaran menggunakan: {metode_pembayaran}")

    # Cetak nomor antrian
    print(f"\n📢 Nomor Antrian Anda: {nomor_antrian}")
    print("Silakan tunggu, pesanan sedang diproses... ☕")

    # Simpan nomor antrian terakhir ke file
    simpan_antrian(nomor_antrian)
    nomor_antrian += 1

    print("\nTerima kasih sudah beli kopi di kantin! 🙏")

# Main program
keranjang = beli_kopi()
if keranjang:
    hitung_total(keranjang)
else:
    print("Kamu belum beli kopi. Yuk balik lagi nanti! 😉")

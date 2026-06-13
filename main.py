import time
import sys
from xmlrpc.client import DateTime


def efek_mengetik(teks, jeda=0.03):
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(jeda)
    print()

def tampilkan_layar_pembuka():
    print("\n" + "=" * 60)
    efek_mengetik("Selamat datang di program Mini Test")
    print("=" * 60)
    time.sleep(1.0)
    profil = (
        "\n>> Mini Test ini dikerjakan oleh,\n"
        "Nama                 : Rifqi Haikal Chairiansyah\n"
        "Posisi yang Dilamar  : Junior Software Developer\n"
        "Tanggal Pengerjaan   : 13 Juni 2026\n"
    )
    efek_mengetik(profil, jeda=0.01)
    time.sleep(0.5)

    instruksi = (
        "\n>> INSTRUKSI PENGGUNAAN:\n"
        "1. Sistem akan meminta Anda memasukkan sebuah angka batas atas.\n"
        "2. Sistem akan membuat deret angka menurun dari batas tersebut hingga 1.\n"
        "3. Bilangan prima akan dihilangkan dari deret.\n"
        "4. Kelipatan 3 menjadi 'Foo', kelipatan 5 menjadi 'Bar', keduanya menjadi 'FooBar'.\n"
    )
    efek_mengetik(instruksi, jeda=0.01)

    input("\n[ Tekan 'ENTER' untuk memulai program ] ")

def cek_bilangan_prima(angka):
    if angka <= 1:
        return False
    if angka <= 3:
        return True
    if angka % 2 == 0 or angka % 3 == 0:
        return False

    pembagi = 5
    while pembagi * pembagi <= angka:
        if angka % pembagi == 0 or angka % (pembagi + 2) == 0:
            return False
        pembagi += 6

    return True

def terjemahkan_angka(angka):
    if cek_bilangan_prima(angka):
        return None

    hasil_teks = ""
    if angka % 3 == 0:
        hasil_teks += "Foo"
    if angka % 5 == 0:
        hasil_teks += "Bar"

    return hasil_teks if hasil_teks else str(angka)

def proses_dan_analisis_deret(batas_atas):
    deret_asli = list(range(1, batas_atas + 1))
    kumpulan_output = []

    statistik = {
        "total_prima_dihapus": 0,
        "total_foo": 0,
        "total_bar": 0,
        "total_foobar": 0,
        "total_angka_biasa": 0
    }

    for angka in reversed(deret_asli):
        hasil_terjemahan = terjemahkan_angka(angka)

        if hasil_terjemahan is None:
            statistik["total_prima_dihapus"] += 1
        else:
            kumpulan_output.append(hasil_terjemahan)

            if hasil_terjemahan == "FooBar":
                statistik["total_foobar"] += 1
            elif hasil_terjemahan == "Foo":
                statistik["total_foo"] += 1
            elif hasil_terjemahan == "Bar":
                statistik["total_bar"] += 1
            else:
                statistik["total_angka_biasa"] += 1

    return ", ".join(kumpulan_output), statistik

def jalankan_program():
    tampilkan_layar_pembuka()
    print("\nJika kamu ingin berhenti, ketik 'keluar' untuk tutup\n")
    while True:
        print("-" * 60)
        input_user = input("\nMasukkan batas maksimal angka : ").strip()

        if input_user.lower() in ['keluar', 'exit', 'quit']:
            efek_mengetik("\nMematikan sistem... Terima kasih telah mencoba Mini Test ini!")
            break

        if not input_user.isdigit() or int(input_user) <= 0:
            print("Peringatan: Harap masukkan angka bilangan bulat positif!")
            continue

        batas_atas = int(input_user)

        efek_mengetik("\nMemproses kalkulasi...", jeda=0.02)
        hasil_akhir, data_statistik = proses_dan_analisis_deret(batas_atas)

        print("\n>> HASIL OUTPUT:")
        print(hasil_akhir)
        print("\n" + "-" * 60)

        while True:
            opsi_lanjutan = input(
                "Pilih aksi: \n[1] Penjelasan Output \n[2] Input Angka Baru \n[3] Keluar\n"
                "Pilihan Anda (1/2/3): "
            ).strip()

            if opsi_lanjutan == '1':
                print("\n>> PENJELASAN ANALITIK OUTPUT:")
                penjelasan = (
                    f"Dari pemrosesan deret angka 1 hingga {batas_atas}, sistem melakukan tindakan berikut:\n"
                    f"- Menghapus {data_statistik['total_prima_dihapus']} bilangan prima.\n"
                    f"- Mengubah {data_statistik['total_foobar']} angka menjadi 'FooBar' (Kelipatan 3 & 5).\n"
                    f"- Mengubah {data_statistik['total_foo']} angka menjadi 'Foo' (Kelipatan 3).\n"
                    f"- Mengubah {data_statistik['total_bar']} angka menjadi 'Bar' (Kelipatan 5).\n"
                    f"- Menyisakan {data_statistik['total_angka_biasa']} angka biasa."
                )
                efek_mengetik(penjelasan, jeda=0.01)
                print("\n" + "-" * 60)
            elif opsi_lanjutan == '2':
                break
            elif opsi_lanjutan == '3':
                efek_mengetik("\nMematikan sistem... Terima kasih sudah mencoba Mini Test ini!")
                sys.exit()
            else:
                print("Opsi tidak valid. Silakan pilih 1, 2, atau 3.")

if __name__ == "__main__":
    try:
        jalankan_program()
    except KeyboardInterrupt:
        print("\n\nSistem dihentikan secara paksa. Terima kasih sudah mencoba Mini Test ini!")
        sys.exit()
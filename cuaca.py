import os
import requests
import time
import sys
from datetime import datetime
from collections import defaultdict
from dotenv import load_dotenv

load_dotenv()

def efek_mengetik(teks, jeda=0.03):
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(jeda)
    print()

def tampilkan_layar_pembuka():
    print("\n" + "=" * 65)
    efek_mengetik("Selamat datang di Mini Test", jeda=0.01)
    print("=" * 65)
    time.sleep(1.0)

    profil = (
        "\n>> Mini Test ini dikerjakan oleh,\n"
        "Nama                 : Rifqi Haikal Chairiansyah\n"
        "Posisi yang Dilamar  : Junior Software Developer\n"
        "Tanggal Pengerjaan   : 13 Juni 2026\n"
    )
    efek_mengetik(profil, jeda=0.01)
    time.sleep(0.3)

    instruksi = (
        ">> INSTRUKSI PENGGUNAAN:\n"
        "1. Sistem akan meminta Anda memasukkan nama kota target.\n"
        "2. Sistem akan melacak titik koordinat (Latitude/Longitude) kota tersebut.\n"
        "3. Sistem akan menarik data cuaca 5 hari ke depan dan menghitung suhu rata-rata hariannya.\n"
    )
    efek_mengetik(instruksi, jeda=0.01)

    input("\n[ Tekan 'ENTER' untuk memulai program utama ] ")

def dapatkan_koordinat_kota(nama_kota):
    kunci_api = os.getenv("OPENWEATHER_API_KEY")
    url_geo = f"http://api.openweathermap.org/geo/1.0/direct?q={nama_kota}&limit=1&appid={kunci_api}"

    try:
        respons = requests.get(url_geo)
        respons.raise_for_status()
        data = respons.json()

        if not data:
            return None, None, f"Kota '{nama_kota}' tidak ditemukan di database."

        return data[0]['lat'], data[0]['lon'], None
    except requests.exceptions.HTTPError as err:
        if respons.status_code == 401:
            return None, None, "Akses Ditolak (401): API Key belum aktif. Harap tunggu proses propagasi."
        return None, None, f"Gagal menghubungi server geocoding: {err}"
    except Exception as e:
        return None, None, f"Terjadi kesalahan sistem: {e}"

def ambil_data_cuaca(lat, lon):
    kunci_api = os.getenv("OPENWEATHER_API_KEY")
    url_cuaca = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={kunci_api}&units=metric"

    try:
        respons = requests.get(url_cuaca)
        respons.raise_for_status()
        return respons.json(), None
    except requests.exceptions.HTTPError as err:
        return None, f"Gagal mengambil data cuaca satelit: {err}"
    except Exception as e:
        return None, f"Terjadi kesalahan sistem: {e}"

def proses_dan_analisis_cuaca(data_mentah_json):
    suhu_harian = defaultdict(list)

    for item in data_mentah_json['list']:
        waktu_lokal = datetime.fromtimestamp(item['dt'])
        tanggal_teks = waktu_lokal.strftime("%a, %d %b %Y")
        suhu_harian[tanggal_teks].append(item['main']['temp'])

    hasil_output = []
    total_data_diproses = len(data_mentah_json['list'])
    suhu_tertinggi = -999
    suhu_terendah = 999

    hitungan_hari = 0
    for tanggal, daftar_suhu in suhu_harian.items():
        if hitungan_hari >= 5:
            break

        suhu_rata_rata = sum(daftar_suhu) / len(daftar_suhu)
        hasil_output.append(f"{tanggal}: {suhu_rata_rata:.2f}°C")

        maks_hari_ini = max(daftar_suhu)
        min_hari_ini = min(daftar_suhu)
        if maks_hari_ini > suhu_tertinggi: suhu_tertinggi = maks_hari_ini
        if min_hari_ini < suhu_terendah: suhu_terendah = min_hari_ini

        hitungan_hari += 1

    data_analitik = {
        "total_titik_data": total_data_diproses,
        "suhu_tertinggi": suhu_tertinggi,
        "suhu_terendah": suhu_terendah
    }

    return "\n".join(hasil_output), data_analitik

def jalankan_aplikasi():
    if not os.getenv("OPENWEATHER_API_KEY"):
        print("❌ ERROR KRITIS: File .env tidak ditemukan atau OPENWEATHER_API_KEY kosong!")
        return

    tampilkan_layar_pembuka()
    print("\nJika kamu ingin berhenti, ketik 'keluar' untuk tutup\n")
    while True:
        print("\n" + "=" * 65)
        input_kota = input("Masukkan nama kota target [Tekan ENTER untuk 'Jakarta'] : ").strip()

        if input_kota.lower() in ['keluar', 'exit', 'quit']:
            efek_mengetik("Menutup sesi... Terima kasih telah mencoba Mini Test ini!")
            break

        kota_target = input_kota if input_kota else "Jakarta"

        print(f"\n[1/2] Melacak koordinat untuk '{kota_target}'...")
        lat, lon, error_geo = dapatkan_koordinat_kota(kota_target)

        if error_geo:
            print(f"❌ {error_geo}")
            continue

        print(f"[2/2] Mengunduh data cuaca dari OpenWeatherMap...")
        data_cuaca, error_cuaca = ambil_data_cuaca(lat, lon)

        if error_cuaca:
            print(f"❌ {error_cuaca}")
            continue

        hasil_teks, data_analitik = proses_dan_analisis_cuaca(data_cuaca)

        print("\n>> Weather Forecast:")
        print(hasil_teks)
        print("-" * 65)

        while True:
            opsi = input("\nPilih Aksi: \n[1] Penjelasan Output \n[2] Input Kota Baru \n[3] Keluar\nPilih aksi, ketik (1/2/3): ").strip()

            if opsi == '1':
                print("\n>> PENJELASAN LOGIKA SISTEM & ANALITIK:")
                penjelasan = (
                    f"- Sistem mengunduh total {data_analitik['total_titik_data']} titik data cuaca (interval per 3 jam) dari API gratis.\n"
                    f"- Karena soal mewajibkan 'satu suhu per hari', sistem mengelompokkan data berdasarkan tanggal.\n"
                    f"- Sistem kemudian menghitung nilai rata-rata (mean) dari fluktuasi suhu di hari tersebut.\n"
                    f"- Sebagai catatan metrik: Suhu paling ekstrem yang terdeteksi dalam 5 hari ini mencapai "
                    f"{data_analitik['suhu_tertinggi']:.2f}°C, dan paling dingin mencapai {data_analitik['suhu_terendah']:.2f}°C."
                )
                efek_mengetik(penjelasan, jeda=0.01)
                print("-" * 65)

            elif opsi == '2':
                break

            elif opsi == '3':
                efek_mengetik("\nSistem dimatikan secara manual. Terima kasih telah mencoba Mini Test ini!")
                sys.exit()

            else:
                print("Pilihan tidak valid. Silakan ketik angka 1, 2, atau 3.")

if __name__ == "__main__":
    try:
        jalankan_aplikasi()
    except KeyboardInterrupt:
        print("\n\nSistem diinterupsi paksa oleh pengguna. Mematikan proses...")
        sys.exit()
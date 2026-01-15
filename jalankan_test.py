import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Panggil temannya (Import file lain)
import data_rahasia
from halaman_login import HalamanLogin

# 1. SETUP DRIVER (Mode Incognito)
print("[START] Menyiapkan Robot...")
opsi = webdriver.ChromeOptions()
opsi.add_argument("--incognito")
opsi.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=opsi)

# 2. MULAI TES (Panggil Class dari file sebelah)
# Kita serahkan driver ke 'HalamanLogin' untuk dikendalikan
aksi_login = HalamanLogin(driver)

try:
    # Langkah 1: Buka Web (Ambil URL dari file data)
    aksi_login.buka_website(data_rahasia.URL_WEB)

    # Langkah 2: Login (Ambil User/Pass dari file data)
    aksi_login.isi_username(data_rahasia.USERNAME)
    aksi_login.isi_password(data_rahasia.PASSWORD)
    aksi_login.klik_login()

    # Langkah 3: Cek Hasil
    if aksi_login.validasi_login_sukses():
        # DULU DISINI ADA EMOJI CENTANG, SEKARANG KITA HAPUS
        print("[SUKSES] TES POM BERHASIL: Login masuk dashboard!")
    else:
        print("[GAGAL] TES GAGAL: Tidak masuk dashboard.")

except Exception as e:
    # DULU DISINI ADA EMOJI SILANG, SEKARANG KITA HAPUS
    print(f"[ERROR] Terjadi kesalahan: {e}")

# 3. TUTUP
print("[FINISH] Selesai. Tutup 5 detik lagi.")
time.sleep(5)
driver.quit()
import time
from selenium import webdriver
import data_rahasia
from halaman_login import HalamanLogin

# 1. SETUP
print("[START] Menyiapkan Robot...")
opsi = webdriver.ChromeOptions()
opsi.add_argument("--incognito")
opsi.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=opsi)

aksi = HalamanLogin(driver)

try:
    # --- SKENARIO 1: LOGIN GAGAL (NEGATIVE TEST) ---
    print("\n--- TEST CASE 1: Coba Login Password Ngawur ---")
    aksi.buka_website(data_rahasia.URL_WEB)
    aksi.isi_username("standard_user")
    aksi.isi_password("password_salah_total") # Password ngawur
    aksi.klik_login()
    
    # Validasi Error
    pesan = aksi.cek_pesan_error()
    if "Username and password do not match" in pesan:
        print(f"[SUKSES] Robot mendeteksi error: {pesan}")
    else:
        print(f"[GAGAL] Robot tidak melihat pesan error. Malah dapet: {pesan}")

    # --- SKENARIO 2: LOGIN SUKSES (POSITIVE TEST) ---
    print("\n--- TEST CASE 2: Login Password Benar ---")
    # Refresh halaman dulu biar bersih
    driver.refresh() 
    
    aksi.isi_username(data_rahasia.USERNAME)
    aksi.isi_password(data_rahasia.PASSWORD)
    aksi.klik_login()
    
    if aksi.validasi_login_sukses():
        print("[SUKSES] Berhasil masuk dashboard!")
    else:
        print("[GAGAL] Gagal login yang benar.")

except Exception as e:
    print(f"[ERROR] Terjadi kesalahan: {e}")

print("\n[FINISH] Semua tes selesai. Tutup 5 detik lagi.")
time.sleep(5)
driver.quit()
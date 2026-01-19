from selenium.webdriver.common.by import By
import time

class HalamanLogin:
    
    def __init__(self, driver):
        self.driver = driver

    def buka_website(self, url):
        print(f"[INFO] Membuka: {url}")
        self.driver.get(url)

    def isi_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def isi_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def klik_login(self):
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(1) # Tunggu loading
        print("[INFO] Klik tombol login...")

    def validasi_login_sukses(self):
        try:
            judul = self.driver.find_element(By.CLASS_NAME, "title").text
            if judul == "Products":
                return True
            else:
                return False
        except:
            return False

    def cek_pesan_error(self):
        """Fungsi untuk mengambil teks merah error"""
        try:
            # Cari tulisan error di layar
            teks_error = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
            return teks_error
        except:
            return "Tidak ada error"
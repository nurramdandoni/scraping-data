import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Inisialisasi webdriver Selenium
driver = webdriver.Chrome()

# Daftar User-Agent yang berbeda
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0",
    # Tambahkan User-Agent lain yang ingin Anda gunakan
]

# Fungsi untuk menghasilkan penundaan yang bervariasi
def random_delay():
    delay = random.uniform(1, 3)  # Ganti dengan rentang penundaan yang diinginkan
    time.sleep(delay)
loop = 0
# Buka file CSV untuk menulis data
with open('./out.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['key', 'value', 'img'])  # Tulis header kolom

    # Loop melalui setiap barcode dalam file CSV
    with open('./pd.csv', 'r') as barcode_file:
        reader = csv.reader(barcode_file)
        
        # Lewati header baris pertama jika ada
        next(reader)
        
        # Loop melalui setiap baris dalam file CSV
        for row in reader:
            barcode = row[0]  # Ambil nilai barcode dari kolom pertama
            nama = row[1]  # Ambil nilai nama dari kolom kedua

            # Inisialisasi WebDriver Chrome
            chrome_options = Options()
            chrome_options.add_argument("--headless")  # Jalankan dalam mode headless (tanpa tampilan browser)
            chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")  # Pilih secara acak User-Agent
            driver = webdriver.Chrome(options=chrome_options)

            # URL yang akan dibuka
            url = f'https://www.google.com/search?q={barcode} {nama}&tbm=isch'
            
            # Buka URL menggunakan webdriver
            driver.get(url)
            random_delay()

            # Tangkap layar dan simpan ke file
            screenshot_path = barcode + ".png"  # Tentukan path dan nama file untuk menyimpan screenshot
            driver.save_screenshot(screenshot_path)
            # Tulis data ke file CSV
            writer.writerow([barcode, nama, screenshot_path])
            loop +=1
            print(f"{barcode}: Sukses - {loop} :: {screenshot_path}")

            # Tutup webdriver setelah selesai mengambil gambar
            driver.quit()

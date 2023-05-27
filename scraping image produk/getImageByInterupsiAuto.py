import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Inisialisasi webdriver Selenium
driver = webdriver.Chrome()

# Buka file CSV untuk menulis data
loop = 0
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
            nama = row[1]  # Ambil nilai barcode dari kolom pertama
            
            # Membuat objek opsi Chrome
            chrome_options = Options()
            # Mengatur User-Agent sesuai dengan browser yang digunakan
            chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

            # Inisialisasi webdriver Chrome dengan opsi yang ditentukan
            driver = webdriver.Chrome(options=chrome_options)

            # URL yang akan dibuka
            url = f'https://www.google.com/search?q={barcode} {nama}&tbm=isch'
            # Buka URL menggunakan webdriver
            driver.get(url)
            
            # Tunggu sampai elemen gambar kedua muncul
            wait = WebDriverWait(driver, 3600)
            image_elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img')))
            
            # Periksa apakah ada elemen gambar kedua
            if len(image_elements) > 1:
                # Dapatkan elemen gambar kedua
                image_element = image_elements[1]
                
                # Dapatkan URL gambar dari atribut 'src'
                image_url = image_element.get_attribute('src')
                
                # Cetak URL gambar
                # print(image_url)
                # Tulis barcode dan URL gambar ke file CSV
                writer.writerow([barcode, nama, image_url])
                loop +=1
                print(barcode+": Sukses -"+str(loop))
            else:
                # Dapatkan elemen gambar pertama
                image_element = image_elements[0]
                
                # Dapatkan URL gambar dari atribut 'src'
                image_url = image_element.get_attribute('src')
                writer.writerow([barcode, nama, image_url])
                loop +=1
                print(barcode+": Sukses -"+str(loop))


# Tutup webdriver
driver.quit()

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Inisialisasi webdriver Selenium
driver = webdriver.Chrome()  # Ganti dengan driver sesuai dengan browser yang Anda gunakan (misalnya Firefox)

# # URL yang akan dibuka
# url = 'https://www.google.com/search?q=8991002122000&tbm=isch'
# # Buka URL menggunakan webdriver
# driver.get(url)

# Ambil tangkapan layar dari halaman web
# screenshot_path = 'screenshot.png'
# driver.save_screenshot(screenshot_path)


# Buka file CSV untuk menulis data
loop = 0
with open('./out.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['key', 'value', 'img'])  # Tulis header kolom
    
    # Loop melalui setiap barcode dalam file CSV
    with open('./produk.csv', 'r') as barcode_file:
        reader = csv.reader(barcode_file)
        
        # Lewati header baris pertama jika ada
        next(reader)
        
        # Loop melalui setiap baris dalam file CSV
        for row in reader:
            barcode = row[0]  # Ambil nilai barcode dari kolom pertama
            
            # Membuat objek opsi Chrome
            chrome_options = Options()
            # Mengatur User-Agent sesuai dengan browser yang digunakan
            chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

            # Inisialisasi webdriver Chrome dengan opsi yang ditentukan
            driver = webdriver.Chrome(options=chrome_options)

            # Buat URL dengan nilai barcode
            url = f'https://www.google.com/search?q={barcode}&tbm=isch'
            
            # Buka URL menggunakan webdriver
            driver.get(url)
            
            # Temukan semua elemen gambar pada halaman
            image_elements = driver.find_elements(By.CSS_SELECTOR, 'img')
            
            # Ambil gambar ke-5 (indeks ke-4) dari daftar gambar
            if len(image_elements) > 4:
                image_element = image_elements[4]
                image_url = str(image_element.get_attribute('src'))
                
                # Tulis barcode dan URL gambar ke file CSV
                writer.writerow([row[0],row[1], image_url])
                loop +=1
                print(row[0]+": Sukses")
            else:
                writer.writerow([row[0],row[1], 'Tidak ada gambar ke-5 pada halaman'])
                loop +=1
                print(row[0]+": Tidak ada gambar ke-5 pada halaman")

# Tutup webdriver
driver.quit()
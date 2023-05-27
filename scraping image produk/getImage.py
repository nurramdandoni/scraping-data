import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Inisialisasi webdriver Selenium
driver = webdriver.Chrome()  # Ganti dengan driver sesuai dengan browser yang Anda gunakan (misalnya Firefox)

# # URL yang akan dibuka
# url = 'https://www.google.com/search?q=8991002122000&tbm=isch'
# # Buka URL menggunakan webdriver
# driver.get(url)

# Ambil tangkapan layar dari halaman web
# screenshot_path = 'screenshot.png'
# driver.save_screenshot(screenshot_path)


# # Temukan semua elemen gambar pada halaman
# image_elements = driver.find_elements(By.CSS_SELECTOR, 'img')

# # Ambil URL gambar pada daftar gambar pertama
# image_urls = []
# for i in range(min(len(image_elements), 5)):  # Ambil maksimal 5 gambar pertama
#     image_element = image_elements[i]
#     image_url = image_element.get_attribute('src')
#     image_urls.append(image_url)

# # Cetak URL gambar
# for url in image_urls:
#     print(url)

# # Temukan elemen gambar pertama
# image_element = driver.find_element(By.CSS_SELECTOR, 'img')

# # Dapatkan URL gambar dari atribut 'src'
# image_url = image_element.get_attribute('src')

# # Cetak URL gambar pertama
# print(image_url)

# # Temukan semua elemen gambar pada halaman
# image_elements = driver.find_elements(By.CSS_SELECTOR, 'img')

# # Ambil gambar ke-5 (indeks ke-4) dari daftar gambar
# if len(image_elements) > 4:
#     image_element = image_elements[4]
#     image_url = image_element.get_attribute('src')
    
#     # Lakukan tindakan selanjutnya dengan gambar ke-5
    
#     # Cetak URL gambar ke-5
#     print(image_url)
# else:
#     print('Tidak ada gambar ke-5 pada halaman')



# Buka file CSV untuk menulis data
with open('./out.csv', 'w', newline='') as csv_file:
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
                print(image_url)
            else:
                writer.writerow([row[0],row[1], 'Tidak ada gambar ke-5 pada halaman'])

# Tutup webdriver
driver.quit()
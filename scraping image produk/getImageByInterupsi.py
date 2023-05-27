import time
from selenium import webdriver

# Inisialisasi webdriver Selenium
driver = webdriver.Chrome()

# URL yang akan dibuka
url = 'https://www.google.com/search?q=8991002122000&tbm=isch'
# Buka URL menggunakan webdriver
driver.get(url)

time.sleep(3)  # Tunggu selama 3 detik (Anda dapat menggantinya dengan logika yang sesuai)

# Temukan semua elemen gambar dengan XPath
image_elements = driver.find_elements('xpath', '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img')

# Periksa apakah terdapat elemen kedua dalam daftar
if len(image_elements) > 1:
    # Dapatkan elemen kedua
    image_element = image_elements[1]
    
    # Dapatkan URL gambar dari atribut 'src'
    image_url = image_element.get_attribute('src')
    
    # Cetak URL gambar
    print(image_url)
else:
    print('Tidak ada elemen gambar kedua')

# Tutup webdriver
driver.quit()

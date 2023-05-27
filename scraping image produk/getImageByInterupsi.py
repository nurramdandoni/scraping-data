import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Inisialisasi webdriver Selenium
driver = webdriver.Chrome()
barcode = '8991002122000'
nama = 'ABC EXO CHOCOMALT'

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
    # Dapatkan elemen gambar kedua
    image_element = image_elements[0]
    
    # Dapatkan URL gambar dari atribut 'src'
    image_url = image_element.get_attribute('src')
    
    # Cetak URL gambar
    print(image_url)

# Tutup webdriver
driver.quit()

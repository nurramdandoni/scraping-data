from selenium import webdriver

# Inisialisasi webdriver Selenium
driver = webdriver.Chrome()  # Ganti dengan driver sesuai dengan browser yang Anda gunakan (misalnya Firefox)

# URL yang akan dibuka
url = 'https://www.google.com/search?client=firefox-b-d&q=8991002122000'

# Buka URL menggunakan webdriver
driver.get(url)

# Ambil tangkapan layar dari halaman web
screenshot_path = 'screenshot.png'
driver.save_screenshot(screenshot_path)

# Tutup webdriver
driver.quit()
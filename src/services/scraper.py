from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def scrape_playlist_spotify():
    url = 'https://open.spotify.com/playlist/7Cr153JYdNSJAuX0IjVb5J?si=jgQcMVC-ScWLPYMr0t3jBA&pi=u-aTDu_FTnQB-s&nd=1&dlsi=652d424bc7824a5b' 

    # Configuração do Chrome sem interface gráfica
    options = Options()
    options.add_argument("--headless")  # Para rodar sem interface gráfica

    # Inicializa o WebDriver (você precisa do ChromeDriver instalado)
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)
    
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    music_titles = soup.find_all('div', class_='encore-text encore-text-body-medium encore-internal-color-text-base btE2c3IKaOXZ4VNAb8WQ standalone-ellipsis-one-line')

    list_music = []
    for title in music_titles:
        list_music.append(title.text)
    
    driver.quit()
    
    return list_music




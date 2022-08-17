import requests
from bs4 import BeautifulSoup
SiteENSH = 'https://www.ensh.dz/category/marches-publiques/'
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
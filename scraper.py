from selenium import webdriver
#library for chrome options qui sont indisponsable pour replit for some reason? 
 

SiteENSH = 'https://www.ensh.dz/category/marches-publiques/'



#driver is a simulation of a driver in request that we can use , so we are loading the page HtmlText in it
driver = webdriver.Chrome()
driver.get('https://www.repl.it/')
print(driver.title)


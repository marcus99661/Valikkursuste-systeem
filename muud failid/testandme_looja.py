import time
from selenium import webdriver
import random
import string

algus_aeg = time.clock()
x = 1
nimed = ["Emily","Madison","Emma","Hannah","Abigail","Olivia","Ashley","Samantha","Alexis","Sarah","Elizabeth","Isabella","Alyssa","Grace","Lauren","Taylor","Jessica","Brianna","Kayla"]

website = "https://docs.google.com/forms/d/e/1FAIpQLSeqw3IGGkasB51jKXjrX_Ig6xHK0cTlbu39Y1eUs8CkNDDWDQ/viewform?usp=sf_link"

driver = webdriver.Chrome("D:\Chromedriver 2\chromedriver.exe")
driver.get(website)
korda = 4
time.sleep(3)
def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))
for i in range(268, 525):
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[1]/input').send_keys(random_char(7)+"@fakegmail.com")
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(random.choice(nimed) + " " + str(i))
    ### klass
    asd1 = random.randint(1,3)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[' + str(asd1) + ']/label').click()
    ### 2. periood hommik
    asd2 = random.randint(1,14)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd2) + ']/label').click()
    korda += 1
    asd3 = random.randint(1,14)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd3) + ']/label').click()
    korda += 1
    asd4 = random.randint(1,14)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd4) + ']/label').click()

    korda += 1
    asd5 = random.randint(1,13)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd5) + ']/label').click()
    korda += 1
    asd6 = random.randint(1,13)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd6) + ']/label').click()
    korda += 1
    asd7 = random.randint(1,13)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd7) + ']/label').click()

    korda += 1
    asd8 = random.randint(1,13)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd8) + ']/label').click()
    korda += 1
    asd9 = random.randint(1,13)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd9) + ']/label').click()
    korda += 1
    asd10 = random.randint(1,13)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd10) + ']/label').click()
    
    korda += 1
    asd11 = random.randint(1,12)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd11) + ']/label').click()
    korda += 1
    asd12 = random.randint(1,12)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd12) + ']/label').click()
    korda += 1
    asd13 = random.randint(1,12)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd13) + ']/label').click()
    
    korda += 1
    asd14 = random.randint(1,13)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd14) + ']/label').click()
    korda += 1
    asd15 = random.randint(1,13)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd15) + ']/label').click()
    korda += 1
    asd16 = random.randint(1,13)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd16) + ']/label').click()
    
    korda += 1
    asd17 = random.randint(1,9)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd17) + ']/label').click()
    korda += 1
    asd18 = random.randint(1,9)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd18) + ']/label').click()
    korda += 1
    asd19 = random.randint(1,9)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd19) + ']/label').click()
    
    korda += 1
    asd20 = random.randint(1,11)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd20) + ']/label').click()
    korda += 1
    asd21 = random.randint(1,11)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd21) + ']/label').click()
    korda += 1
    asd22 = random.randint(1,11)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd22) + ']/label').click()
    
    korda += 1
    asd23 = random.randint(1,8)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd23) + ']/label').click()
    korda += 1
    asd24 = random.randint(1,8)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd24) + ']/label').click()
    korda += 1
    asd25 = random.randint(1,8)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[' + str(korda) + ']/div/div/div[2]/div/div/span/div/div[' + str(asd25) + ']/label').click()

    driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[3]/div/div").click()
    
    driver.get(website)
    korda = 4
    time.sleep(0.5)


from selenium import webdriver
import pandas as pd
desired_width = 320
pd.set_option('display.width', desired_width)
from time import sleep
import random

class CoList:
    def __init__(self):
        self.path = r"C:\Users\Admin\Desktop\chromedriver.exe"
        self.driver = webdriver.Chrome(self.path)
        self.driver.get('https://www.colist.eu/searchbygroup.php?lang=en&land_id=16&&group_id=15560&&org_group_id=0,15084,15560,&&records=10&')

    colist_data = pd.DataFrame(columns=['Company Name', 'info', 'loc_phone'])

    def wait(self):
        sleep(random.uniform(0.4, 0.7))

    def crawling(self):
        base_url = 'https://www.colist.eu/searchbygroup.php?lang=en&land_id=16&&group_id=15560&&org_group_id=0,15084,15560,&&records=10&start='
        for url_i in range(1, 332):
            for i in range(0, 10):
                try:
                    name = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/table/tbody/tr[7]/td/table/tbody/tr[{}]/td/b/font'.format((i*3) + 1)).text
                except:
                    name = None
                try :
                    info = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/table/tbody/tr[7]/td/table/tbody/tr[{}]/td[1]'.format((i * 3) + 2)).text
                except:
                    info = None
                try :
                    loc_phone = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/table/tbody/tr[7]/td/table/tbody/tr[{}]/td[3]'.format((i * 3) + 2)).text
                except:
                    loc_phone = None

                self.colist_data.loc[len(self.colist_data.index)] = [name, info, loc_phone]
                print(i)
                print([name, info, loc_phone])

            self.wait()
            self.driver.get(base_url+'{}'.format(url_i * 10))
            print(base_url+'{}'.format(url_i * 10))

        self.colist_data.to_csv('colist.csv', index=False)
        print(self.colist_data)
        # for i in range(1,11):
        #     if i > 1:
        #         i = i*3
        #     else:
        #         pass
        #     try:
        #         name = self.driver.find_elements_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/table/tbody/tr[7]/td/table/tbody/tr[{}]/td/b/font'.format(i))
        #     except:
        #         name = None
        #     try:
        #         info = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/table/tbody/tr[7]/td/table/tbody/tr[2]/td[1]').





class EuroPages:
    def __init__(self):
        self.path = r"C:\Users\Admin\Desktop\chromedriver.exe"
        self.driver = webdriver.Chrome(self.path)

    def wait(self):
        sleep(random.uniform(1, 1.5))


    def get_name(self):
        try:
            name = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/aside/div[1]/div[1]/div/div[1]/h3').text
            return name
        except:
            return None

    def get_number(self):
        try:
            number = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[2]/aside/div[1]/div[1]/div/div[2]/div/div').text
            return number
        except:
            return None

    def get_website(self):
        try:
            number = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[2]/aside/div[1]/div[1]/div/div[2]/div/div').text
            return number
        except:
            return None
    def get_country(self):
        try:
            country = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[2]/aside/div[1]/div[1]/div/div[1]/div/address/dl/span/span/dd[1]/span[2]').text
            return country
        except:
            return None

    def get_adress(self):
        try:
            address = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[2]/aside/div[1]/div[1]/div/div[1]/div/address/dl/span/span/dd[2]/pre').text
            return address
        except:
            return None

    def click_phone(self):
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/aside/div[1]/div[1]/div/div[2]/div').click()
        except:
            pass
    def click_company(self):
        try:
            self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[3]/div[3]/ul/li[{}]/div[2]/div[2]/a'.format(i)).click()
            self.wait()
        except:
            print('error')
    def animal_production(self):
        website = 'https://www.europages.co.uk/companies/results.html?ih=02559&ih=02540H&ih=01607A&ih=02715B&ih=02540A'
        self.driver.get(website)

        animal_data = pd.DataFrame(columns=['Company Name', 'number', 'website', 'country', 'address'])

        for i in range (1, 34):
            if i != 5:
                try:
                    self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[3]/ul/li[{}]/div[2]/div[2]/a'.format(i)).click()
                    self.wait()
                except:
                    print('error')

            self.wait()
            self.driver.back()
            animal_data.loc[len(animal_data.index)] = [name, number, website, country, address]
            print(i)
            print([name, number, website, country, address])

        animal_data.to_csv('animal.csv', index=False)
        print(animal_data)
b = EuroPages()
b.animal_production()



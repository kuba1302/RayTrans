from selenium import webdriver
import pandas as pd
desired_width = 320
pd.set_option('display.width', desired_width)
from time import sleep
import random
from selenium.webdriver.chrome.options import Options

class CoList:
    def __init__(self):
        self.path = r"C:\Users\Admin\Desktop\chromedriver.exe"
        self.driver.get('https://www.colist.eu/searchbygroup.php?lang=en&land_id=16&&group_id=15560&&org_group_id=0,15084,15560,&&records=10&')
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(self.path, options=self.options)

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
        sleep(random.uniform(0.4, 0.6))


    def get_name(self):
        try:
            name = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/aside/div[1]/div[1]/div/div[1]/h3').text
            return name
        except:
            return None

    def get_number(self):
        try:
            self.wait()
            number = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[2]/aside/div[1]/div[1]/div/div[2]/div/div').text
            return number
        except:
            return None

    def get_website(self):
        try:
            number = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[2]/aside/div[1]/div[1]/div/a[1]').get_attribute('href')
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

    def get_address(self):
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

    def get_info(self):
        company_info = [self.get_name(), self.get_number(), self.get_website(),
                        self.get_country(), self.get_address()]
        print(company_info)
        return company_info

    animal_data = pd.DataFrame(columns=['Company Name', 'number', 'website', 'country', 'address'])

    def next_company(self, i):
        try:
            link = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[3]/div[3]/ul/li[{}]/div[2]/div[2]/a'.format(i)).get_attribute('href')
            self.driver.get(link)
            self.wait()
            self.click_phone()
            print(i)
            self.animal_data.loc[len(self.animal_data.index)] = self.get_info()
            self.driver.back()
        except:
            try:
                link = self.driver.find_element_by_xpath(
                    '/html/body/div[2]/div[3]/div[3]/ul/li[{}]/div[2]/div/a'.format(i)).get_attribute('href')
                self.driver.get(link)
                self.wait()
                self.click_phone()
                print(i)
                self.animal_data.loc[len(self.animal_data.index)] = self.get_info()
                self.driver.back()
            except:
                print('error')

    def animal_production(self):
        website = 'https://www.europages.co.uk/companies/results.html?ih=02740P&ih=02740Q&ih=02745R&ih=02700I&ih=02740G&ih=02701G&ih=02900D&ih=02745A&ih=02740J&ih=02745E&ih=02740R&ih=02740O&ih=' \
                  '02740K&ih=02740C&ih=02740I&ih=02740A&ih=02701B&ih=02664B&ih=02703A&ih=02700A&ih=02745P&ih=02740N&ih=02700H&ih=02700B&ih=02740M&ih=02740F&ih=02664A&ih=02701A&ih=02703B&ih=02740H&ih=02740E'
        self.driver.get(website)
        for url_i in range(1, 278):
            self.wait()
            self.driver.get('https://www.europages.co.uk/companies/pg-{}/results.html?ih=02700B;02900D;02664A;02'
                            '745A;02701G;02740O;02700A;02740Q;02703A;02701B;02740E;02740I;02745R;02664B;02700H;02740A;02701A;02740N;02740'
                            'F;02703B;02740H;02700I;02745E;02740C;02740K;02740R;02740M;02740G;02745P;02740P;02740J'.format(url_i))
            for i in range(1, 34):
                self.next_company(i)

        self.animal_data.to_csv('drinks_all_countries.csv', index=False)
        self.driver.close()
b = EuroPages()
b.animal_production()



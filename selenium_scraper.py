from selenium import webdriver
import pandas as pd
desired_width = 320
pd.set_option('display.width', desired_width)
from time import sleep
import random
from selenium.webdriver.chrome.options import Options

class CoList:
    def __init__(self):
        self.path = "/usr/bin/chromedriver"
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
        self.path = "/usr/bin/chromedriver"
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

    data = pd.DataFrame(columns=['Company Name', 'number', 'website', 'country', 'address'])

    def next_company(self, i):
        try:
            link = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[3]/div[3]/ul/li[{}]/div[2]/div[2]/a'.format(i)).get_attribute('href')
            self.driver.get(link)
            self.wait()
            self.click_phone()
            print(i)
            self.data.loc[len(self.data.index)] = self.get_info()
            self.driver.back()
        except:
            try:
                link = self.driver.find_element_by_xpath(
                    '/html/body/div[2]/div[3]/div[3]/ul/li[{}]/div[2]/div/a'.format(i)).get_attribute('href')
                self.driver.get(link)
                self.wait()
                self.click_phone()
                print(i)
                self.data.loc[len(self.data.index)] = self.get_info()
                self.driver.back()
            except:
                print('error')

    def scraping(self, start_page, end_page, file_name, new_file = True):
        # Create empty csv file
        if new_file:
            self.data.to_csv('{}.csv'.format(file_name), index=False)

        for url_i in range(start_page, end_page):
            # Reset DataFrame at the begining of every iteration
            self.data = pd.DataFrame(columns=['Company Name', 'number', 'website', 'country', 'address'])

            self.wait()
            self.driver.get('https://www.europages.co.uk/companies/pg-{}/results.html?ih=04662B;04620H;04661C;04615K;0'
                            '4670D;04670A;04665L;04663A;04663K;04674A;04661D;04663D;04615G;04615A;04620A;04661A;04663'
                            'H;04615H;04661E;04663F;04662A;04665N;04672A;04663I;04615E;04677A;04620F;04620B;04663B;0'
                            '4663C;04670E;04615F;04665B;04615D;04630A;05626I;04620L;04665O;04630B;04660F;04665A;0466'
                            '3J;04620G;04665J;04620I;04665C;05620M;04630C;04615B;04620J;04672B;04660H;04620K'.format(url_i))

            print('Scraping {} page'.format(url_i))

            for i in range(1, 34):
                self.next_company(i)

            if url_i % 2 == 0:
                self.data.to_csv('{}.csv'.format(file_name), mode= 'a', index=False, header=False)

        self.driver.close()

    def search_on_dnb(self, name):
        self.driver.get('https://www.dnb.com/')
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/div/div[2]/div[1]/button').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/input')\
            .send_keys(name)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/button').click()

b = EuroPages()
b.scraping(621, 1749, 'tools_hardware', new_file=False)




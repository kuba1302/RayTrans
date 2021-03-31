from selenium import webdriver
import pandas as pd
desired_width = 320
pd.set_option('display.width', desired_width)
from time import sleep
import random
from selenium.webdriver.chrome.options import Options
from multiprocessing import Process
import threading
from datetime import datetime
import numpy as np


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
        # Prepare dict for multiple site scraping at once
        self.scraping_dict = {
            'site_url': ['https://www.europages.co.uk/companies/pg-{}/results.html?ih=09315A;09303E;09312D;09305D;09315D;09315C;09312B'
                         ';09303B;09303G;09312A;09305A;09305C;09303D;09305B;09305G;09303F;09303C;09305H;09330C;09305E;09312G;09305I;09315B',
                         'https://www.europages.co.uk/companies/pg-{}/results.html?ih=15220A;19569D;15220D;15220C;15220B;15220E',
                         'https://www.europages.co.uk/companies/pg-{}/results.html?ih=15210D;15230C;15230F;15216C;15212O;15230A;15230B;15210E'
                         ';15212L;15210A;15225C;15218D;15210B;15218A;15210F;15218C;15216B;15216D;15212M;15225B;15230E;15220F;15210P;19569N;152'
                         '10C;15216A;15210O;15212A;15225D;15210H;19575F;15212N;15210I;15212K;15230G'],
            'file_name': ['wood', 'paper_packing_materials', 'paper_finished_products'],
            'start_page': [1, 1, 1],
            'end_page': [205, 88, 312],
            'current_page': [0, 0, 0], # Save current page
            'new_file': [True, True, True], # Check if new file is needed
            'driver_name': [webdriver.Chrome(self.path), webdriver.Chrome(self.path), webdriver.Chrome(self.path)], # Need few drivers
            'data': [pd.DataFrame(columns=['Company Name', 'number', 'website', 'country', 'address']),
                     pd.DataFrame(columns=['Company Name', 'number', 'website', 'country', 'address']),
                     pd.DataFrame(columns=['Company Name', 'number', 'website', 'country', 'address'])] # Need few data frames
        }


    def wait(self):
        sleep(random.uniform(0.4, 0.6))


    def get_name(self, site_number):
        try:
            name = self.scraping_dict['driver_name'][site_number].find_element_by_xpath('/html/body/div[2]/div[2]/aside/div[1]/div[1]/div/div[1]/h3').text
            return name
        except:
            return None

    def get_number(self, site_number):
        try:
            self.wait()
            number = self.scraping_dict['driver_name'][site_number].find_element_by_xpath(
                '/html/body/div[2]/div[2]/aside/div[1]/div[1]/div/div[2]/div/div').text
            return number
        except:
            return None

    def get_website(self, site_number):
        try:
            number = self.scraping_dict['driver_name'][site_number].find_element_by_xpath(
                '/html/body/div[2]/div[2]/aside/div[1]/div[1]/div/a[1]').get_attribute('href')
            return number
        except:
            return None
    def get_country(self, site_number):
        try:
            country = self.scraping_dict['driver_name'][site_number].find_element_by_xpath(
                '/html/body/div[2]/div[2]/aside/div[1]/div[1]/div/div[1]/div/address/dl/span/span/dd[1]/span[2]').text
            return country
        except:
            return None

    def get_address(self, site_number):
        try:
            address = self.scraping_dict['driver_name'][site_number].find_element_by_xpath(
                '/html/body/div[2]/div[2]/aside/div[1]/div[1]/div/div[1]/div/address/dl/span/span/dd[2]/pre').text
            return address
        except:
            return None

    def click_phone(self, site_number):
        try:
            self.scraping_dict['driver_name'][site_number].find_element_by_xpath('/html/body/div[2]/div[2]/aside/div[1]/div[1]/div/div[2]/div').click()
        except:
            pass

    def get_info(self, site_number):
        company_info = [self.get_name(site_number), self.get_number(site_number), self.get_website(site_number),
                        self.get_country(site_number), self.get_address(site_number)]
        print(company_info)
        return company_info

    data = pd.DataFrame(columns=['Company Name', 'number', 'website', 'country', 'address'])

    def next_company(self, i, site_number):
        try:
            link = self.scraping_dict['driver_name'][site_number].find_element_by_xpath(
                '/html/body/div[2]/div[3]/div[3]/ul/li[{}]/div[2]/div[2]/a'.format(i)).get_attribute('href')
            self.scraping_dict['driver_name'][site_number].get(link)
            self.wait()
            self.click_phone(site_number)
            self.scraping_dict['data'][site_number].loc[len(self.scraping_dict['data'][site_number].index)] = self.get_info(site_number)
            self.scraping_dict['driver_name'][site_number].back()
        except:
            try:
                link = self.scraping_dict['driver_name'][site_number].find_element_by_xpath(
                    '/html/body/div[2]/div[3]/div[3]/ul/li[{}]/div[2]/div/a'.format(i)).get_attribute('href')
                self.scraping_dict['driver_name'][site_number].get(link)
                self.wait()
                self.click_phone(site_number)
                self.scraping_dict['data'][site_number].loc[len(self.scraping_dict['data'][site_number].index)] = self.get_info(site_number)
                self.scraping_dict['driver_name'][site_number].back()
            except:
                print('error')

    def scraping(self, site_number):
        # Test scraping performacne
        time_list = []
        # Create empty csv file if start scraping new page
        if self.scraping_dict['new_file'][site_number]:
            self.data.to_csv('{}.csv'.format(self.scraping_dict['file_name'][site_number]), index=False)

        # Get page numbers of page from dict
        for url_i in range(self.scraping_dict['start_page'][site_number], self.scraping_dict['end_page'][site_number]):
            # Reset DataFrame at the beginning of every iteration
            time_start = datetime.now()
            url = self.scraping_dict['site_url'][site_number].format(url_i)
            self.data = pd.DataFrame(columns=['Company Name', 'number', 'website', 'country', 'address'])
            self.wait()
            self.scraping_dict['driver_name'][site_number].get(url.format(url_i))
            for i in range(1, 34):
                self.next_company(i, site_number)
            # Save scraped data every 2 iterations
            if url_i % 2 == 0:
                self.scraping_dict['data'][site_number].to_csv('{}.csv'.format(self.scraping_dict['file_name'][site_number]), mode= 'a', index=False, header=False)
            # Keep current page number
            self.scraping_dict['current_page'][site_number] = url_i
            print(self.scraping_dict['file_name'][site_number], 'page number: ', self.scraping_dict['current_page'][site_number])
            # Test scraping performacne
            time_end = datetime.now()
            scraping_time = time_end - time_start
            scraping_time = scraping_time.total_seconds()
            time_list.append(scraping_time)

            if url_i % 5 == 0:
                mean = np.mean(time_list)
                print(f'One page scraping mean for {url_i} pages',mean)

        self.scraping_dict['driver_name'][site_number].close()

    def multiple_scraping(self, number_of_sites):
        thread_list = []
        for i in range(number_of_sites):
            t = threading.Thread(target=self.scraping, args=[i])
            t.start()
            thread_list.append(t)

        for thread in thread_list:
            thread.join()


    def search_on_dnb(self, name):
        self.driver.get('https://www.dnb.com/')
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/div/div[2]/div[1]/button').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/input')\
            .send_keys(name)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/button').click()

    def test1(self, i):
        self.path = "/usr/bin/chromedriver"
        self.driver1 = webdriver.Chrome(self.path)
        self.driver2 = webdriver.Chrome(self.path)
        self.driver1.get('https://www.google.com')
        self.driver2.get('https://www.amazon.com')

if __name__ == '__main__':
    a = 0
    b = EuroPages()
    b.multiple_scraping(3)





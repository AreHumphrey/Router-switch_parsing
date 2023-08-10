from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep


def check_exist(obj):
    if obj is not None:
        return True
    else:
        return False


excel = pd.DataFrame(
    columns=["Model", "Main Image", "Other Images", "Category/Brand", "Model/Detail", "List Price", "Price",
             "Specification"])

options = Options()
options.add_argument('--headless')
driver_path = "D:\chromedriver.exe"
service = Service(driver_path)

with webdriver.Chrome(service=service, options=options) as driver:
    with open("products.txt", "r") as file:
        arr_product = file.read().splitlines()

    for product in arr_product:
        driver.get(product)
        sleep(10)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        div_element = soup.select_one('.page-main')

        name_element = div_element.find("meta", itemprop="sku")
        name = name_element["content"]
        print(name)

        img_main_element = div_element.find("img")
        img_main = img_main_element["src"] if img_main_element else None

        model_element = div_element.find("td", class_="h-model-pr")
        detail_element = div_element.find("div", itemprop="description")
        if model_element:
            model = model_element.text.strip()
        else:
            model = None
        if detail_element:
            detail = detail_element.text.strip()
        else:
            detail = None

        list_price = div_element.find('span', class_="price")
        l_prices = list_price.text.strip() if list_price else None

        price = div_element.find('span', class_="regular-price")
        price_element = price.text.strip() if price else None

        path = []
        for item in soup.select('.items'):
            li_category = item.find_all('a')[2].text
            li_brand = item.find_all('a')[-2].text
            path.append((li_category[2:], li_brand[2:]))

        specifications = []
        specification_table = soup.find('div', class_='std').find('table')

        if specification_table:
            header_row = specification_table.find('tr')
            if header_row:
                table_name_element = header_row.find('strong')
                if table_name_element:
                    table_name = table_name_element.text.strip()
                    data_rows = specification_table.find_all('tr')[1:]
                    for row in data_rows:
                        cells = row.find_all('td')
                        if cells and len(cells) > 0:
                            spec_name_element = cells[0].find('p')
                            spec_name = spec_name_element.text.strip() if spec_name_element else None
                        else:
                            spec_name = None

                        if len(cells) > 1:
                            if cells[1].find('p'):
                                spec_value = cells[1].find('p').text.strip()
                            else:
                                spec_value = None
                            specifications.append((spec_name, spec_value))
                        else:
                            specifications.append((spec_name, None))

        excel = pd.concat([excel, pd.DataFrame({
            "Model": [name],
            "Main Image": [img_main],
            "Category/Brand": [path],
            "Model/Detail": [(model if model else "") + " / " + (detail if detail else "")],
            "List Price": [l_prices],
            "Price": [price_element],
            "Specification": [specifications]
        })])

        excel.to_excel("output.xlsx", index=False)

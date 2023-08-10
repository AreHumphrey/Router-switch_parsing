import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.router-switch.com")
soup = BeautifulSoup(req.text, "html.parser")

with open("out.html", 'w', encoding="utf-8") as f:
    f.write(soup.prettify())

hrefs = []
count = 0
div1_element = soup.select_one('.header-dropdown-first')
if div1_element:
    div2 = div1_element.find_all('div', class_='header-dropdown-third')
    for div in div2:
        links_element = div.find_all('ul', class_='header-dropdown-third-lilst')
        for link in links_element:
            li_elements = link.find_all('li', class_="nav-category-text")
            for li_element in li_elements:
                a_elements = li_element.find_all('a', href=True)
                for a_element in a_elements:
                    href = a_element['href']
                    hrefs.append(href)

sorted_hrefs = sorted(hrefs)

arr_product = []
with open("products.txt", "a") as file:
    for href in sorted_hrefs:
        page_number = 1
        has_next_page = True

        while has_next_page:
            url = f"{href}?p={page_number}"
            req = requests.get(url)
            soup = BeautifulSoup(req.text, "html.parser")

            product_links = soup.select(".products.wrapper.list.products-list")
            for link in product_links:
                a_elements = link.find_all('a', class_="product-item-link")
                for a in a_elements:
                    product = a["href"]
                    arr_product.append(product)
                    file.write(product)
                    file.write('\n')
                    count += 1

            next_page_button = soup.select_one(".action .next")
            if next_page_button:
                page_number += 1
            else:
                has_next_page = False

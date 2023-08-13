import os
import requests
import re


def download_image(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print("Картинка успешно скачана и сохранена как", file_path)
    else:
        print("Ошибка при скачивании картинки")


txt_file = "img.txt"
names_file = "name.txt"
folder = "images"

if not os.path.exists(folder):
    os.makedirs(folder)

with open(txt_file, "r") as file:
    img = file.read().splitlines()

with open(names_file, "r") as file:
    product_names = file.read().splitlines()

if len(img) != len(product_names):
    print("Ошибка: количество изображений и названий товаров не совпадает.")
else:
    for url, name in zip(img, product_names):
        valid_name = re.sub(r'[\\/:"*?<>|]+', '_', name)
        save_path = os.path.join(folder, f"{valid_name}.jpg")
        download_image(url, save_path)

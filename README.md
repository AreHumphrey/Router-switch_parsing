# _Описание_
_Данный проект представляет собой парсер для веб-сайта:_
**_https://www.router-switch.com_**
# _Функциональность_
 _Парсер позволяет извлекать:_
 * _Наименование товара_
 * _Модель товара_
 * _Цену_
 * _Главную фотографию_
 * _Бренд товара_
 * _Раздел в котором находится данный товар_<br>
_и загружать полученные данные в Excel_
* _Так же программа позволяет импортировать изображения товаров с сайта в указанную папку при помощи_ **foto.py**<br>
# _Установка_
_1. Установите Python на свою систему, если его еще нет. Вы можете загрузить Python с официального сайта Python._
_2. Установите Selenium и прочие модули, выполните следующие команды:_
<pre> pip install selenium </pre>
<pre> pip install beautifulsoup4  </pre>
<pre> pip install pandas </pre>
_3. Запустите парсер, выполнив следующую команду:_
<pre> python parser.py </pre>
_Парсер начнет обрабатывать веб-страницу router-switch.com, извлекать данные о товарах и сохранять их в_ **xlsx** _формате._<br>
_4. Если необходимо скачать и поместить изображения товаров в папку, воспользуйтесь:_ 
<pre> python foto.py </pre>





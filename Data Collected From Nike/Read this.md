# JSON That Has Been Collected From Nike.com

Through my research of Nike's website I have found that Nike uses two different types of webpages (not inclueding nike ID), due to this they also formate their JSON differently. Both of these webpages use javascript with the JSON data to formate the overall look of the webpageon the front-end. The javascript disable and enable elements of the HTML (ex. size in stock).

## Webpage 1 - New JSON Formate

![alt text](https://github.com/MJC17/Nike-Stock-Moniter/blob/master/Data%20Collected%20From%20Nike/Images/Screen%20Shot%202018-03-09%20at%2012.19.28%20PM.png)

To find the JSON within this formate of the Nike page, input/use:

```python
import requests
from bs4 import BeautifulSoup
import json

StyleCode = raw_input("What is the SKU?")

URL = 'https://store.nike.com/us/en_us/pw/n/1j7?sl=' + str(StyleCode)
r = requests.get(URL).content
lxml = BeautifulSoup(r, "lxml")
j = lxml.find_all('script')[0]
print(j)
```

### Todo List
- [ ] Locate JSON
- [ ] Locate the indacation of the sizes in stock
- [ ] Locate the Client ID within the JSON/HTML

## Webpage 2 - Old JSON Formate

![alt text](https://github.com/MJC17/Nike-Stock-Moniter/blob/master/Data%20Collected%20From%20Nike/Images/Screen%20Shot%202018-03-09%20at%2012.19.55%20PM.png)

To find the JSON within this formate of the Nike page, input/use:

```python
import requests
from bs4 import BeautifulSoup
import json

StyleCode = raw_input("What is the SKU?")

URL = 'https://store.nike.com/us/en_us/pw/n/1j7?sl=' + str(StyleCode)
r = requests.get(URL).content
lxml = BeautifulSoup(r, "lxml")
j = lxml.find("script", {"id": "product-data"}).string
print(j)
```

### Todo List
- [x] Locate JSON
- [x] Locate the indacation of the sizes in stock
- [ ] Locate the Client ID within the JSON/HTML

## Webpage 3 - Countdown Page (JSON Formate Unknown)
![alt text](https://github.com/MJC17/Nike-Stock-Moniter/blob/master/Data%20Collected%20From%20Nike/Images/Screen%20Shot%202018-03-09%20at%2012.18.30%20PM.png)

To find the JSON within this formate of the Nike page, input/use:

```python
#Still working on this 
```

### Todo List
- [ ] Locate JSON
- [ ] Locate the indacation of the sizes in stock
- [ ] Locate the the data invalving the countdown timer


import requests
from bs4 import BeautifulSoup
import json

class Shoe:

	def __init__(self, Site, Region, StyleCode):

		if Site.upper == "NIKE":
			Nike(self, StyleCode, Region)
		else:
			pass
	


def Nike(Shoe, StyleCode, Region):

		if Region == "US":
			Shoe.URL = 'https://store.nike.com/us/en_us/pw/n/1j7?sl=' + str(StyleCode)
		else:
			pass

		Shoe.r = requests.get(Shoe.URL).content
		Shoe.soup = BeautifulSoup(Shoe.r, "lxml")
		Shoe.j = Shoe.soup.find("script", {"id": "product-data"}).string
		Shoe.jsn = json.loads(Shoe.j)
		print(Shoe.j)
		# Sizes in Stock
		Shoe.sizesinStock = []
		Shoe.sizesBox = Shoe.jas['skuContainer']['productSkus']
		for size in Shoe.sizesBox:
			if size['inStock'] == True:
				sizeNum = size['displaySize']

				for i in "M/ W":
					sizeNum = str(sizeNum).replace(i, "")

				sizeNum = float(sizeNum)

				if '.0' in str(sizeNum):
					sizeNum = int(sizeNum)
				else:
					sizeNum = float(sizeNum)
				Shoe.sizesinStock.append(sizeNum)

		Shoe.Price = Shoe.jas['rawPrice']
		Shoe.Name = Shoe.jas['productTitle']
		Shoe.ColorWay = Shoe.jas['colorDescription']
		Shoe.StoreName = "Nike"
		Shoe.Brand = "Nike"
		Shoe.Region = Region
		Shoe.StyleCode = Shoe.jas['chat']['productId']
		Shoe.LDate = None
		Shoe.LTime = None
		Shoe.Img = Shoe.jas['imagesCopyLarge']
		Shoe.Url = Shoe.jas['url']
		Shoe.Currency = Shoe.jas['currencyCode']
	
	

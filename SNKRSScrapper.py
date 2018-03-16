import requests
from bs4 import BeautifulSoup
import json

def Shoe(Site, Region, StyleCode):
	if Site == "NIKE":
		s = Nike(Region, StyleCode)
	else:
		pass


	return s



class Nike:
	def __init__(self, Region, StyleCode):
		
		self.URL = 'https://store.nike.com/us/en_us/pw/n/1j7?sl=' + str(StyleCode)
		self.r = requests.get(self.URL).content
		self.soup = BeautifulSoup(self.r, "lxml")
		self.j = self.soup.find("script", {"id": "product-data"}).string
		self.jas = json.loads(self.j)

		# Sizes in Stock
		self.sizesinStock = []
		self.sizesBox = self.jas['skuContainer']['productSkus']
		for size in self.sizesBox:
			if size['inStock'] == True:
				sizeNum = size['displaySize']

				for i in "M/ W":
					sizeNum = str(sizeNum).replace(i, "")

				sizeNum = float(sizeNum)

				if '.0' in str(sizeNum):
					sizeNum = int(sizeNum)
				else:
					sizeNum = float(sizeNum)
				self.sizesinStock.append(sizeNum)

		self.Price = self.jas['rawPrice']
		self.Name = self.jas['productTitle']
		self.ColorWay = self.jas['colorDescription']
		self.Site = "Nike.com"
		self.Brand = "Nike"
		self.Region = Region
		self.StyleCode = self.jas['chat']['productId']
		self.LDate = None
		self.LTime = None
		self.Img = self.jas['imagesCopyLarge']
		self.Url = self.jas['url']
		self.Currency = self.jas['currencyCode']

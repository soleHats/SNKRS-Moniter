import requests
from bs4 import BeautifulSoup
import json

class NikeShoe:

	def __init__(self, StyleCode):
		self.URL = 'https://store.nike.com/us/en_us/pw/n/1j7?sl=' + str(StyleCode)
		self.r = requests.get(self.URL).content
		self.lxml = BeautifulSoup(self.r, "lxml")
		self.j = self.lxml.find("script", {"id": "product-data"}).string
		print(self.j)
        

	def GetStock(self):

		self.sizesinStock = []
		self.sizesBox = json.loads(self.j)['skuContainer']['productSkus']
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

		return self.sizesinStock


	def GetPrice(self):
		self.Price = json.loads(self.j)['rawPrice']
		return self.Price


	def GetName(self):
		self.name = json.loads(self.j)['productTitle']
		return self.name


	def GetColorWay(self):
		self.CW = json.loads(self.j)['colorDescription']
		return

ss1 = NikeShoe("302370-021")
print(ss1.GetName())
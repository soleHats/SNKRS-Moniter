import requests
from bs4 import BeautifulSoup
import json

class NikeShoe:

	def __init__(self, StyleCode):
		self.URL = 'https://store.nike.com/us/en_us/pw/n/1j7?sl=' + str(StyleCode)
		self.r = requests.get(self.URL).content
		self.soup = BeautifulSoup(self.r, "lxml")
		self.j = self.soup.find("script", {"id": "product-data"}).string
		self.jsn = json.loads(self.j)
		print(self.j)


	def GetStock(self):

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

		return self.sizesinStock


	def GetPrice(self):
		self.Price = self.jas['rawPrice']
		return self.Price


	def GetName(self):
		self.name = self.jas['productTitle']
		return self.name


	def GetColorWay(self):
		self.CW = self.jas['colorDescription']
		return

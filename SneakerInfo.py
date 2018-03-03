import requests
from bs4 import BeautifulSoup
import json

class NikeShoe:

	def __init__(self, StyleCode):
		self.URL = 'https://store.nike.com/ca/en_gb/pw/n/1j7?sl=' + str(StyleCode)
		self.r = requests.get(self.URL).content
		self.lxml = BeautifulSoup(self.r, "lxml")



	def GetStock(self):

		self.sizesinStock = []

		self.j = self.lxml.find("script", {"id": "product-data"}).string
		self.j = json.loads(self.j)
		self.sizesBox = self.j['skuContainer']['productSkus']
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
		return self.lxml.find(class_="js-pdpLocalPrice").string


	def GetName(self):
		return self.lxml.find(class_="exp-product-title").string


	def GetColorWay(self):
		return self.lxml.find(class_="colorText").string

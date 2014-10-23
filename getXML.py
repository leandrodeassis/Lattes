from mechanize import Browser
from xml.etree import ElementTree as ET
from zipfile import ZipFile,is_zipfile
from bs4 import BeautifulSoup
import pytesseract
import Image


url = 'http://buscatextual.cnpq.br/buscatextual/download.do?metodo=apresentar&idcnpq='
idlattes = '1982919735990024'

while True:
	try:
		browser = Browser()
		html = browser.open(url+idlattes)
		soup = BeautifulSoup(html)
		image = soup.find('img')
		data = browser.open_novisit(image['src']).read()
		filename = 'captcha.png'
		save = open(filename, 'wb')
		save.write(data)
		save.close()
		captcha = pytesseract.image_to_string(Image.open('captcha.png'))
		getUrl = "http://buscatextual.cnpq.br/buscatextual/download.do?metodo=enviar&idcnpq=%s&palavra=%s" % (idlattes,captcha)
		arquivo = browser.retrieve(getUrl,'%s.zip' % idlattes)[0]
		if is_zipfile('%s.zip' % idlattes):
			print "ENTREI"
			data = ZipFile('%s.zip' % idlattes).read('curriculo.xml')
			break
	except:
		pass

root = ET.fromstring(data)





from selenium import webdriver
import urllib.request


web = webdriver.Chrome()
url = 'https://www.google.com/search?q=rowing+machine+gym&tbm=isch&ved=2ahUKEwj0nfiBypnyAhVNk0sFHYCBDwwQ2-cCegQIABAA&oq=rowing+machine+gym&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIGCAAQCBAeMgYIABAIEB4yBggAEAgQHjIGCAAQCBAeMgYIABAIEB4yBggAEAgQHjIGCAAQCBAeOgQIABBDOggIABCABBCxA1CNK1jeL2CaMWgAcAB4AIABdYgBsgOSAQMxLjOYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=prALYfSyNM2mrtoPgIO-YA&bih=728&biw=1390'
web.get(url)
xpath_p1='//*[@id="islrg"]/div[1]/div['
xpath_p2=']/a[1]/div[1]/img'
for i in range(1,350):
	try:
		src = web.find_element_by_xpath(xpath_p1+str(i)+xpath_p2).get_attribute("src")
		#print(src)
		urllib.request.urlretrieve(
    		src, './data/train/rowing/'+(str(i))+'.jpg')
	except:
		print(i)

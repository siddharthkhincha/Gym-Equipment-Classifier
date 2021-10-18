#This is a utility to download the data by scraping images off Google Searches

#To maintain quality of downloaded images, the original source of the image is tracked and downloaded.

from selenium import webdriver
import urllib.request

def download_data(url,num_images=100,location_to_save=''):
	web = webdriver.Chrome()
	 					
	web.get(url)
	xpath_p1='//*[@id="islrg"]/div[1]/div['
	xpath_p2=']/a[1]/div[1]/img'
	for i in range(1,num_images):
		try:
			src = web.find_element_by_xpath(xpath_p1+str(i)+xpath_p2).get_attribute("src")
			#print(src)
			urllib.request.urlretrieve(
	    		src, location_to_save+(str(i))+'.jpg')
		except:
			print('Error at number: ',i,'. Continuing with the other images.')



if __name__=='__main__':
	url = input("Enter the URL of the google search to scrape images off")
	location_to_save = input("Enter the location to save the images at") 
	num_images = input("Enter the number of images to download")
	download_data(url,location_to_save)

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


groupLinks = [
	"https://www.facebook.com/groups/693606614544160/",
]

imagePaths = [
	"C:\\Users\\lars\\OneDrive - Aalborg Universitet\\Programmering\\Python\\Scripts\\Posting\\Selling-Data.jpg"
]

"""
messages = [
	"4 bullet points:\n- 1\n2\n3\n4\n\nNOT bullet point",
	Keys.CONTROL + "b",
	"4 bold bullet points:\n- 1\n2\n3\n4\n\nNOT bullet point",
	Keys.CONTROL + "b",
	"4 bullet points:\n- 1\n2\n3\n4\n\nNOT bullet point"
]
"""

messages = []

def composeMessage():
	m = []
	m.append(sentence())
	m.append(bold())
	m.append(sentence())
	m.append(bold())
	m.append(sentence())
	return m


def sentence():
	return "4 bullet points:\n- 1\n2\n3\n4\n\nNOT bullet point\n"

def bold():
	return Keys.CONTROL + "b"

def postOnFacebook(messages):
	#Open facebook
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_experimental_option("detach", True)
	chrome_options.add_argument("--disable-infobars")
	chrome_options.add_experimental_option("prefs", { \
		"profile.default_content_setting_values.notifications": 2 # 1:allow, 2:block 
	})
	driver = webdriver.Chrome(options=chrome_options)
	driver.get("https://www.facebook.com")

	#Enter Log-in information
	emailElement = driver.find_element(By.XPATH, './/*[@id="email"]')
	emailElement.send_keys(os.environ.get('EMAIL'))
	passwordElement = driver.find_element(By.XPATH, './/*[@id="pass"]')
	passwordElement.send_keys(os.environ.get('PASSWORD2'))

	#Login
	passwordElement.send_keys(Keys.RETURN)
	WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, './/*[@id="navItem_217974574879787"]/a/div')))


	#Post in all groups
	for link in groupLinks:
		#Open facebook group
		driver.get(link)

		#Insert message
		postBox = driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
		postBox.send_keys(' ')
		WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div")))
		postBox = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div")
		postBox.send_keys(Keys.DELETE)


		print(messages)


		for message in messages:
			print(message)
			postBox = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div")
			postBox.send_keys(message)
		
		for path in imagePaths:
			# Click on the add media button
			addMediaButton = driver.find_elements_by_xpath("//*[contains(text(), 'Photo/Video')]")[0]
			addMediaButton.click()
			sleep(5)

			# Click the 'Upload Photo/Video' button
			uploadPhotoButton = driver.find_element_by_xpath("//input[@type='file'][@class='_n _5f0v']")
			uploadPhotoButton.send_keys(path)
			
			# Wait for the image to upload
			sleep(5)
		#for message in messages:
		#	postBox = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/span/span")
		#	postBox.send_keys(message)


		#Post
		post_button = driver.find_element_by_xpath("//*[@data-testid='react-composer-post-button']")
		clickable = False
		while not clickable:
			cursor = post_button.find_element_by_tag_name('span').value_of_css_property("cursor")
			if cursor == "pointer":
				clickable = True
				break
		#post_button.click()

		
def main():
	messages = composeMessage()
	postOnFacebook(messages)


if __name__ == "__main__":
    main()
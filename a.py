from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException        
from selenium.common.exceptions import StaleElementReferenceException
import pdb
from selenium.webdriver.common.action_chains import ActionChains
from random import randint




#For random waiting
debug = False
shortA = 5
shortB = 10
longA = 50
longB = 100

#Facebook groups
bodybuildingFacebook = [
	"https://www.facebook.com/groups/631289720578391/?ref=br_rs",
	"https://www.facebook.com/groups/453629264758830/?ref=br_rs",
	"https://www.facebook.com/groups/musclewar/?ref=br_rs"
]

testGroupLinksFacebook = [
	"https://www.facebook.com/groups/600475964231127/",
	"https://www.facebook.com/groups/2685275021574710/"
]

flutterFacebook = [
	"https://www.facebook.com/groups/425920117856409/",
	"https://www.facebook.com/groups/googleflutter/?ref=br_rs",
	"https://www.facebook.com/groups/flutterdev/?ref=br_rs"
]

guitarFacebookPrivate = [
	"https://www.facebook.com/groups/everythingguitar/?ref=br_rs",
	"https://www.facebook.com/groups/GuitarUniverse/?ref=br_rs",
	"https://www.facebook.com/groups/909398102509055/?ref=br_rs",
	"https://www.facebook.com/groups/guitarplayerscollective/?ref=br_rs"
]

ADHDGroupsFacebookEnglish1 = [
	"https://www.facebook.com/groups/170248456950819/?notif_id=1577043797255333&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/1148725191823971/?notif_id=1577046285861405&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/adultadhdsupport/?notif_id=1577044633499211&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/1421578967876637/?notif_id=1577099025945041&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/696361647197068/?notif_id=1577099048424827&notif_t=group_r2j_approved&ref=notif",
	

]

ADHDGroupsFacebookEnglish2 = [
	"https://www.facebook.com/groups/1996816297217400/?notif_id=1577105053364318&notif_t=group_r2j_approved&ref=notif",	
	"https://www.facebook.com/groups/adhdparentsuppport/?notif_id=1577111376869471&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/MyADHD/?notif_id=1577112395146851&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/supportforadhd/?notif_id=1577140037634331&notif_t=group_r2j_approved&ref=notif",
	
]

ADHDGroupsFacebookEnglish3 = [
	"https://www.facebook.com/groups/601537296692135/?notif_id=1577161481952195&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/366049367126466/?notif_id=1577310767996621&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/116833318979154/?notif_id=1577416202612259&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/additudemag/?notif_id=1577398475307953&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/ADHDNaturalNonMedicationchildrenSupport/?notif_id=1577655733005050&notif_t=group_r2j_approved&ref=notif",
	
]

ADHDGroupsFacebookEnglish4 = [
	"https://www.facebook.com/groups/168187756595334/?notif_id=1577680225667640&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/2474319084/?notif_id=1577705207542018&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/409354609832404/?notif_id=1577815912900309&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/483756611687483/?notif_id=1582510901695574&notif_t=group_r2j_approved"
]

physiotherapyFacebook = [
	"https://www.facebook.com/groups/1765821727007016/?ref=br_rs",
	"https://www.facebook.com/groups/412864998742796/?ref=br_rs",
	"https://www.facebook.com/groups/202441989790194/?ref=br_rs",
	#"https://www.facebook.com/groups/427750767317549/?ref=br_rs", DUR IKKE
	"https://www.facebook.com/groups/TelehealthPTs/?ref=br_rs",
	"https://www.facebook.com/groups/1573749652679279/?ref=br_rs",
	"https://www.facebook.com/groups/934086979985824/?ref=br_rs",
	"https://www.facebook.com/groups/sportsphysiotherapy/?ref=br_rs",
	"https://www.facebook.com/groups/337909523042091/?ref=br_rs"
]
	


quantifiedSelfFacebook = [
	"https://www.facebook.com/groups/quantifiedself/?notif_id=1590611126742152&notif_t=group_r2j_approved&ref=notif"
]


QuantifiedSelfReddit = [
	"https://www.reddit.com/r/QuantifiedSelf/",
	"https://www.reddit.com/r/Biohackers/",
	"https://www.reddit.com/r/biohacker/"
]

SelfImprovementFacebook = [
	"https://www.facebook.com/groups/1688036868097484/?ref=br_rs",
	"https://www.facebook.com/groups/personaldevelopmentbusinessowners/?ref=br_rs",
	"https://www.facebook.com/groups/personaldevelopmentbusinessowners/?ref=br_rs",
	"https://www.facebook.com/groups/103281503048003/?notif_id=1588590857650040&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/selfimprovementsecretsrevealed1/?notif_id=1588594139889540&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/328246271086920/?notif_id=1588601685690249&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/dailyselfimprovementtopics/?notif_id=1588600649537336&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/491485350932591/?notif_id=1588600794075946&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/312342462784408/?notif_id=1588607924027175&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/559197144233811/?notif_id=1588613433726406&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/selfhelpspiritualbooks/?notif_id=1588628526267943&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/selfimprovementwithmeditationandyogatips/?notif_id=1588622130076918&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/psycholog/?notif_id=1588667880529341&notif_t=group_r2j_approved",
	"https://www.facebook.com/groups/215126659279505/?notif_id=1589122679510050&notif_t=group_r2j_approved&ref=notif",
	"https://www.facebook.com/groups/115654415435645/?notif_id=1589320115986978&notif_t=group_r2j_approved&ref=notif",

]

########################### FILL OUT ALL INFORMATION FROM HERE ********************************************************************

#Choose groups
groupLinksFacebook = SelfImprovementFacebook
groupLinksReddit = QuantifiedSelfReddit

#Images/Videos
imagePaths = [
	#"C:\\Users\\lars\\OneDrive - Aalborg Universitet\\Programmering\\Python\\Scripts\\Posting\\ab.png"
]

#Define message
title = "Would you sell your tracked data if you were paid? How much should you be paid?"
def composeMessage():
	m = []

	randomInteger = randint(1, 2)

	sentence(m, 'The extended selfish gene" - Richard Dawkins\n')
	sentence(m, "Was AMAZING to read! 📖\n")
	sentence(m, "Aim of the book:\n")
	sentence(m, "- Explains selfishness and altruism by looking at life from the perspective of genes!\n\n")
	sentence(m, "Here is a full summary:\n")
	sentence(m, "https://learnfromnotes.com/index.php/2020/09/19/the-extended-selfish-gene-richard-dawkins-summary/")
	#sentence(m, "Would you sell your data?\nHow much money should you get to sell your data? \nWhat if it only was some of your data that you choose yourself?\n")
	#sentence(m, "What if the data is used for companies market research? What if the data is used for science?\n\n")
	#sentence(m, "Would love to hear your thoughts on this topic :D")




	#m.append(sentence("Hey everybody! :)\nWhat do you think of this guided meditation voice?\n- https://soundcloud.com/lars-pedersen-703978720/adhd-meditation-what-do-you-think-of-this-voice \n\n\nI'm the creator of the app \"Mindfulness for ADHD\", and am trying to find out if I should order more meditations from her, or from someone else, so PLEASE be honest! :)"))
	#m.append(sentence("Hey everybody! :) \n has anyone tried testing Oura ring against wearables like fitbit and smartphone apps?\nI'm trying to find something that is accurate enough to make experiments and trust the data. Has anyone tested Oura ring side to side with other sleep trackers?"))
	return m

############################ AND UNTIL HERE #######################################################################


def wait(atLeast, atMost):
	if not debug:
		sleep(randint(atLeast, atMost))

def sentence(m, text):
	m.append(Keys.ARROW_DOWN * 50 + text)

def bold():
	return Keys.CONTROL + 'b'

def postOnFacebook(driver, messages):
	#Elements:
	postBoxXPATH = "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div"


	#Open facebook
	driver.get("https://www.facebook.com")
	wait(shortA, shortB)

	#Enter Log-in information
	emailElement = driver.find_element(By.XPATH, './/*[@id="email"]')
	emailElement.send_keys(os.environ.get('EMAIL'))
	wait(shortA, shortB)
	passwordElement = driver.find_element(By.XPATH, './/*[@id="pass"]')
	passwordElement.send_keys(os.environ.get('PASSWORD2'))
	wait(shortA, shortB)

	#Login
	passwordElement.send_keys(Keys.RETURN)
	#WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, './/*[@id="navItem_217974574879787"]/a/div')))
	wait(shortA, shortB)

	#Post in all groups
	for link in groupLinksFacebook:
		#Open facebook group
		driver.get(link)
		wait(shortA, shortB)

		#Insert message
		postBox = driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
		postBox.send_keys(' ')
		WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, postBoxXPATH)))
		postBox = driver.find_element_by_xpath(postBoxXPATH)
		postBox.send_keys(Keys.DELETE)
		wait(shortA, shortB)


		for message in messages:
			print(message)
			#postBox = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div")
			postBox.send_keys(message)
			wait(shortA, shortB)
		
		for path in imagePaths:
			# Click on the add media button
			addMediaButton = driver.find_element_by_xpath("//*[contains(text(), 'Photo/Video')]")
			addMediaButton.click()
			sleep(5)

			# Click the 'Upload Photo/Video' button
			uploadPhotoButton = driver.find_element_by_xpath("//input[@type='file'][@class='_n _5f0v']")
			uploadPhotoButton.send_keys(path)
			
			# Wait for the image to upload
			sleep(5)
			wait(longA, longB)

		clickable = False
		while not clickable:
			try:
				postBox =  driver.find_element_by_xpath(postBoxXPATH)
				postBox.click()
				postBox.send_keys(Keys.CONTROL + Keys.ENTER)
				#ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
				print("using: " + Keys.CONTROL + Keys.ENTER)
				sleep(10)
				wait(longA, longB)
			except NoSuchElementException:
				clickable = True

		print("(Facebook) : succesfully posted to: " + link)
		#post_button.click()
		

		

def postOnReddit(driver, messages):
	#Open reddit
	driver.get("https://www.reddit.com/")

	#Login
	WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.LINK_TEXT, "LOG IN")))
	loginButton = driver.find_element_by_link_text("LOG IN")
	loginButton.click() 
	wait(shortA, shortB)

	iframe = driver.find_elements_by_tag_name("iframe")
	driver.switch_to.frame(1)
	try:
		usernameField = driver.find_element_by_id("loginUsername")
	except NoSuchElementException:
		driver.switch_to.default_content()
		driver.switch_to.frame(0)
		usernameField = driver.find_element_by_id("loginUsername")


	
	usernameField.send_keys(os.environ.get('USERNAMEOLD'))
	sleep(5)
	wait(shortA, shortB)
	passwordField = driver.find_element_by_id("loginPassword")
	passwordField.send_keys(os.environ.get('PASSWORD'))
	wait(shortA, shortB)
	loginButton2 = driver.find_element_by_class_name("AnimatedForm__submitButton")
	loginButton2.click()
	sleep(5)
	wait(shortA, shortB)
	
	#Post in subreddits
	for link in groupLinksReddit:

		sleep(11*60)
		wait(shortA, shortB)

		#Enter subreddit
		driver.get(link)
		sleep(5)
		wait(shortA, shortB)

		##"Create post" button
		createPostButton = driver.find_element_by_link_text("CREATE POST")
		createPostButton.click()
		wait(shortA, shortB)

		#Enter information
		WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.TAG_NAME, 'textarea')))
		titleField = driver.find_element_by_tag_name("textarea")
		titleField.send_keys(title)
		wait(shortA, shortB)

		

		bodyTextField = driver.find_element_by_class_name("public-DraftEditor-content")
		for text in messages:
			bodyTextField.send_keys(text)

		#Post
		postButton = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[3]/div[2]/div/div[1]/button')
		postButton.click()

		print("(Reddit) : succesfully posted to: " + link)
		


def openChrome():
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_experimental_option("detach", True)
	chrome_options.add_argument("--disable-infobars")
	chrome_options.add_argument("--start-maximized")
	chrome_options.add_experimental_option("prefs", { \
		"profile.default_content_setting_values.notifications": 2 # 1:allow, 2:block 
	})
	return webdriver.Chrome(options=chrome_options)

def main():
	messages = composeMessage()
	print("composeMessage: ")
	print(messages)

	driver = openChrome()
	postOnFacebook(driver, messages)
	#postOnReddit(driver, messages)


if __name__ == "__main__":
    main()
# WebDriverWait IN SELENIUM:-
It is applied on certain element with defined expected condition and time. This wait is only applied to the specified element. This wait can also throw exception when element is not found.

# EXPLICIT WAITS:-
An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code. The extreme case of this is time.sleep(), which sets the condition to an exact time period to wait. There are some convenience methods provided that help you write code that will wait only as long as required. Explicit waits are achieved by using webdriverWait class in combination with expected_conditions.


# EXPECTED CONDITIONS :–
There are some common conditions that are frequently of use when automating web browsers.
## The following are the Expected Conditions that can be used in Explicit Wait:
 
alertIsPresent()

elementSelectionStateToBe()

elementToBeClickable()

elementToBeSelected()

frameToBeAvaliableAndSwitchToIt()

invisibilityOfTheElementLocated()

invisibilityOfElementWithText()

presenceOfAllElementsLocatedBy()

presenceOfElementLocated()

textToBePresentInElement()

textToBePresentInElementLocated()

textToBePresentInElementValue()

titleIs()

titleContains()

visibilityOf()

visibilityOfAllElements()

visibilityOfAllElementsLocatedBy()

visibilityOfElementLocated()



# SYNTAX:-
### #import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

### #create webdriver object
driver = webdriver.Chrome()
	
### #get website by pasting it's URL 
driver.get("URL of website")
	
### #get element after explicitly waiting for few seconds(lets say x seconds)
element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.link_text, "Specific desired Tag"))
	)


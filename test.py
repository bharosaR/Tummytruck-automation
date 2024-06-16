import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


#Set up the Chrome WebDriver using WebDriver Manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Function to check if a string is a valid email address
def is_valid_email(email):
   try:
       # check email format using RE
       email_pattern = r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"


       if re.search(email_pattern,email):
           return True


       else:
           return False

   except Exception as e:
       print(e)
       return False


# Function to check if a string is a valid phone number
def is_valid_phone(phone):
   return bool(re.match(r'^\d{10}$', phone))

# Open the web page
driver.get("https://tummytruck.com.np/")

driver.maximize_window()

# set scroll parameters
target_y = 6000
scroll_distance = 1000
current_y = 0

time.sleep(2)

# loop to keep scrolling
while current_y < target_y:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

#Green Tummy Package (Rs. 4500)
#First Week
First_week_locator = (driver.find_element(*(By.XPATH,"//div[@id='menu']//div[2]//div[1]//a[1]//div[1]//span[1]//img[1]")))
First_week = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(First_week_locator))

time.sleep(2),

#First_week
driver.execute_script("arguments[0].scrollIntoView();", First_week)
time.sleep(2)

#Open the next web page
driver.get("https://tummytruck.com.np/menu/5/first%20week")

# set scroll parameters
target_y = 6000
scroll_distance = 1000
current_y = 0

time.sleep(2)

# loop to keep scrolling
while current_y < target_y:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

# Allow some time for the new page to stabilize
time.sleep(2)

# Navigate back
driver.back()

time.sleep(3)


#Second Week
Second_week_locator = (driver.find_element(*(By.XPATH,"//div[@id='menu']//div[2]//div[1]//a[2]//div[1]//span[1]//img[1]")))
Second_week = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Second_week_locator))

time.sleep(2),

#Second_week
driver.execute_script("arguments[0].scrollIntoView();", Second_week)
time.sleep(2)

#Open the next web page
driver.get("https://tummytruck.com.np/menu/5/second%20week")

# set scroll parameters
target_y = 6000
scroll_distance = 1000
current_y = 0

time.sleep(2)

# loop to keep scrolling
while current_y < target_y:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

# Allow some time for the new page to stabilize
time.sleep(2)

# Navigate back
driver.back()

time.sleep(3)



#Third Week
Third_week_locator = (driver.find_element(*(By.XPATH,"//div[@id='menu']//div[2]//div[1]//a[3]//div[1]//span[1]//img[1]")))
Third_week = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Third_week_locator))

time.sleep(2),

#Third_week
driver.execute_script("arguments[0].scrollIntoView();", Third_week)
time.sleep(2)

#Open the next web page
driver.get("https://tummytruck.com.np/menu/5/third%20week")

# set scroll parameters
target_y = 6000
scroll_distance = 1000
current_y = 0

time.sleep(2)

# loop to keep scrolling
while current_y < target_y:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

# Allow some time for the new page to stabilize
time.sleep(2)

# Navigate back
driver.back()

time.sleep(3)


#Fourth Week
Fourth_week_locator = (driver.find_element(*(By.XPATH,"//div[@id='menu']//div[2]//div[1]//a[4]//div[1]//span[1]//img[1]")))
Fourth_week = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Fourth_week_locator))

time.sleep(2),

#Fourth_week
driver.execute_script("arguments[0].scrollIntoView();", Fourth_week)
time.sleep(2)

#Open the next web page
driver.get("https://tummytruck.com.np/menu/5/fourth%20week")

# set scroll parameters
target_y = 6000
scroll_distance = 1000
current_y = 0

time.sleep(2)

# loop to keep scrolling
while current_y < target_y:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

# Allow some time for the new page to stabilize
time.sleep(2)

# Navigate back
driver.back()




#Yummy Tummy (Rs. 5000)
#First Week
First_week_locator = (driver.find_element(*(By.XPATH,"//div[3]//div[1]//a[1]//div[1]//span[1]//img[1]")))
First_week = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(First_week_locator))

time.sleep(2),

#First_week
driver.execute_script("arguments[0].scrollIntoView();", First_week)
time.sleep(2)

#Open the next web page
driver.get("https://tummytruck.com.np/menu/4/first%20week")

# set scroll parameters
target_y = 6000
scroll_distance = 1000
current_y = 0

time.sleep(2)

# loop to keep scrolling
while current_y < target_y:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

# Allow some time for the new page to stabilize
time.sleep(2)

# Navigate back
driver.back()

time.sleep(3)


#Second Week
Second_week_locator = (driver.find_element(*(By.XPATH,"//div[3]//div[1]//a[2]//div[1]//span[1]//img[1]")))
Second_week = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Second_week_locator))

time.sleep(2),

#Second_week
driver.execute_script("arguments[0].scrollIntoView();", Second_week)
time.sleep(2)

#Open the next web page
driver.get("https://tummytruck.com.np/menu/4/second%20week")

# set scroll parameters
target_y = 6000
scroll_distance = 1000
current_y = 0

time.sleep(2)

# loop to keep scrolling
while current_y < target_y:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

# Allow some time for the new page to stabilize
time.sleep(2)

# Navigate back
driver.back()

time.sleep(3)



#Third Week
Third_week_locator = (driver.find_element(*(By.XPATH,"//div[3]//div[1]//a[3]//div[1]//span[1]//img[1]")))
Third_week = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Third_week_locator))

time.sleep(2),

#Third_week
driver.execute_script("arguments[0].scrollIntoView();", Third_week)
time.sleep(2)

#Open the next web page
driver.get("https://tummytruck.com.np/menu/4/third%20week")

# set scroll parameters
target_y = 6000
scroll_distance = 1000
current_y = 0

time.sleep(2)

# loop to keep scrolling
while current_y < target_y:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

# Allow some time for the new page to stabilize
time.sleep(2)

# Navigate back
driver.back()

time.sleep(3)


#Fourth Week
Fourth_week_locator = (driver.find_element(*(By.XPATH,"//div[3]//div[1]//a[4]//div[1]//span[1]//img[1]")))
Fourth_week = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Fourth_week_locator))

time.sleep(2),

#Fourth_week
driver.execute_script("arguments[0].scrollIntoView();", Fourth_week)
time.sleep(2)

#Open the next web page
driver.get("https://tummytruck.com.np/menu/4/fourth%20week")

# set scroll parameters
target_y = 6000
scroll_distance = 1000
current_y = 0

time.sleep(2)

# loop to keep scrolling
while current_y < target_y:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

# Allow some time for the new page to stabilize
time.sleep(2)

# Navigate back
driver.back()




#Pro Tummy Package (Rs. 6000)
#First Week
First_week_locator = (driver.find_element(*(By.XPATH,"//div[4]//div[1]//a[1]//div[1]//span[1]//img[1]")))
First_week = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(First_week_locator))

time.sleep(2),

#First_week
driver.execute_script("arguments[0].scrollIntoView();", First_week)
time.sleep(2)

#Open the next web page
driver.get("https://tummytruck.com.np/menu/6/first%20week")

# set scroll parameters
target_y = 6000
scroll_distance = 1000
current_y = 0

time.sleep(2)

# loop to keep scrolling
while current_y < target_y:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

# Allow some time for the new page to stabilize
time.sleep(2)

# Navigate back
driver.back()

time.sleep(3)


#Second Week
Second_week_locator = (driver.find_element(*(By.XPATH,"//div[4]//div[1]//a[2]//div[1]//span[1]//img[1]")))
Second_week = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Second_week_locator))

time.sleep(2),

#Second_week
driver.execute_script("arguments[0].scrollIntoView();", Second_week)
time.sleep(2)

#Open the next web page
driver.get("https://tummytruck.com.np/menu/6/second%20week")

# set scroll parameters
target_y = 6000
scroll_distance = 1000
current_y = 0

time.sleep(2)

# loop to keep scrolling
while current_y < target_y:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

# Allow some time for the new page to stabilize
time.sleep(2)

# Navigate back
driver.back()

time.sleep(3)



#Third Week
Third_week_locator = (driver.find_element(*(By.XPATH,"//div[4]//div[1]//a[3]//div[1]//span[1]//img[1]")))
Third_week = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Third_week_locator))

time.sleep(2),

#Third_week
driver.execute_script("arguments[0].scrollIntoView();", Third_week)
time.sleep(2)

#Open the next web page
driver.get("https://tummytruck.com.np/menu/6/third%20week")

# set scroll parameters
target_y = 6000
scroll_distance = 1000
current_y = 0

time.sleep(2)

# loop to keep scrolling
while current_y < target_y:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

# Allow some time for the new page to stabilize
time.sleep(2)

# Navigate back
driver.back()

time.sleep(3)


#Fourth Week
Fourth_week_locator = (driver.find_element(*(By.XPATH,"//div[4]//div[1]//a[4]//div[1]//span[1]//img[1]")))
Fourth_week = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Fourth_week_locator))

time.sleep(2),

#Fourth_week
driver.execute_script("arguments[0].scrollIntoView();", Fourth_week)
time.sleep(2)

#Open the next web page
driver.get("https://tummytruck.com.np/menu/6/fourth%20week")

# set scroll parameters
target_y = 6000
scroll_distance = 1000
current_y = 0

time.sleep(2)

# loop to keep scrolling
while current_y < target_y:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

# Allow some time for the new page to stabilize
time.sleep(2)

# Navigate back
driver.back()

time.sleep(3)


#Contact_Us
driver.get("https://tummytruck.com.np/contactus")


#Name
Your_name = driver.find_element(*(By.XPATH,"//input[@id='name']"))

#Contact
Your_contact = driver.find_element(*(By.XPATH,"//input[@id='contact']"))

#Query
Your_query = driver.find_element(*(By.XPATH,"//textarea[@id='query']"))


# Example values
name = "Jasmine"
contact = "9772188832"
query = "Which diet is suitable for weight loss?"


# Clear the field and enter the last name value
Your_name.clear()
Your_name.send_keys(name)
time.sleep(3)

# Clear the field and enter the contact value
Your_contact.clear()
Your_contact.send_keys(contact)
time.sleep(3)

# Clear the field and enter your query
Your_query.clear()
Your_query.send_keys(query)
time.sleep(3)

# Navigate back
driver.back()

# Add another sleep
time.sleep(3)

#email
email_field = driver.find_element(*(By.XPATH,"//input[@id='email']"))

#example input
email = "jasmine20@gmail.com"

# Check if the email address is valid
if is_valid_email(email):
   print("Valid email address")
else:
   print("Invalid email address")

# Clear the field and enter the email value
email_field.clear()
email_field.send_keys(email)

time.sleep(3)

# Close the WebDriver
driver.quit()
print("Congrats!! code run successfully")

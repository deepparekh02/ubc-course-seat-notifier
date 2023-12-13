from selenium import webdriver
import time
import smtplib
from email.message import EmailMessage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Function to send email
def send_email(email, password, seat_type, subject, course, section):
    msg = EmailMessage()
    msg.set_content("A " + seat_type + " seat is available in {subject} {course} {section}! Go register now!".format(subject=subject, course=course, section=section))

    msg['Subject'] = 'Seat Availability Notification for ' + subject + ' ' + course + ' ' + section
    msg['From'] = email
    msg['To'] = email

    # Replace 'smtp.example.com' with your email provider's SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # Example for Gmail
        smtp.login(email, password)
        smtp.send_message(msg)

# User input for URL and email

subject = input("Enter the subject area (E.g. COMM): ")
course = input("Enter the course number (E.g. 203): ")
section = input("Enter the section number (E.g. 205): ")
url = "https://www.courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept={subject}&course={course}&section={section}".format(subject=subject, course=course, section=section)
seat_type = input("Enter seat type (general/restricted): ")
email_id = input("Enter your email ID (Gmail only): ")
password = input("Enter your app password (more info in README): ")
my_pwd = "ghuy uzfa jgdy zakz"
time_check = int(input("How frequently do you want to check for seat availability (in minutes)?"))

# Set Chrome options for headless mode
chrome_options = Options()
# chrome_options.add_argument("--headless")

# Initialize the Chrome driver in headless mode
driver = webdriver.Chrome(options=chrome_options)

# Main loop
while True:
    driver.get(url)
    if seat_type.lower() == 'general':
        wait = WebDriverWait(driver, 20)
        element_locator = (By.XPATH, '/html/body/div[2]/div[4]/table[4]/tbody/tr[3]/td[2]/strong')
        table = wait.until(EC.visibility_of_element_located(element_locator))
        seat_element = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/table[4]/tbody/tr[3]/td[2]/strong')
        seats_available = int(seat_element.text)
    elif seat_type.lower() == 'restricted':
        wait = WebDriverWait(driver, 20)
        element_locator = (By.XPATH, '/html/body/div[2]/div[4]/table[4]/tbody/tr[4]/td[2]/strong')
        table = wait.until(EC.visibility_of_element_located(element_locator))
        seat_element = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/table[4]/tbody/tr[4]/td[2]/strong')
        seats_available = int(seat_element.text)

    # Check if seats are available and send email
    if seats_available > 0:
        print("FOUND!")
        send_email(email_id, password, seat_type, subject, course, section)
        
    time.sleep(time_check * 60)


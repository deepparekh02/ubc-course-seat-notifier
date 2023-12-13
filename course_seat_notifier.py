from selenium import webdriver
import time
import smtplib
from email.message import EmailMessage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Function to send email
def send_email(sender_email, recipient_email, password, seat_type, subject, course, section, url):
    msg = EmailMessage()
    msg.set_content("A " + seat_type + " seat is available in {subject} {course} {section}! Go register now on {url}".format(subject=subject, course=course, section=section, url=url))

    msg['Subject'] = 'Seat Availability Notification for ' + subject + ' ' + course + ' ' + section
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Replace 'smtp.example.com' with your email provider's SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, password)
        smtp.send_message(msg)

# User input
subject = input("Enter the subject area (E.g. COMM): ")
course = input("Enter the course number (E.g. 203): ")
section = input("Enter the section number (E.g. 205): ")
url = "https://www.courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept={subject}&course={course}&section={section}".format(subject=subject, course=course, section=section)
seat_type = input("Enter seat type (general/restricted): ")
sender_email = input("Enter the sender's email ID (Gmail only): ")
password = input("Enter the sender's app password (more info in README): ")
same_email = input("Do you want to send the email to a different email ID (Y/N)? ")
recipient_email = ''
if same_email.lower() == 'y':
    recipient_email = input("Enter the recipient's email ID: ")
else:
    recipient_email = sender_email
time_check = int(input("How frequently do you want to check for seat availability (in minutes) (min = 2)?"))
time_check = min(time_check, 2)

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

element_path = ''
if seat_type.lower() == 'restricted':
    element_path = '/html/body/div[2]/div[4]/table[4]/tbody/tr[4]/td[2]/strong'
else:
    element_path = '/html/body/div[2]/div[4]/table[4]/tbody/tr[3]/td[2]/strong'

# Main loop
while True:
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    element_locator = (By.XPATH, element_path)
    table = wait.until(EC.visibility_of_element_located(element_locator))
    seat_element = driver.find_element(By.XPATH, element_path)
    seats_available = int(seat_element.text)

    # Check if seats are available and send email
    if seats_available > 0:
        print("FOUND!")
        send_email(sender_email, recipient_email, password, seat_type, subject, course, section, url)
        
    time.sleep(time_check * 60)


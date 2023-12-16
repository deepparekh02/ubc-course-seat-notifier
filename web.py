import smtplib
from email.message import EmailMessage
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def check_seats(subject, course, section, seat_type, sender_email, password, recipient_email, url, time_input):
    # Selenium setup
    time_check = max(time_input, 2)
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)

    element_path = ''
    if seat_type.lower() == 'Restricted':
        element_path = '/html/body/div[2]/div[4]/table[4]/tbody/tr[4]/td[2]/strong'
    else:
        element_path = '/html/body/div[2]/div[4]/table[4]/tbody/tr[3]/td[2]/strong'

    email_sent = False
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
            if (not email_sent):
                send_email(sender_email, recipient_email, password, seat_type, subject, course, section, url, str(seats_available))
            time_check = max(time_input, 60)
            email_sent = True
        else:
            time_check = max(time_input, 2)
            email_sent = False
            
        time.sleep(time_check * 60)
        
def send_email(sender_email, recipient_email, password, seat_type, subject, course, section, url, seats_available):
    msg = EmailMessage()
    msg.set_content(seats_available + " " + seat_type + " seat(s) are available in {subject} {course} {section}! Go register now on {url}".format(subject=subject, course=course, section=section, url=url))

    msg['Subject'] = 'Seat Availability Notification for ' + subject + ' ' + course + ' ' + section
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Replace 'smtp.example.com' with your email provider's SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, password)
        smtp.send_message(msg)
from selenium import webdriver
import time
import smtplib
from email.message import EmailMessage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from multiprocessing import Process, Manager
from tkinter import *
from tkinter import ttk
import json
import os
import platform

# Function to send email
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

def check_seats_and_send_email(subject, course, section, seat_type, sender_email, password, recipient_email, url, time_input):
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
                send_email(sender_email, recipient_email, password, seat_type, subject, course, section, url, seats_available)
            time_check = max(time_input, 60)
            email_sent = True
        else:
            time_check = max(time_input, 2)
            email_sent = False
            
            
        time.sleep(time_check * 60)

process_num = 0
processes = []
        
def create_gui():
    window = Tk()
    window.title("Course Seat Notifier")

    # Add padding and spacing to the window
    for i in range(9):
        window.grid_rowconfigure(i, pad=10)
    for i in range(2):
        window.grid_columnconfigure(i, pad=10)

    # Create labels and entry fields with padding
    Label(window, text="Sender Email").grid(row=0, padx=10, pady=2)
    Label(window, text="Password (more info in README)").grid(row=1, padx=10, pady=2)
    Label(window, text="Subject (E.g. COMM)").grid(row=2, padx=10, pady=2)
    Label(window, text="Course (E.g. 205)").grid(row=3, padx=10, pady=2)
    Label(window, text="Section (E.g. 202)").grid(row=4, padx=10, pady=2)
    Label(window, text="Seat Type (General/Restricted)").grid(row=5, padx=10, pady=2)
    Label(window, text="Recipient Email").grid(row=6, padx=10, pady=2)
    Label(window, text="Time Input (minutes - min 2)").grid(row=7, padx=10, pady=2)

    # Create entry fields
    sender_email = Entry(window)
    password = Entry(window, show="*")
    subject = Entry(window)
    course = Entry(window)
    section = Entry(window)
    seat_type = Entry(window)
    recipient_email = Entry(window)
    time_input = Entry(window)

    # Grid entry fields with padding
    sender_email.grid(row=0, column=1, padx=10, pady=2)
    password.grid(row=1, column=1, padx=10, pady=2)
    subject.grid(row=2, column=1, padx=10, pady=2)
    course.grid(row=3, column=1, padx=10, pady=2)
    section.grid(row=4, column=1, padx=10, pady=2)
    seat_type.grid(row=5, column=1, padx=10, pady=2)
    recipient_email.grid(row=6, column=1, padx=10, pady=2)
    time_input.grid(row=7, column=1, padx=10, pady=2)
    
    
    def load_and_start_processes():
        # Load existing data
        global all_fields
        try:
            if os.path.getsize('data/save.json') > 0:
                with open('data/save.json', 'r') as f:
                    all_fields = json.load(f)
        except FileNotFoundError:
            pass

        # Start a process for each entry
        for entry in all_fields:
            p = Process(target=check_seats_and_send_email, args=(entry['subject'], entry['course'], entry['section'], entry['seat_type'], entry['sender_email'], entry['password'], entry['recipient_email'], entry['url'], int(entry['time_input'])))
            p.start()
            entry['pid'] = p.pid
            course_name = entry['subject'] + " " + entry['course'] + " " + entry['section']
            treeview.insert('', 'end', values=(course_name, entry['seat_type'], entry['sender_email'], entry['password'], entry['recipient_email'], entry['time_input']))
      
    def start_process():
        global all_fields
        subject1 = subject.get()
        course1 = course.get()
        section1 = section.get()
        url = "https://www.courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept={subject1}&course={course1}&section={section1}".format(subject1=subject1, course1=course1, section1=section1)
        # Create a dictionary for the current entry
        current_entry = {
            'subject': subject.get(),
            'course': course.get(),
            'section': section.get(),
            'url': url,
            'sender_email': sender_email.get(),
            'password': password.get(),
            'seat_type': seat_type.get(),
            'recipient_email': recipient_email.get(),
            'time_input': time_input.get()
        }
        
    # ghuy uzfa jgdy zakz
        
        # Start a new process for the current entry
        p = Process(target=check_seats_and_send_email, args=(subject.get(), course.get(), section.get(), seat_type.get(), sender_email.get(), password.get(), recipient_email.get(), url, int(time_input.get())))
        p.start()
        
        current_entry['pid'] = p.pid

        # Add the current entry to all_fields
        all_fields.append(current_entry)

        # Save data
        with open('data/save.json', 'w') as f:
            json.dump(list(all_fields), f)
        
        course_name = subject.get() + " " + course.get() + " " + section.get()
        treeview.insert('', 'end', values=(course_name, seat_type.get(), sender_email.get(), password.get(), recipient_email.get(), time_input.get()))
        
        # Clear the textboxes
        subject.set('')
        course.set('')
        section.set('')
        seat_type.set('')
        time_input.set('')
    
    def delete_process():
        # Get the selected item
        selected_item = treeview.selection()[0]
        values = treeview.item(selected_item, 'values')

        # Remove the selected item from the treeview
        treeview.delete(selected_item)

        # Create a dictionary for the selected entry
        selected_entry = {
            'subject': values[0].split()[0],
            'course': values[0].split()[1],
            'section': values[0].split()[2],
            'seat_type': values[1],
            'sender_email': values[2],
            'password': values[3],
            'recipient_email': values[4],
            'time_input': values[5]
        }

        # Remove the selected entry from all_fields
        all_fields.remove(selected_entry)
        
            # Stop the process
        if platform.system() == 'Windows':
            os.system(f'taskkill /PID {selected_entry["pid"]} /F')
        else:
            os.kill(selected_entry['pid'], signal.SIGTERM)

        # Save data
        with open('data/save.json', 'w') as f:
            json.dump(all_fields, f) 
               
    # Create the start button
    Button(window, text="Add", command=start_process).grid(row=9, column=0, columnspan=2, sticky='ew', pady=4)
    # Create the Delete button
    Button(window, text="Delete", command=delete_process).grid(row=10, column=0, columnspan=2, sticky='ew', pady=4)
    
    # Create the table
    columns = ('#1', '#2', '#3', '#4', '#5', '#6')
    treeview = ttk.Treeview(window, columns=columns, show='headings')
    treeview.heading('#1', text='Course')
    treeview.heading('#2', text='Seat Type')
    treeview.heading('#3', text='Sender Email')
    treeview.heading('#4', text='Password')
    treeview.heading('#5', text='Recipient Email')
    treeview.heading('#6', text='Time Input')
    treeview.grid(row=11, column=0, columnspan=2)
    
    load_and_start_processes()

    window.mainloop()
    
if __name__ == '__main__':
    manager = Manager()
    all_fields = manager.list()
    create_gui()
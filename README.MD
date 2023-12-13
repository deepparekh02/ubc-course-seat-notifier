# Course Seat Availability Notifier

## Introduction
This Python script automates the process of checking for seat availability in university courses. It periodically monitors a specified course's seat availability on the university's course schedule page and sends an email notification when a seat becomes available.


## Installation Instructions
1. **Install Python**: 
   - Download Python from the [official Python website](https://www.python.org/downloads/).
   - Follow the installation instructions for your operating system.

2. **Install Selenium and WebDriver**:
   - Open a terminal or command prompt.
   - Install Selenium by running `pip install selenium`.
   - Install the Chrome WebDriver by running `pip install chromedriver-py`.

## Configuration
- **Email Setup**: Provide your Gmail credentials in the script to enable sending notifications.
- **App Password**: 
   - Visit your [Google Account's security page](https://myaccount.google.com/security).
   - Ensure 2-Step Verification is turned on.
   - Enter "App Passwords" in the search bar.
   - Enter "Course Bot" or any other name in the App Name box.
   - Press Create
   - Copy the app password and store it in a secure location - You will not get to see it again.
   - Use this App Password in the script where required.

## Usage Instructions
1. **Running the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script using `python course_seat_notifier.py`.

2. **Input Parameters**: Upon running the script, input the details as prompted.
   - NOTE (IMPORTANT): If a seat is available for a long time, the code will keep spamming your account every time interval you have chosen.

## Running the Script Continuously
- **Keep Terminal Open**: For the script to run continuously and monitor seat availability, the terminal or command prompt where the script is running must be kept open.
- **Background Running**: If you close the terminal or command prompt, the script will stop running. To keep the script running in the background, you can minimize the terminal window.
- **Concurrent Running**: Running multiple instances of the script for different courses or sections is possible. Open a new terminal for each instance and run the script with different input parameters.


# Course Seat Availability Notifier

<img src="https://github.com/deepparekh02/ubc-course-seat-notifier/assets/65657471/90c5ccde-c004-42cf-bec1-155d29bca579" width=300>

## Introduction
This Python script automates the process of checking for seat availability in UBC courses. It periodically monitors a specified course's seat availability on the university's course schedule page and sends an email notification with the course page link when a seat becomes available.
<img width="1189" alt="screenshot" src="https://github.com/deepparekh02/ubc-course-seat-notifier/assets/65657471/3b53945c-d97f-47c5-a84b-55bf4f80343f">


## Overview of Modules
- **main.py**: Main entry point, integrating modules for primary functionality.
- **process.py**: Manages data processing and seat availability checks.
- **ui.py**: Handles user interface aspects like input prompts and messages.
- **web.py**: Responsible for web-related tasks, including web scraping and notifications.

## Query Saving and Reloading
This application includes a convenient feature to save your search queries. When you input your course details and other parameters, the app saves these queries locally. The next time you open the app, it automatically reloads your last queries. This saves time and effort, especially for users who need to monitor the same courses regularly.

### How It Works
- **Saving Queries**: Each time you run a query, the app saves the parameters in a local file.
- **Reloading Queries**: Upon restarting the app, it checks for saved queries and pre-loads them for your convenience.
- **Managing Queries**: You can choose to add, delete, or continue with the pre-loaded queries.

## Multiprocessing and Concurrent Query Handling
The application is designed with multiprocessing capabilities, allowing it to handle multiple queries simultaneously. This means you can monitor several courses at once without affecting the performance or speed of each individual query.

## Installation Instructions
1. **Install Python3**: 
   - Download Python3 from the [official Python website](https://www.python.org/downloads/).
   - Follow the installation instructions for your operating system.

2. **Install Selenium and WebDriver**:
   - Open a terminal or command prompt.
   - Install Selenium by running `pip3 install selenium`.
   - Note: Needs Chrome Installed.

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
   - Navigate to the directory containing the script. (use cd path-to-directory)
   - Run the script using `python3 main.py`.

2. **Input Parameters**: Upon running the script, input the details as prompted.
   - **Subject Area**: E.g., COMM
   - **Course Number**: E.g., 203
   - **Section Number**: E.g., 205
   - **Seat Type**: Choose between 'general' or 'restricted'.
   - **Sender Email ID**: Your Gmail ID.
   - **App Password**: The app password generated for your Gmail account.
   - **Recipient Email ID**: The email you want to send the notification to.
   - **Check Frequency**: Frequency of seat availability checks (in minutes).

## Running the Script Continuously
- **Keep App Open**: For the App to run continuously and monitor seat availability, it must be kept open
- **Background Running**: If you close the app, the script will stop running. To keep the script running in the background, you can minimize it.
- **Concurrent Running**: Just add a new entry to the app to keep track of multiple courses with different emails if needed.


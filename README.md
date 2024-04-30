Ravens Roost Application Status Notifier

Overview
This Python script automates the monitoring of the Ravens Roost job application status at Carleton University. It checks the website for changes in the application status and sends an email notification when the status is updated. This script is intended to help potential applicants keep track of the application opening, ensuring they can apply as soon as it becomes available.

Features
- Automated checks: The script visits the Carleton Ravens Roost application page and checks for updates in the application status.
- Email notifications: Sends an automated email to a specified address when the application status changes.

Requirements
- Python 3
- Libraries: requests, lxml, smtplib, email.mime.text, email.mime.multipart, dotenv
- A .env file containing credentials for the email functionality

Setup and Installation
1. Ensure Python 3 is installed on your system.
2. Clone this repository to your local machine.
3. Install the required Python libraries:
   pip install requests lxml python-dotenv
4. Create a .env file in the root directory of the project with the following variables:
   MY_EMAIL = your-email@gmail.com
   GOOGLE_APP_PASSWORD = your-generated-app-password

Usage
To run the script, navigate to the project directory and execute:
   python main.py



Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your proposed changes.

License
This project is released under the MIT License. See the LICENSE file for more details.

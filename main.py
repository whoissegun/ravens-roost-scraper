import requests
from lxml import html
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()
url = "https://housing.carleton.ca/current-residents/get-involved/ravens-roost/"


def send_email(subject, body):
    message = MIMEMultipart()
    message["From"] = os.getenv("MY_EMAIL")
    message["To"] = os.getenv("MY_EMAIL")
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(os.getenv("MY_EMAIL"), os.getenv("GOOGLE_APP_PASSWORD"))
        text = message.as_string()
        server.sendmail(os.getenv("MY_EMAIL"), os.getenv("MY_EMAIL"), text)
        print("Email sent successfully!")
    except Exception as e:
        print("Email could not be sent:", e)
    finally:
        server.quit()

def main(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if status is not 200
        
        tree = html.fromstring(response.content)  # Parse the HTML content
        xPath = "/html/body/div[2]/div[2]/main/article/h2[3]"
        
        application_status_elements = tree.xpath(xPath)

        if application_status_elements:
            
            app_status = application_status_elements[0].text_content()
            print("Application Status:", app_status)
            if "Closed" in app_status:
                send_email("Ravens Roost Application Status Update", "Application is still closed.")
            else:
                send_email("Ravens Roost Application Status Update", "Application is finally open. GO APPLY!!!!")
        else:
            print("No application status found with the given XPath.")

    except requests.exceptions.RequestException as e:
        print("HTTP Request failed:", e)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main(url)

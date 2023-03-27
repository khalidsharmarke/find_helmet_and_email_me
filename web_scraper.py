import os
from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
load_dotenv()

driver = webdriver.Chrome()
driver.get(os.getenv("WEBSITE_URL"))
add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn-addtocart")

if add_to_cart_button.text == "ADD TO CART":
    driver.close()
    msg = EmailMessage()
    msg['From'] = os.getenv("EMAIL")
    msg['To'] = os.getenv("EMAIL")
    msg['Subject'] = "YOUR ITEM IS NOW AVAILABLE TO PURCHASE"
    msg.set_content(os.getenv("WEBSITE_URL"))
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.getenv("EMAIL"), os.getenv("APP_PASSWORD"))
        smtp.send_message(msg)

    print('here')
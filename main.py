import smtplib


from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
from pyexpat.errors import messages

load_dotenv()

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7,bn;q=0.6",
    "Dnt": "1",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
}
response = requests.get(practice_url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
#print(soup.prettify())
price = soup.find(class_="aok-offscreen").get_text()

price_without_currency = price.split("$")[1]
#print(price_without_currency)

price_as_float =float(price_without_currency)
print(price_as_float)
title = soup.find(id="productTitle").get_text().strip()
print(title)
BUY_PRICE = 100
if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"],port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"],os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{practice_url}".encode("utf-8")
        )

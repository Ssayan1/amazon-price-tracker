# Amazon Price Tracker

A Python script that tracks Amazon product prices and sends an email alert when the price drops below a set value.

## Features
- Scrapes Amazon product page
- Sends email alert via SMTP
- Uses dotenv for environment variables

## Setup
1. Clone the repo
2. Run `pip install -r requirements.txt`
3. Create a `.env` file with:
```bash
EMAIL_ADDRESS=your_email
EMAIL_PASSWORD=your_password
SMTP_ADDRESS=smtp.gmail.com
```
4. Run the script:
```bash
main.py
```
5.Save a requirements.txt file:
```nginx
requests
beautifulsoup4
python-dotenv
```

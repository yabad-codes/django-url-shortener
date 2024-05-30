# URL Shortener Django Project

## Project Overview

This project is a URL shortener application built with Django. Users can sign up and log in to add URLs they want to shorten. Each URL has a copy button and a counter for the number of views. Users can view statistics of clicks over time using Chart.js.

## Features

- User Registration and Authentication
- URL Shortening
- URL View Count Tracking
- URL Metadata Fetching (Title, Description, Favicon)
- Click Statistics with Chart.js

## User Stories

1. **User Registration and Login:**
   - A user can sign up with an email and password.
   - A user can log in with valid credentials.

### index page
<img width="1630" alt="Screen Shot 2024-05-30 at 2 25 30 PM" src="https://github.com/yabad-codes/django-url-shortener/assets/103969464/b68533e3-76d4-4edc-868a-68de6d401595">

### signup page
<img width="1620" alt="Screen Shot 2024-05-30 at 2 24 51 PM" src="https://github.com/yabad-codes/django-url-shortener/assets/103969464/ad95a0be-d15a-4898-bf7e-1352a2303371">

### login page
<img width="1619" alt="Screen Shot 2024-05-30 at 2 25 09 PM" src="https://github.com/yabad-codes/django-url-shortener/assets/103969464/719277e9-ff8e-4dfb-8e4b-f99bd4168ce3">

2. **Add URLs:**
   - Once logged in, a user can add URLs they want to shorten.
   - The shortened URL is displayed with a copy button.

### home page
<img width="1686" alt="Screen Shot 2024-05-30 at 2 28 55 PM" src="https://github.com/yabad-codes/django-url-shortener/assets/103969464/9e3d79ac-a458-43bf-a41a-0ecd28c2da25">

### adding a url
<img width="1683" alt="Screen Shot 2024-05-30 at 2 31 56 PM" src="https://github.com/yabad-codes/django-url-shortener/assets/103969464/afcfc631-7fd6-4710-9a99-7f18f1c601af">

3. **URL List:**
   - The user sees a list of their shortened URLs with a view counter.
   - Clicking on the view counter takes the user to the statistics page.

### views counter
<img width="736" alt="Screen Shot 2024-05-30 at 2 33 23 PM" src="https://github.com/yabad-codes/django-url-shortener/assets/103969464/7ddb92c2-164f-407c-ba3f-40ba2f8b7f33">

### copy button
<img width="734" alt="Untitled" src="https://github.com/yabad-codes/django-url-shortener/assets/103969464/1f0d6e27-6fd6-47f5-8e8c-0ac98ea2e9c9">


4. **View URL Statistics:**
   - The statistics page displays a chart showing when the clicks happened using Chart.js.
  
### URL Statistics
<img width="1689" alt="Screen Shot 2024-05-30 at 2 38 06 PM" src="https://github.com/yabad-codes/django-url-shortener/assets/103969464/23e87c38-e1a6-4ee7-bf24-b0ed6687808c">


## Prerequisites

- Python 3.12.2
- Django 5.0.6 or higher
- Chart.js
- Docker

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yabad-codes/django-url-shortener.git
   cd django-url-shortener
   python -m venv virt
   source virt/bin/activate
   pip install django
   pip install psycopg2-binary
   pip install bs4
   pip install requests
2. **Setup the database:**
   ```bash
   docker run -d --name postgres-server -p 5432:5432 -e POSTGRES_PASSWORD=create_your_db_password postgres:latest
3. **Create a database called url_shortener**
4. **Add these env variables:**
   ```bash
   export DB_NAME=url_shortner
   export DB_USER=postgres
   export DB_PASSWORD=your_db_password
   export DB_HOST=localhost
   export DB_PORT=5432
5. **Migrate to DATABASE:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
6. **Launch app:**
   ```bash
   python manage.py runserver

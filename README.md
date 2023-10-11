# Online-Shop-Project

## Project Description:
This project aimed to create an online shopping platform for a mock store. 
The website displays the online stores available items with images and prices. It allows the user to select an item, view the physical stores that has this specific item in stock, and allows the user to reserve their item until pick-up. The website requires the user to be logged in, and will therefore redirect to the login page as required.

## Table of Contents:
1. Installation Steps Using Vitual Environment
2. Installation Steps Using Docker
3. User Guide
4. Credits

## 1. Installation Steps Using Virtual Environment:

1. Clone the respository to your local machine:
   *git clone https://github.com/miekenel/online-shop-project.git*
   
2. Change to the project directory:
   *cd your-project*
  
3. Create a virtual environment:
   *python -m venv venv*

4. Activate the virual environment:
   *cd venv\Scripts\activate*

5. Install project dependencies:
   *pip install -r requirements.txt*

6. Apply migrations:
   *python manage.py migrate*

7. Create a superuser:
   *python manage.py createsuperuser*

8. Start the development server:
   *python manage.py runserver*

9. Open your web browser and go to "http://localhost:8000" to go to the website.

## 2. Installation Steps Using Docker:

1. Clone the respository to your local machine:
   *git clone https://github.com/miekenel/hyperion-consolidation.git*
   
2. Change to the project directory:
   *cd mysite*

3. Build the Docker Image:
    *docker build -t mysite .*

4. Run the Docker Container:
    *docker run -p 8000:8000 mysite*

5. Open your web browser and go to "http://localhost:8000" to go to the website.

## 3. User Guide

* Brows the website to view available products.
  
![image](https://github.com/MiekeNel/Online-Shop-Project/assets/98015730/046b9a15-bf9a-4730-bc76-829d87766503)

* Click on the "View Details" button of the product you are interested in.
* If you are logged out, you will be redirected to the login page where you can login. If you are not registered as a superuser, please revert back to step **7** of the Installation Steps.
  
![image](https://github.com/MiekeNel/Online-Shop-Project/assets/98015730/262117a2-d434-4b5e-bf79-8ddaa372e496)

* After loging in you will be able to select the item and subsequently the store at which you would like to reserve the item for pick-up.
* After selecting the desired store, click on the "Reserve Mine!" button to reserve your item in the selected store.
  
![image](https://github.com/MiekeNel/Online-Shop-Project/assets/98015730/928c6ca7-aa59-4774-aa3f-cf7c525d4beb)

* Once reserved, there will be a confirmation message as below, and a "Continue Shopping" button which will take you back to the main page of the shopping site.
  
![image](https://github.com/MiekeNel/Online-Shop-Project/assets/98015730/2d05f203-da1f-43f3-ae81-85739ed47539)

## 4. Credits
Author: Mieke Nel, https://github.com/MiekeNel

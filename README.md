## Admin ##
## Username: 
   ArnasZv
## Password:
   AT290519*


#  Clothing Shop Web Application
### Frameworks Module – College Project Submission

##  Overview
The **Clothing Shop Web Application** is a fully functional e-commerce platform developed using the **Django framework** with a **PostgreSQL database** (locally using SQLite for development). The system demonstrates the integration of modern web technologies, including **Bootstrap, JavaScript, and Django’s MVC architecture**, while showcasing secure user management, data storage, and hosting readiness.

This project fulfills all the **Frameworks Assessment** criteria, highlighting proficiency in **Django concepts, database integration, authentication and authorization**, and **front-end responsiveness** through a well-structured, modular web application.

---

##  Project Objectives
1. **Demonstrate** the application of Django as a full-stack web development framework.  
2. **Integrate** a relational database for structured data storage and management.  
3. **Implement** authentication and authorization systems to manage user roles securely.  
4. **Design** a responsive and interactive interface using Bootstrap and JavaScript.  
5. **Deploy** a hosted Django web application using Render, ensuring full accessibility.  

---

##  Application Architecture
### **Backend Framework:** Django 5.2  
### **Database:** PostgreSQL (SQLite used in development)  
### **Frontend Technologies:** HTML5, CSS3, Bootstrap 5, JavaScript  
### **Hosting Environment:** Render (via `Procfile` and `render.yaml`)  

The application is divided into multiple Django apps, ensuring modularity and scalability.

---

##  Project Structure
```
Clothing_shop/
│
├── clothing_shop/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py / asgi.py
│
├── shop/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/shop/
│   ├── static/shop/
│
├── users/
│   ├── models.py / views.py
│   ├── urls.py
│   ├── templates/users/
│
├── media/products/
│
├── manage.py
├── requirements.txt
├── Procfile
├── render.yaml
├── db.sqlite3
└── README.md
```

---

##  Core Features
###  **User Management**
- Registration and authentication via Django’s built-in system.  
- Profile management with editable user information.  
- Email-based password reset functionality (via `auth_views`).  
- Role-based permissions (regular users vs. admin staff).  

###  **Product and Category Management**
- Products organized into **categories** (`Category` model).  
- Each product includes name, slug, description, price, and inventory count.  
- Multiple images handled through inline model relationships (`ProductImageInline`).  

###  **Cart, Orders, and Checkout**
- Add/remove items from a shopping cart (`CartItem` model).  
- Orders processed with customer details, address, payment method, and total cost.  
- Linked `OrderItem` entries for each order line.  

###  **Favourites and Support**
- Save favourite items (`Favourite` model).  
- Submit **Support Messages** via form; managed in admin interface.  

###  **Messaging and Admin Features**
- Admin interface includes product and order management.  
- View and manage support messages (`SupportMessageAdmin`).  

###  **User Interface and Responsiveness**
- Responsive Bootstrap 5 design.  
- Shared templates for header, footer, and navigation.  
- JavaScript for validation and dynamic UI.  

###  **Security and Data Protection**
- Password encryption with Django hashing.  
- CSRF protection and session security.  
- Role-based access and `.env` configuration.  

---

##  Database Schema Overview
| Table | Description |
|-------|--------------|
| `auth_user` | Default Django user table |
| `shop_category` | Product categories |
| `shop_product` | Product details (linked to category) |
| `shop_cartitem` | User shopping cart |
| `shop_favourite` | User favourites/wishlist |
| `shop_order` | Order and checkout details |
| `shop_orderitem` | Items within orders |
| `shop_supportmessage` | User-submitted support messages |

---

## Technologies and Libraries
| Category | Technology |
|-----------|-------------|
| Framework | Django 5.2 |
| Database | PostgreSQL / SQLite |
| Frontend | Bootstrap 5, JavaScript |
| Environment | Python 3.10+, Virtualenv |
| Deployment | Render |
| Dependencies | Listed in `requirements.txt` |

---

##  Setup and Execution Instructions
### **1. Environment Setup**
```bash
git clone https://github.com/ArnasZv/Clothing_shop/tree/main
cd Clothing_shop
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **2. Database Configuration**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'clothing_shop_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### **3. Run Migrations and Server**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Access locally at: **http://127.0.0.1:8000**
Access Render at: **https://clothing-shop-06eh.onrender.com**

---

## Deployment Instructions (Render)
1. Push to GitHub.  
2. Connect Render and create new **Web Service**.  
3. Build Command: `pip install -r requirements.txt`  
4. Start Command: `gunicorn clothing_shop.wsgi`  
5. Add environment variables (`SECRET_KEY`, `DATABASE_URL`, `DEBUG=False`).  
6. Deploy and verify. 


---

##  Learning Outcomes
- Applied key **Django concepts** (models, templates, views).  
- Integrated **PostgreSQL database** via Django ORM.  
- Implemented secure **authentication and authorization**.  
- Developed a **responsive Bootstrap interface**.  
- Deployed a live Django app on **Render**.

---

##  Student Information
**Student Name:** [Arnas Zvirblis]  
**Course:** Frameworks Module  
**College:** [UCD Academy]  
**Submission Date:** 8 October 2025  

---

##  Conclusion
This project illustrates comprehensive understanding and practical application of the **Django framework** and modern web technologies. I believe this meets the Frameworks Assessment’s highest-level criteria by implementing robust backend logic, a relational database schema, a secure authentication system, and an interactive frontend, all within a modular, deployable architecture.

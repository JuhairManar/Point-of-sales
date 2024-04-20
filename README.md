# Point-of-sales

![image](https://github.com/JuhairManar/Point-of-sales/assets/89413439/ada13d39-dd1c-4c5e-bb85-7c3926ede7bf)
![image](https://github.com/JuhairManar/Point-of-sales/assets/89413439/5a0357e3-62b0-48a3-827d-a961a73eb84a)




This is a simple web-based inventory management system developed using Django, a high-level Python web framework. It allows users to add, update, delete, and view inventory items, as well as sell items and keep records of sales.

Features
Add Inventory: Users can add new items to the inventory, specifying details such as name, cost per item, quantity in stock, and quantity sold.
View Inventory List: Users can view a list of all inventory items, including details like name, quantity in stock, quantity sold, cost per item, sales revenue, stock date, and last sales date.
View Individual Product Details: Users can click on individual inventory items to view more detailed information about each product.
Update Inventory: Users can update the details of existing inventory items, including name, quantity in stock, quantity sold, and cost per item.
Delete Inventory: Users can delete existing inventory items from the system.
Sell Item: Users can sell items from the inventory, specifying the item and the quantity sold. The system automatically updates the quantity in stock, quantity sold, and sales revenue.
Installation

Clone the repository to your local machine:
git clone https://github.com/your_username/inventory-management.git

Navigate to the project directory:
cd inventory-management

Install dependencies:
pip install -r requirements.txt

Run migrations to create the database schema:
python manage.py migrate

Create a superuser account to access the admin interface:
python manage.py createsuperuser

Start the development server:
python manage.py runserver

Open your web browser and navigate to http://127.0.0.1:8000 to access the application.

Usage
Log in with your superuser credentials to access the admin interface or register a new account.
Add new inventory items by clicking on the "Add Inventory" link in the navigation bar.
View, update, or delete existing inventory items by navigating to the "Inventory List" page.
Click on individual inventory items to view more details and perform updates or deletions.
Sell items by navigating to the "Sell Item" page, selecting the item from the dropdown list, and specifying the quantity sold.
View sales records and details by accessing the admin interface or querying the database directly.

# Web-Applications
Django web applications.

## Recipe Sharing Web Application

> Objective

This is a Django-based web application designed to allow users to share, discover, and manage recipes. The platform provides a user-friendly interface for browsing recipes, adding new ones, and managing personal collections.

> Features

1. Recipe Management

- Add Recipes: Users can create and share their recipes by providing details such as the recipe name, ingredients, preparation steps, cooking time, and image uploads.

- Edit/Delete Recipes: Users can modify or delete their own recipes.

2. Recipe Browsing

- Recipe Search: A search functionality to filter recipes by keywords.

3. User Authentication

- Registration and Login: Secure user authentication system with the ability to register, log in, and log out.

- Personalized Experience: Users can manage only their own recipes.

> Database Models

- Recipe Model: Stores details like name, description, image and user association.

- User Model: Built on Django’s default User model for authentication.

> How to Use the Application

1. Clone the repository:
git clone <repository-link>
2. Navigate to the project directory:
cd recipe_web_app
3. Install dependencies:
pip install -r requirements.txt
4. Run the server:
python manage.py runserver
5. Open your browser and navigate to:
http://127.0.0.1:8000

> REST API Endpoints

- Endpoint: /api/recipes/
- Method: GET
- Response: Returns a list of recipes in JSON format.

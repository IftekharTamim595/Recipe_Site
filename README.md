# Recipe App

This is my first Django project, focused on learning the basics of Django, templates, and CRUD operations. The app allows users to manage recipes by creating, reading, updating, and deleting them.

---

## Features Implemented

- **Add Recipe:** Users can add a recipe with a name, description, and image.
- **View Recipes:** List all recipes and search by recipe name.
- **Update Recipe:** Edit existing recipes, including changing the image.
- **Delete Recipe:** Remove recipes from the database.
- **Basic Templates:** Used Django templates to render forms and lists.
- **Media Upload:** Handled image uploads for recipes.

---

## What I Learned

- Setting up Django project and apps.
- Creating models and using SQLite database.
- Handling forms and file uploads.
- Using Django template inheritance and blocks.
- URL routing and connecting views.
- Basic Bootstrap for UI.

---

## Project Structure

# Recipe App 🍳

A simple and functional Django web application for managing personal recipes. This project demonstrates basic CRUD (Create, Read, Update, Delete) operations, image handling, and search functionality using the Django framework.

## 📂 Project Structure

todo/
├── vege/                  # Application Directory (The 'vege' app)
│   ├── templates/         # HTML templates
│   │   ├── add_recipe.html
│   │   ├── recipe_list.html
│   │   └── index.html
│   └── views.py           # Application logic and request handlers
├── todo/                  # Project Configuration
│   ├── settings.py
│   └── urls.py            # Project-level URL routing
├── media/                 # Directory for uploaded recipe images
├── db.sqlite3             # SQLite Database file
└── manage.py              # Django command-line utility

🛠️ Installation & Setup

Follow these steps to run the project locally.

1. Clone the repository

git clone <your-repo-url>
cd Recipe_Site


2. Create and activate a virtual environment
For macOS/Linux:

python3 -m venv myvenv
source myvenv/bin/activate


For Windows:

python -m venv myvenv
myvenv\Scripts\activate


3. Install Dependencies

pip install django pillow


4. Apply Migrations
Initialize the database structure:

python manage.py migrate


5. Run the Development Server
Start the application:

python manage.py runserver


6. Access the App
Open your web browser and navigate to:
http://127.0.0.1:8000

📝 Notes

Learning Focus: This project emphasizes functionality over complex styling, making it a great learning resource.

Media: Uploaded recipe images are stored in the media/ directory.

# Recipe App

This is my first Django project, focused on learning the basics of Django, templates, and CRUD operations. The app allows users to manage recipes by creating, reading, updating, deleting & Searching them.

---

## Features Implemented

- **Add Recipe:** Users can add a recipe with a name, description, and image.
- **View Recipes:** List all recipes and search by recipe name.
- **Update Recipe:** Edit existing recipes, including changing the image.
- **Delete Recipe:** Remove recipes from the database.
- **Search REcipe:** Search Recipe from the database.
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

## 📂 Project Structure

```
todo/
├── vege/
│   ├── templates/
│   │   ├── add_recipe.html
│   │   ├── recipe_list.html
│   │   └── index.html
│   └── views.py
├── todo/
│   ├── settings.py
│   └── urls.py
├── media/
├── db.sqlite3
└── manage.py
```

## 🛠️ Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd Recipe_Site
```

### 2. Create and activate a virtual environment

**For macOS / Linux:**
```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

**For Windows:**
```bat
python -m venv myvenv
myvenv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install django pillow
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Run the development server
```bash
python manage.py runserver
```

### 6. Access the app
Open your browser and visit:
```
http://127.0.0.1:8000
```

---

## 📝 Notes

- **Learning Focus:** This project prioritizes functionality over heavy styling.
- **Media Storage:** Uploaded recipe images are stored in the `media/` directory.


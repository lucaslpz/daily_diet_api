# 🥗 daily_diet_api

Daily Diet API is a RESTful web service built with Flask to manage daily meal tracking, including CRUD operations and dietary status.  
Developed for Rocketseat's Challenge 02.

---

## 🚀 Technologies

- Python 3
- Flask
- Flask SQLAlchemy
- SQLite
- Postman (for testing)

---

## ⚙️ Features

- Create, read, update and delete meals
- Track meals by user
- Filter meals by user ID
- Associate meals with dietary status (`is_on_diet`)
- Timestamp for each meal (`date_time`)

---

## 📦 Setup Instructions

### 1. Clone the repository

git clone https://github.com/lucaslpz/daily_diet_api.git  
cd daily_diet_api

### 2. Create and activate a virtual environment

python -m venv venv  
.\venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the application

$env:FLASK_APP=app  
flask run

Access the API at: http://localhost:5000

---

## 🧪 Example Endpoints (via Postman)

### Create a meal (POST)

POST /meals

{
  "name": "Almoço saudável",
  "description": "Arroz integral, feijão, frango grelhado e salada",
  "date_time": "2025-07-10 12:30",
  "is_on_diet": true,
  "user_id": 1
}

### List all meals from a user

GET /meals/user/1

### Get a specific meal from a user

GET /meals/user/1/2  
(Retorna a refeição de ID `2` do usuário `1`)

### Update a meal

PUT /meals/2

### Delete a meal

DELETE /meals/2

---

## 📁 Project Structure

## 📁 Project Structure

```bash
daily_diet_api/
├── app/
│   ├── __init__.py          # Flask app setup  
│   ├── routes.py            # Routes (endpoints)  
│   ├── models.py            # Database models  
│   └── database.py          # DB configuration  
├── instance/
│   └── database.db          # SQLite database  
├── venv/                    # Virtual environment (not uploaded)  
├── config.py                # App configuration  
├── run.py                   # App entry point (if used)  
├── .env                     # Environment variables  
├── .gitignore               # Ignored files  
├── README.md                # Project documentation  
└── requirements.txt         # Dependencies

---

## 🧑‍💻 Author

Developed by **Lucas Felipe de Souza Pinheiro**  
GitHub: [@lucaslpz](https://github.com/lucaslpz)
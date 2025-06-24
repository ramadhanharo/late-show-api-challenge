#  Late Show API

A RESTful API built with Flask + PostgreSQL to manage guest appearances on a late-night talk show.

---

##  Features

- Built using Flask and SQLAlchemy
- PostgreSQL as the database (no SQLite)
- JWT Authentication
- MVC architecture
- Protected routes (POST/DELETE)
- Fully tested with Postman
- Auto-migrating DB schema
- Ready-to-clone GitHub repo

---

## Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge
2. Install Dependencies
bash
Copy
Edit
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
3. PostgreSQL Setup
Create the database:

sql
Copy
Edit
CREATE DATABASE late_show_db;
4. Environment Variables
In server/config.py:

python
Copy
Edit
SQLALCHEMY_DATABASE_URI = 'postgresql://<user>:<password>@localhost:5432/late_show_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = 'your-secret-key'
🚀 How to Run
bash
Copy
Edit
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python server/seed.py
flask run
Server will run at: http://127.0.0.1:5000

### Authentication Flow
🔸 Register a User
bash
Copy
Edit
POST /register
Content-Type: application/json
json

{
  "username": "admin",
  "password": "secret"
}
🔸 Login
pgsql
Copy
Edit
POST /login
Content-Type: application/json
json
Copy
Edit
{
  "username": "admin",
  "password": "secret"
}
Response:

json
Copy
Edit
{
  "access_token": "<your-token>"
}
Use this token for protected routes:

makefile
Copy
Edit
Authorization: Bearer <your-token>
 Routes & Sample Requests
 No Auth Required
Method	Route	Description
GET	/episodes	List all episodes
GET	/episodes/<id>	Get episode with appearances
GET	/guests	List all guests
GET	/guests/<id>	Guest info + their appearance ratings
POST	/register	Register user
POST	/login	Login and get JWT token

🔒 Auth Required (JWT)
Method	Route	Description
POST	/appearances	Create new appearance
DELETE	/episodes/<id>	Delete episode (cascade appearances)
DELETE	/appearances/<id>	Delete appearance

🧪 Postman Testing Guide
1. Import Postman Collection
Open Postman

Click Import

Choose challenge-4-lateshow.postman_collection.json from this repo

2. Test Routes in Order
POST /register

POST /login → Copy token

In protected requests, set:

Type: Bearer Token

Token: your copied token

✅ Sample JSON Payloads
POST /appearances
json
Copy
Edit
{
  "guest_id": 1,
  "episode_id": 2,
  "rating": 4
}
DELETE /appearances/3
Set JWT token, then call:

bash
Copy
Edit
DELETE /appearances/3
🧬 Models Summary
User
id, username, password_hash

Guest
id, name, occupation

Episode
id, date, number

Cascade deletes appearances

Appearance
id, rating, guest_id, episode_id

Validated rating (1–5)

### Repo Structure
pgsql
Copy
Edit
server/
├── app.py
├── config.py
├── seed.py
├── models/
│   ├── user.py
│   ├── guest.py
│   ├── episode.py
│   └── appearance.py
├── controllers/
│   ├── auth_controller.py
│   ├── guest_controller.py
│   ├── episode_controller.py
│   └── appearance_controller.py
migrations/
# 🚀 Content Monitoring System

## 📌 Overview

The **Content Monitoring System** is a backend application built using Django and Django REST Framework. It scans content against predefined keywords, assigns relevance scores, and flags matching content for review.

It also includes a **suppression mechanism** to prevent re-flagging already reviewed content unless it has been updated.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **API Framework:** Django REST Framework
* **Database:** SQLite
* **Version Control:** Git & GitHub

---

## ⚙️ Features

* Add and manage keywords
* Store and manage content items
* Scan content against keywords
* Generate flags with score-based logic
* Update flag status (pending, relevant, irrelevant)
* Suppression logic to avoid duplicate flagging
* RESTful API endpoints for all operations

---

## 🧠 Scoring Logic

| Condition                      | Score |
| ------------------------------ | ----- |
| Exact keyword match in title   | 100   |
| Partial keyword match in title | 70    |
| Keyword match in body          | 40    |
| No match                       | 0     |

---

## 🚫 Suppression Logic

If a flag is marked as **irrelevant**, it will not be recreated unless:

* The content is updated after the last review

---

## 🔗 API Endpoints

### 1️⃣ Add Keyword

**POST** `/api/keywords/`

```json
{
  "name": "example"
}
```

---

### 2️⃣ Run Scan

**POST** `/api/scan/`

---

### 3️⃣ Get All Flags

**GET** `/api/flags/`

---

### 4️⃣ Update Flag Status

**PATCH** `/api/flags/<id>/`

```json
{
  "status": "relevant"
}
```

---

## ▶️ How to Run Locally

```bash
# Clone repository
git clone https://github.com/DHEEKSHASOKALLA7/content-monitoring-system.git

# Navigate to project
cd content-monitoring-system

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Go into Django project
cd content_monitor

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver
```

---

## 📂 Project Structure

```
content-monitoring-system/
│
├── content_monitor/      # Django project settings
├── monitor/              # Main application
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 👤 Author

**Dheeksha Sokalla**

---

## ⭐ Future Improvements

* Add authentication & user roles
* Build frontend dashboard (React)
* Add scheduling for automatic scans
* Use PostgreSQL for production
* Deploy using Docker & cloud platforms

---

## 📌 Summary

This project demonstrates:

* REST API development
* Backend system design
* Business logic implementation
* Real-world content moderation workflow

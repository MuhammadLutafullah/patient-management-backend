# 🏥 Patient Management Backend

A FastAPI-based Patient Management API that provides complete CRUD (Create, Read, Update, Delete) functionality for patient records. The application automatically calculates BMI (Body Mass Index), assigns weight categories, and supports sorting of patient data based on BMI, height, and weight.

The project follows a clean and modular architecture using FastAPI, Pydantic, and Docker, making it easy to maintain, extend, and deploy.

---

## 🚀 Features

* Create new patient records
* Retrieve all patients or a specific patient by ID
* Update existing patient information
* Delete patient records
* Automatic BMI calculation
* Dynamic weight category classification
* Sort patients by:

  * BMI
  * Height
  * Weight
* Ascending and descending sorting support
* Request and response validation using Pydantic
* Interactive API documentation with Swagger UI
* Dockerized for easy deployment

---

## 🛠️ Tech Stack

* FastAPI
* Python 3.11
* Pydantic
* Uvicorn
* Docker
* JSON Database

---

## 📁 Project Structure

```text
.
├── app
│   ├── core
│   ├── db
│   │   └── patient.json
│   ├── routes
│   │   └── patient_routes.py
│   ├── schemas
│   │   └── patient_schema.py
│   ├── services
│   │   └── patient_service.py
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### Create Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn app.main:app --reload
```

---

## 📖 API Documentation

After starting the application:

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## 🐳 Docker Usage

### Build Docker Image

```bash
docker build -t patient-api .
```

### Run Container

```bash
docker run -p 8001:8000 patient-api
```

### Pull from Docker Hub

```bash
docker pull muhammadlutafullah/patient-api
```

### Run Docker Hub Image

```bash
docker run -p 8001:8000 muhammadlutafullah/patient-api
```

---

## 📌 API Endpoints

### Get All Patients

```http
GET /
```

### Get Patient by ID

```http
GET /patient/{patient_id}
```

### Create Patient

```http
POST /create
```

### Update Patient

```http
PUT /edit/{patient_id}
```

### Delete Patient

```http
DELETE /delete/{patient_id}
```

### Sort Patients

```http
GET /sort?sort_by=bmi&order=desc
```

Supported sorting fields:

* bmi
* height
* weight

Supported sorting orders:

* asc
* desc

---

## 🧮 BMI Classification

| BMI Range    | Category    |
| ------------ | ----------- |
| Below 18.5   | Underweight |
| 18.5 - 24.9  | Normal      |
| 25 - 29.9    | Overweight  |
| 30 and Above | Obese       |

---

## 🎯 Learning Objectives

This project demonstrates:

* REST API Development with FastAPI
* Data Validation with Pydantic
* CRUD Operations
* Business Logic Implementation
* Docker Containerization
* Modular Project Architecture
* API Documentation
* Backend Development Best Practices

---

## 👨‍💻 Author

**Muhammad Lutaf Ullah**

Frontend & AI Developer with experience in React.js, FastAPI, Docker, and modern web application development.

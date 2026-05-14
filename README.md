# 🏥 SmartCare - Online Healthcare Platform
![Django](https://img.shields.io/badge/Django-4.x-green?logo=django)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-UI-blue?logo=tailwindcss)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![Stripe](https://img.shields.io/badge/Stripe-Payments-purple?logo=stripe)
![Vercel](https://img.shields.io/badge/Vercel-Deploy-black?logo=vercel)

SmartCare is an online healthcare platform built with Django that connects patients and doctors digitally. It allows users to analyze symptoms using an AI-powered symptom checker, book appointments, consult doctors via video calls, manage prescriptions, make secure payments, and maintain complete medical records — all in one place. 

🌐 Live Demo: https://smart-care-drab.vercel.app/  
🔗 GitHub Repo: https://github.com/saminmahmud/Smart-Care.git  

---

## 📸 Project Preview

<img width="700" alt="Screenshot 2026-05-10 111428" src="https://github.com/user-attachments/assets/b1072b12-c539-4444-88d7-add462784c75" alt="SmartCare" />

---

## 🚀 Key Features

### 👨‍⚕️ Doctor Features
- Doctor profile management
- Appointment management system
- Write & manage prescriptions
- View assigned patients
- Earnings dashboard
- Availability control
- Ratings & reviews system

### 🧑‍💼 Patient Features
- AI symptom checker
- Book doctor appointments
- View prescriptions
- Medical history tracking
- Upload medical reports
- Allergy & family medical history management
- Payment history tracking
- Video consultation access

### 💳 Payment System
- Stripe payment integration
- Secure transaction handling
- Payment status tracking
- Platform fee calculation system

### 📹 Video Consultation
- Real-time video calling using ZEGOCLOUD
- Appointment-based meeting rooms

### 🔐 Authentication & Authorization
- Role-based authentication (Patient / Doctor / Admin)
- Custom user model (email-based login)
- Secure session handling

### 🔍 Core System Features
- Doctor search & filtering
- Appointment slot management
- Prescription system (with medications)
- File upload system (medical reports)
- Pagination system
- Email notification system after booking
- Responsive UI (mobile-friendly)

---

## 🧠 Tech Stack

### Backend
- Django
- Django ORM
- PostgreSQL (Neon DB)
- Gemini AI API (for Symptom Analysis)
- Django Environ
- Gunicorn
- Whitenoise

### Frontend
- Django Templates (Jinja2)
- Tailwind CSS
- JavaScript

### Integrations
- Stripe Payment Gateway
- ZEGOCLOUD (Video Calling)
- Cloud storage (Media handling)

### Deployment
- Vercel (Full Deployment)
- Neon PostgreSQL Database

---

## 📁 Project Structure
```
Smart Care
├── accounts/ # Authentication & user system
├── doctors/ # Doctor management system
├── patients/ # Patient medical system
├── appointments/ # Booking & scheduling system
├── smart_care/ # Main project settings
├── templates/ # UI templates (frontend)
├── static/ # Static files
├── media/ # Uploaded files
├── requirements.txt
├── vercel.json
├── README.md
```
## ⚙️ Installation & Setup

### Clone Repository
```bash
git clone https://github.com/saminmahmud/Smart-Care.git
cd Smart-Care
```

### Setup with UV (Recommended)

1. **Install UV** (if not already installed)
   ```bash
   pip install uv
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Activate virtual environment**
   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. **Create .env file** (for environment variables)
   ```bash
   cp .env.example .env
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000/` or `http://localhost:8000/`.

---

### Setup with Pip

1. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install --upgrade pip
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run development server**
   ```bash
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000/` or `http://localhost:8000/`.

---

### 🧩 System Modules
🧑 Accounts App
* Custom User Model (Email login) & Role-based access system.

👨‍⚕️ Doctors App
* Profile, schedule, earnings, and reviews management.

🧑‍💼 Patients App
* AI Symptom Checker: Gemini-powered analysis to predict severity and recommend specialists.
* Medical history, report uploads, and allergy tracking.

📅 Appointments App
* Booking, prescriptions, ZEGOCLOUD video integration, and Stripe payments.

---

### 🔥 Highlights
* AI-Integrated Workflow: From symptom analysis to doctor recommendation.
* Production Ready: Fully deployed on Vercel with Neon PostgreSQL.
* Industry Standard: Secure payments and real-time video consultations.

# 🔐 Security Event & Alert Monitoring Backend

A scalable backend service built with **Django** and **Django REST Framework** to ingest security events from multiple sources and automatically generate, manage, and view alerts.


## 🚀 Project Overview

This project provides:

* Secure authentication with JWT authentication and role-based access control
* APIs to ingest and store security events
* Automatic alert generation for high-severity threats
* Alert lifecycle management (Open → Acknowledged → Resolved)
* Clean REST APIs with pagination, filtering, and validation

## 🧱 Tech Stack

| Layer           | Technology                   |
| --------------- | ---------------------------- |
| Backend         | Python, Django               |
| API Framework   | Django REST Framework        |
| Authentication  | JWT                          |
| Database        | SQLite                       |
| Documentation   | Swagger                      |
| Version Control | Git & GitHub                 |

---

## 👥 User Roles & Permissions

### Roles

* **Admin**
* **Analyst**

### Access Control

| Feature             | Admin | Analyst |
| ------------------- | ----- | ------- |
| View alerts         | ✅     | ✅       |
| Filter alerts       | ✅     | ✅       |
| Update alert status | ✅     | ❌       |
| Ingest events       | ✅     | ❌       |
| Manage users        | ✅     | ❌       |

---

## 📦 Core Features

### 1️⃣ Authentication & Authorization

* Secure user authentication 
* Role-based permission checks
* Token-based authentication

---

### 2️⃣ Security Event Management

#### Event Ingestion API

* Accepts security events from multiple sources
* Stores events in the database

**Event Fields**:

* `source_name` (string)
* `event_type` (intrusion / malware / anomaly / etc.)
* `severity` (Low / Medium / High / Critical)
* `description` (text)
* `timestamp` (auto-generated)

---

### 3️⃣ Alert System

Alerts are **automatically generated** when:

* Event severity is **High** or **Critical**

🔔 **Implementation Detail (Signals Used)**

This project uses **Django Signals** to decouple event creation from alert generation.

* A `post_save` signal listens for new `Event` records
* When an event is created with severity **High** or **Critical**, an `Alert` is automatically created
* This ensures:

  * Clean separation of concerns
  * No alert logic inside API views
  * Easy extensibility for future integrations (SIEM / AI detectors)

**Signal Flow:**

```
Event Created → Django post_save Signal → Alert Generated
```

**Alert Fields**:

* Reference to the triggering event
* `status` → Open / Acknowledged / Resolved
* `created_at` timestamp

---

## 🔌 API Endpoints

### 🔐 Authentication

| Method | Endpoint            | Description |
| ------ | ------------------- | ----------- |
| POST   | `/v1/auth/login/`  | Login user  |
| POST   | `/v1/auth/signup/` | signup user |

---

### 📡 Events

| Method | Endpoint                               |   Description           | Access |
| ------ | --------------                         | ---------------------   | ------ |
| POST   | `/v1/events/security_events/`          | Ingest security event    | Admin  |

---

### 🚨 Alerts

| Method | Endpoint                                       | Description         | Access          |
| ------ | ----------------------------------------       | ------------------- | --------------- |
| GET    | `/v1/alerts/alerts/`                           | List alerts         | Admin / Analyst |
| GET    | `/v1/alerts/alerts/?severity=High&status=Open` | Filter alerts       | Admin / Analyst |
| PATCH  | `/v1/alerts/alerts/{id}/`                      | Update alert status | Admin           |

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/security-alert-backend.git
cd threat_alert_management
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run Server

```bash
python manage.py runserver
```

## 📘 Assumptions Made

* Only **High** and **Critical** severity events trigger alerts
* Analysts have **read-only** access
* Events are immutable once created

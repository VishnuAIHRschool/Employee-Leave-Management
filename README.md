# 📅 Employee Leave Management Portal

## 🚀 Project Overview

Employee Leave Management Portal is a modern HR application developed using **FastAPI, Streamlit, SQLite, SQLAlchemy, and Plotly**. The portal automates the employee leave management process by providing role-based access for Employees, Managers, and Administrators.

The application enables employees to submit leave requests, managers to approve or reject requests, and administrators to monitor workforce data through interactive dashboards and analytics.

---

## 🎯 Project Objective

The primary objective of this project is to digitize and automate the employee leave management process while providing a user-friendly interface and role-based access control.

---

## 🏗 System Architecture

```text
Streamlit Frontend
        │
        ▼
FastAPI Backend
        │
        ▼
SQLite Database
```

---

## 🛠 Technology Stack

| Component          | Technology |
| ------------------ | ---------- |
| Frontend           | Streamlit  |
| Backend            | FastAPI    |
| Database           | SQLite     |
| ORM                | SQLAlchemy |
| Charts & Analytics | Plotly     |
| Language           | Python     |
| API Documentation  | Swagger UI |

---

## 🔐 Role-Based Login System

### Employee

* Login using Employee ID and Password
* Apply Leave
* View Own Leave History

### Manager

* View Employee Dashboard
* Approve / Reject Leave Requests
* View Leave Statistics
* View Leave History

### Administrator

* Full Portal Access
* Employee Dashboard
* Employee Directory
* Leave Management
* Leave Statistics
* Manager Approval Dashboard

---

## 📋 Features Implemented

### 👨‍💼 Employee Dashboard

* Total Employee Count
* Gender Distribution Analysis
* Department-wise Employee Analytics
* Designation-wise Employee Analytics
* Interactive Visualizations

### 📝 Leave Application Module

* Apply Leave
* Leave Type Selection
* Leave Duration Calculation
* Leave Validation
* Real-Time Submission

### ✅ Manager Approval Dashboard

* Pending Leave Requests
* Approve Requests
* Reject Requests
* Request Tracking

### 👥 Employee Directory

* Employee Search
* Employee Profile Cards
* Department Information
* Reporting Manager Information
* Employee Master Data

### 📊 Leave Statistics Dashboard

* Leave Status Distribution
* Leave Type Analysis
* Department-wise Leave Analytics
* Interactive Charts

### 🗄 Database Management

* Employee Records Storage
* Leave Records Storage
* Status Tracking
* Historical Data Management

---

## 📂 Project Structure

```text
EmployeeLeaveManagement
│
├── backend
│   ├── main.py
│   ├── database.py
│   └── models.py
│
├── frontend
│   └── app.py
│
├── screenshots
│
├── leave_management.db
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

## ⚙ Installation Guide

### Step 1: Clone Repository

```bash
git clone https://github.com/VishnuAIHRschool/Employee-Leave-Management.git
```

### Step 2: Navigate to Project

```bash
cd Employee-Leave-Management
```

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Run Backend

Navigate to backend folder:

```bash
cd backend
```

Run FastAPI:

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## ▶ Run Frontend

Navigate to frontend folder:

```bash
cd frontend
```

Run Streamlit:

```bash
streamlit run app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

## 📸 Application Screenshots

### Login Screen

Screenshot available in screenshots folder.

### Employee Dashboard

Screenshot available in screenshots folder.

### Apply Leave Module

Screenshot available in screenshots folder.

### Manager Approval Dashboard

Screenshot available in screenshots folder.

### Employee Directory

Screenshot available in screenshots folder.

### Leave Statistics Dashboard

Screenshot available in screenshots folder.

---

## 🔄 Workflow

### Employee

1. Login to Portal
2. Apply Leave
3. Submit Request
4. Track Request Status

### Manager

1. Login to Portal
2. Review Leave Requests
3. Approve or Reject Requests

### Administrator

1. Login to Portal
2. Monitor Employee Analytics
3. View Leave Statistics
4. Manage Employee Information

---

## 📊 Key Outcomes

* Automated Leave Management Process
* Improved Approval Efficiency
* Centralized Employee Information
* Interactive HR Analytics
* Real-Time Leave Tracking
* Role-Based Security

---

## 🎓 Buildathon Requirements Covered

✅ FastAPI Backend

✅ Streamlit Frontend

✅ SQLite Database

✅ Role-Based Login

✅ Employee Dashboard

✅ Apply Leave Module

✅ Manager Approval Dashboard

✅ Employee Directory

✅ Leave Statistics Dashboard

✅ Leave History Tracking

✅ API Integration

✅ Interactive Charts

✅ GitHub Repository

---

## 🔗 GitHub Repository

https://github.com/VishnuAIHRschool/Employee-Leave-Management

---

## 👨‍💻 Author

**Vishnukumar**

Buildathon Project Submission

---

## 📌 Conclusion

The Employee Leave Management Portal successfully demonstrates the implementation of a complete HR leave management solution using modern Python technologies. The system automates leave processing, approval workflows, employee analytics, and reporting through an intuitive web-based interface.

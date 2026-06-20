# 📅 Employee Leave Management Portal

## 🚀 Project Overview

The Employee Leave Management Portal is a modern HR application built using FastAPI, Streamlit, and SQLite. The system enables employees to apply for leave, managers to approve or reject requests, and HR teams to monitor workforce leave analytics through interactive dashboards.

This project was developed as a Buildathon submission to demonstrate full-stack application development using Python technologies.

---

## 🎯 Key Features

### 👨‍💼 Employee Dashboard

- Total Employee Count
- Gender Distribution Analysis
- Department-wise Employee Analysis
- Designation-wise Employee Analysis
- Interactive Employee Analytics

### 📝 Leave Management

- Submit Leave Requests
- Automatic Leave Day Calculation
- Leave Validation
- Employee Selection from Directory
- Multiple Leave Types Support

### ✅ Manager Approval Dashboard

- View Pending Requests
- Approve Leave Requests
- Reject Leave Requests
- Real-Time Status Updates

### 👥 Employee Directory

- Employee Search
- Employee Cards View
- Employee Master Data
- Department Information
- Reporting Manager Information

### 📊 Leave Statistics Dashboard

- Leave Status Distribution
- Leave Type Analysis
- Department-wise Leave Analysis
- Interactive Charts & Visualizations

### 🗄 Database Management

- SQLite Database Integration
- Employee Records Storage
- Leave Request Storage
- Status Tracking

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

| Component | Technology |
|------------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Visualization | Plotly |
| Language | Python |
| API Testing | Swagger UI |

---

## 📁 Project Structure

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

### Step 1 - Clone Repository

```bash
git clone https://github.com/VishnuAIHRschool/Employee-Leave-Management.git
```

### Step 2 - Navigate to Project

```bash
cd Employee-Leave-Management
```

### Step 3 - Create Virtual Environment

```bash
python -m venv venv
```

### Step 4 - Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Step 5 - Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Backend

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

## ▶ Running the Frontend

Navigate to frontend folder:

```bash
cd frontend
```

Run Streamlit:

```bash
streamlit run app.py
```

Application URL:

```text
http://localhost:8501
```

---

## 📷 Application Screenshots

### Employee Dashboard

(Add Screenshot Here)

### Apply Leave

(Add Screenshot Here)

### Manager Approval Dashboard

(Add Screenshot Here)

### Employee Directory

(Add Screenshot Here)

### Leave Statistics Dashboard

(Add Screenshot Here)

---

## 🔄 Workflow

### Employee

1. Select Employee
2. Apply Leave
3. Submit Request

### Manager

1. Review Request
2. Approve / Reject Request

### System

1. Store Request in Database
2. Update Status
3. Display Analytics

---

## 📈 Future Enhancements

- Authentication & Login
- Role-Based Access Control
- Email Notifications
- Leave Balance Tracking
- Attendance Management
- Payroll Integration
- Work From Home Module
- Cloud Deployment

---

## 🎓 Buildathon Requirements Covered

✅ FastAPI Backend

✅ Streamlit Frontend

✅ SQLite Database

✅ Employee Dashboard

✅ Apply Leave Module

✅ Manager Approval Dashboard

✅ Employee Directory

✅ Leave Statistics Dashboard

✅ Leave History

✅ Employee Master Data

✅ Interactive Charts

✅ Responsive UI

---

## 👨‍💻 Author

**Vishnukumar**

Buildathon Project Submission

GitHub Repository:

https://github.com/VishnuAIHRschool/Employee-Leave-Management

---

## 📌 Conclusion

The Employee Leave Management Portal streamlines employee leave processing, manager approvals, and workforce analytics through an intuitive web-based interface built using modern Python technologies.

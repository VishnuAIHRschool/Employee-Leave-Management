from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import Employee, LeaveRequest
import random
from datetime import date, timedelta

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Leave Management API",
    description="Backend API for Employee Leave Management System",
    version="1.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Employee Leave Management API is running successfully"}


@app.post("/employees/")
def add_employee(
    employee_id: str,
    name: str,
    department: str,
    designation: str,
    email: str,
    manager: str,
    db: Session = Depends(get_db)
):
    existing = db.query(Employee).filter(
        (Employee.employee_id == employee_id) | (Employee.email == email)
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Employee already exists")

    employee = Employee(
        employee_id=employee_id,
        name=name,
        department=department,
        designation=designation,
        email=email,
        manager=manager
    )

    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


@app.get("/employees/")
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()


@app.post("/apply-leave/")
def apply_leave(
    employee_id: str,
    employee_name: str,
    leave_type: str,
    start_date: str,
    end_date: str,
    total_days: int,
    reason: str,
    db: Session = Depends(get_db)
):
    leave = LeaveRequest(
        employee_id=employee_id,
        employee_name=employee_name,
        leave_type=leave_type,
        start_date=start_date,
        end_date=end_date,
        total_days=total_days,
        reason=reason,
        status="Pending"
    )

    db.add(leave)
    db.commit()
    db.refresh(leave)
    return leave


@app.get("/leave-history/")
def leave_history(db: Session = Depends(get_db)):
    return db.query(LeaveRequest).all()


@app.put("/leave/{leave_id}/approve")
def approve_leave(leave_id: int, db: Session = Depends(get_db)):
    leave = db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()

    if not leave:
        raise HTTPException(status_code=404, detail="Leave request not found")

    leave.status = "Approved"
    db.commit()
    db.refresh(leave)
    return leave


@app.put("/leave/{leave_id}/reject")
def reject_leave(leave_id: int, db: Session = Depends(get_db)):
    leave = db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()

    if not leave:
        raise HTTPException(status_code=404, detail="Leave request not found")

    leave.status = "Rejected"
    db.commit()
    db.refresh(leave)
    return leave


@app.post("/seed-data/")
def seed_data(db: Session = Depends(get_db)):
    existing_count = db.query(Employee).count()

    if existing_count >= 50:
        return {
            "message": "Demo data already available",
            "employees": existing_count
        }

    departments = ["HR", "IT", "Finance", "Sales", "Operations", "Admin"]
    designations = [
        "Executive",
        "Senior Executive",
        "Manager",
        "Assistant Manager",
        "Analyst",
        "Team Lead"
    ]
    managers = [
        "Anitha Raj",
        "Ramesh Kumar",
        "Priya Menon",
        "Karthik S",
        "Meera Nair"
    ]
    leave_types = [
    "Casual Leave",
    "Sick Leave",
    "Earned Leave",
    "Emergency Leave"
]
    
    statuses = ["Approved", "Pending", "Rejected"]

    first_names = [
        "Arjun", "Priya", "Karthik", "Meera", "Rahul", "Divya", "Suresh", "Ananya", "Vijay", "Sneha",
        "Naveen", "Lakshmi", "Manoj", "Aishwarya", "Prakash", "Keerthana", "Balaji", "Swetha", "Gokul", "Nithya",
        "Ravi", "Harini", "Sanjay", "Pooja", "Vikram", "Gayathri", "Madhan", "Janani", "Ashwin", "Deepika",
        "Bharath", "Ramya", "Dinesh", "Sowmya", "Ajay", "Monika", "Saravanan", "Kavya", "Vignesh", "Shruthi",
        "Mohan", "Sindhu", "Ranjith", "Abinaya", "Praveen", "Latha", "Hari", "Rekha", "Sathish", "Indhu"
    ]

    for i, name in enumerate(first_names, start=1):
        emp_id = f"EMP{i:03d}"
        employee = Employee(
            employee_id=emp_id,
            name=f"{name} Kumar" if i % 2 == 0 else f"{name} Raj",
            department=random.choice(departments),
            designation=random.choice(designations),
            email=f"{name.lower()}{i}@company.com",
            manager=random.choice(managers)
        )
        db.add(employee)

    db.commit()

    employees = db.query(Employee).all()

    for emp in employees[:35]:
        start = date.today() + timedelta(days=random.randint(-20, 30))
        days = random.randint(1, 5)
        end = start + timedelta(days=days - 1)

        leave = LeaveRequest(
            employee_id=emp.employee_id,
            employee_name=emp.name,
            leave_type=random.choice(leave_types),
            start_date=str(start),
            end_date=str(end),
            total_days=days,
            reason=random.choice([
                "Personal work",
                "Medical appointment",
                "Family function",
                "Travel plan",
                "Health issue",
                "Work from home request"
            ]),
            status=random.choice(statuses)
        )
        db.add(leave)

    db.commit()

    return {
        "message": "Demo data created successfully",
        "employees_created": 50,
        "leave_requests_created": 35
    }
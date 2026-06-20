from sqlalchemy import Column, Integer, String
from database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True)
    name = Column(String)
    department = Column(String)
    designation = Column(String)
    email = Column(String, unique=True)
    manager = Column(String)


class LeaveRequest(Base):
    __tablename__ = "leave_requests"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String)
    employee_name = Column(String)
    leave_type = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    total_days = Column(Integer)
    reason = Column(String)
    status = Column(String, default="Pending")
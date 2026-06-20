import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import date

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Leave Management Portal", page_icon="📅", layout="wide")

st.markdown("""
<style>
.stApp { background:#f5f7fb; }
.block-container { padding: 1.4rem 2rem 2rem 2rem; }

[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#071426,#10213d);
    padding-top: 25px;
}
[data-testid="stSidebar"] * { color:white !important; }

.sidebar-title { font-size:26px; font-weight:900; line-height:1.35; margin-bottom:8px; }
.sidebar-subtitle { font-size:13px; color:#cbd5e1 !important; margin-bottom:26px; }

.topbar, .card, .metric-card, .approval-card {
    background:white;
    border:1px solid #e5e7eb;
    box-shadow:0 8px 24px rgba(15,23,42,.07);
}
.topbar { padding:20px 26px; border-radius:18px; margin-bottom:22px; }
.page-title { font-size:30px; font-weight:900; color:#0f172a; }
.page-subtitle { color:#64748b; font-size:14px; font-weight:600; }

.metric-card { padding:22px; border-radius:20px; min-height:125px; }
.metric-title { color:#64748b; font-size:14px; font-weight:800; }
.metric-value { color:#0f172a; font-size:34px; font-weight:900; }
.metric-note { color:#64748b; font-size:13px; font-weight:600; }

.card { padding:24px; border-radius:22px; margin-bottom:22px; }
.card-title { color:#0f172a; font-size:21px; font-weight:900; margin-bottom:18px; }


.approval-card {
    padding:24px;
    border-radius:20px;
    border-left:7px solid #2563eb;
    margin-bottom:18px;
}
.approval-title { color:#0f172a; font-size:22px; font-weight:900; margin-bottom:16px; }
.info-row { color:#0f172a; font-size:15px; margin-bottom:10px; }
.info-label { color:#475569; font-weight:900; display:inline-block; min-width:160px; }

.badge-pending { background:#fef3c7; color:#92400e; padding:7px 14px; border-radius:20px; font-weight:900; }
.badge-approved { background:#dcfce7; color:#166534; padding:7px 14px; border-radius:20px; font-weight:900; }
.badge-rejected { background:#fee2e2; color:#991b1b; padding:7px 14px; border-radius:20px; font-weight:900; }

.employee-card {
    background:white;
    border:1px solid #e5e7eb;
    border-radius:18px;
    padding:18px;
    box-shadow:0 8px 22px rgba(15,23,42,.06);
    min-height:205px;
}
.employee-avatar {
    width:45px;
    height:45px;
    border-radius:50%;
    background:#eef2ff;
    color:#3730a3;
    display:flex;
    align-items:center;
    justify-content:center;
    font-weight:900;
    margin-bottom:12px;
}
.employee-name { color:#0f172a; font-size:18px; font-weight:900; }
.employee-meta { color:#64748b; font-size:13px; margin-bottom:7px; font-weight:600; }
.employee-tag {
    display:inline-block;
    background:#eef2ff;
    color:#3730a3;
    padding:5px 10px;
    border-radius:16px;
    font-size:12px;
    font-weight:900;
}

label { color:#0f172a !important; font-weight:800 !important; }
.stButton > button {
    background:linear-gradient(135deg,#2563eb,#7c3aed);
    color:white;
    border:none;
    border-radius:12px;
    font-weight:900;
    padding:.6rem 1.2rem;
}
.stButton > button:hover { color:white; border:none; }
</style>
""", unsafe_allow_html=True)


# -------------------- API FUNCTIONS --------------------

def get_leave_data():
    try:
        r = requests.get(f"{API_URL}/leave-history/")
        return r.json() if r.status_code == 200 else []
    except:
        st.error("Backend not running. Start FastAPI first.")
        return []


def get_employee_data():
    try:
        r = requests.get(f"{API_URL}/employees/")
        return r.json() if r.status_code == 200 else []
    except:
        return []


def add_gender_if_missing(df):
    if df.empty:
        return df

    if "gender" not in df.columns:
        female_names = [
            "Priya", "Meera", "Divya", "Ananya", "Sneha", "Lakshmi", "Aishwarya",
            "Keerthana", "Swetha", "Nithya", "Harini", "Pooja", "Gayathri",
            "Janani", "Deepika", "Ramya", "Sowmya", "Monika", "Kavya",
            "Shruthi", "Sindhu", "Abinaya", "Latha", "Rekha", "Indhu"
        ]

        def find_gender(name):
            first_name = str(name).split()[0]
            return "Female" if first_name in female_names else "Male"

        df["gender"] = df["name"].apply(find_gender)

    return df


def status_badge(status):
    status = str(status).strip()
    if status == "Approved":
        return '<span class="badge-approved">Approved</span>'
    if status == "Rejected":
        return '<span class="badge-rejected">Rejected</span>'
    return '<span class="badge-pending">Pending</span>'


def clean_plot(fig, height=430):
    fig.update_layout(
        template="plotly_white",
        height=height,
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#0f172a", size=15),
        title_font=dict(color="#0f172a", size=21, family="Arial Black"),
        margin=dict(l=80, r=80, t=80, b=110),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.32,
            xanchor="center",
            x=0.5,
            font=dict(color="#0f172a", size=14),
            bgcolor="rgba(255,255,255,0)"
        ),
        uniformtext_minsize=12,
        uniformtext_mode="show",
        autosize=True
    )

    fig.update_xaxes(
        automargin=True,
        title_standoff=25,
        title_font=dict(color="#0f172a", size=16, family="Arial Black"),
        tickfont=dict(color="#0f172a", size=14),
        showgrid=False,
        linecolor="#334155",
        linewidth=2
    )

    fig.update_yaxes(
        automargin=True,
        title_standoff=25,
        title_font=dict(color="#0f172a", size=16, family="Arial Black"),
        tickfont=dict(color="#0f172a", size=14),
        showgrid=True,
        gridcolor="#dbe3ef",
        linecolor="#334155",
        linewidth=2
    )

    return fig


def clean_pie(fig, height=430):
    fig.update_traces(
        textposition="outside",
        textinfo="label+percent+value",
        marker=dict(line=dict(color="white", width=2))
    )

    fig.update_layout(
        template="plotly_white",
        height=height,
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#0f172a", size=15),
        title_font=dict(color="#0f172a", size=21, family="Arial Black"),
        margin=dict(l=90, r=90, t=80, b=95),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.22,
            xanchor="center",
            x=0.5,
            font=dict(color="#0f172a", size=14),
            bgcolor="rgba(255,255,255,0)"
        ),
        uniformtext_minsize=12,
        uniformtext_mode="show",
        autosize=True
    )
    return fig


# -------------------- LOGIN SYSTEM --------------------

USERS = {
    "EMP001": {"password": "emp123", "role": "Employee", "name": "Employee User"},
    "MGR001": {"password": "manager123", "role": "Manager", "name": "Manager User"},
    "ADMIN001": {"password": "admin123", "role": "Admin", "name": "Admin User"},
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_id = ""
    st.session_state.role = ""
    st.session_state.name = ""

if not st.session_state.logged_in:

    left, center, right = st.columns([2, 1.2, 2])

    with center:

        st.markdown("""
        <div style="
            background:white;
            padding:35px;
            border-radius:20px;
            box-shadow:0 10px 30px rgba(0,0,0,0.08);
            margin-top:80px;
        ">
        <h1 style="text-align:center;color:#0f172a;">
            Leave Management Portal
        </h1>

        <p style="
            text-align:center;
            color:#64748b;
            margin-bottom:30px;
        ">
            Employee • Manager • Administrator Access
        </p>
        </div>
        """, unsafe_allow_html=True)

        login_id = st.text_input(
            "Employee ID",
            placeholder="Enter Employee ID"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter Password"
        )

        login_btn = st.button(
            "Login",
            use_container_width=True
        )

        if login_btn:
            if login_id in USERS and USERS[login_id]["password"] == password:
                st.session_state.logged_in = True
                st.session_state.user_id = login_id
                st.session_state.role = USERS[login_id]["role"]
                st.session_state.name = USERS[login_id]["name"]
                st.rerun()
            else:
                st.error("Invalid Employee ID or Password")

    st.stop()  
    st.markdown("<h1 style='text-align:center;color:#0f172a;'>📅 Leave Management Portal</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center;color:#64748b;'>Role-Based Login</h4>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.1, 1])

    with col2:
        

        login_id = st.text_input("Employee / Manager / Admin ID")
        password = st.text_input("Password", type="password")

      

        login_btn = st.button("Login")

        if login_btn:
            if login_id in USERS and USERS[login_id]["password"] == password:
                st.session_state.logged_in = True
                st.session_state.user_id = login_id
                st.session_state.role = USERS[login_id]["role"]
                st.session_state.name = USERS[login_id]["name"]
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid ID or password")

      

    st.stop()


# -------------------- DATA LOAD --------------------

leave_df_all = pd.DataFrame(get_leave_data())

if not leave_df_all.empty and "leave_type" in leave_df_all.columns:
    wfh_df = leave_df_all[
        leave_df_all["leave_type"].astype(str).str.lower().str.contains("work from home|wfh", na=False)
    ]

    leave_df = leave_df_all[
        ~leave_df_all["leave_type"].astype(str).str.lower().str.contains("work from home|wfh", na=False)
    ]
else:
    leave_df = leave_df_all
    wfh_df = pd.DataFrame()

employee_df = pd.DataFrame(get_employee_data())
employee_df = add_gender_if_missing(employee_df)


# -------------------- SIDEBAR --------------------

st.sidebar.markdown('<div class="sidebar-title">📅 Leave Management Portal</div>', unsafe_allow_html=True)
st.sidebar.markdown(
    f'<div class="sidebar-subtitle">Logged in as: {st.session_state.role}</div>',
    unsafe_allow_html=True
)

if st.session_state.role == "Employee":
    menu_options = [
        "📝 Apply Leave",
        "📄 Leave History"
    ]

elif st.session_state.role == "Manager":
    menu_options = [
        "🏠 Employee Dashboard",
        "✅ Manager Approval Dashboard",
        "📊 Leave Statistics",
        "📄 Leave History"
    ]

else:
    menu_options = [
        "🏠 Employee Dashboard",
        "📝 Apply Leave",
        "✅ Manager Approval Dashboard",
        "👥 Employee Directory",
        "📊 Leave Statistics",
        "📄 Leave History"
    ]

menu = st.sidebar.radio("MAIN MENU", menu_options)

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.user_id = ""
    st.session_state.role = ""
    st.session_state.name = ""
    st.rerun()


page_title = menu.split(" ", 1)[1]

st.markdown(f"""
<div class="topbar">
    <div class="page-title">{page_title}</div>
    <div class="page-subtitle">Welcome, {st.session_state.name} | Role: {st.session_state.role}</div>
</div>
""", unsafe_allow_html=True)


# -------------------- EMPLOYEE DASHBOARD --------------------

if menu == "🏠 Employee Dashboard":
    total_employees = len(employee_df)
    total_departments = employee_df["department"].nunique() if not employee_df.empty else 0
    total_designations = employee_df["designation"].nunique() if not employee_df.empty else 0
    male_count = len(employee_df[employee_df["gender"] == "Male"]) if not employee_df.empty else 0
    female_count = len(employee_df[employee_df["gender"] == "Female"]) if not employee_df.empty else 0

    cols = st.columns(5)
    data = [
        ("Total Employees", total_employees, "Active employee records"),
        ("Departments", total_departments, "Business units"),
        ("Designations", total_designations, "Role categories"),
        ("Male Employees", male_count, "Gender split"),
        ("Female Employees", female_count, "Gender split")
    ]

    for col, (title, value, note) in zip(cols, data):
        col.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    if not employee_df.empty:
        c1, c2 = st.columns(2)

        with c1:
            st.markdown('<div class="card"><div class="card-title">Gender Distribution</div>', unsafe_allow_html=True)
            gender_count = employee_df.groupby("gender").size().reset_index(name="employees")
            fig = px.pie(gender_count, names="gender", values="employees", hole=0.45, title="Employee Gender Split")
            st.plotly_chart(clean_pie(fig), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with c2:
            st.markdown('<div class="card"><div class="card-title">Department-wise Employees</div>', unsafe_allow_html=True)
            dept_count = employee_df.groupby("department").size().reset_index(name="employees")
            fig = px.bar(
                dept_count,
                x="department",
                y="employees",
                text="employees",
                title="Employees by Department",
                labels={"department": "Department", "employees": "Number of Employees"}
            )
            fig.update_traces(textposition="outside", cliponaxis=False)
            st.plotly_chart(clean_plot(fig), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card"><div class="card-title">Designation-wise Employees</div>', unsafe_allow_html=True)
        designation_count = employee_df.groupby("designation").size().reset_index(name="employees")
        fig = px.bar(
            designation_count,
            x="designation",
            y="employees",
            text="employees",
            title="Employees by Designation",
            labels={"designation": "Designation", "employees": "Number of Employees"}
        )
        fig.update_traces(textposition="outside", cliponaxis=False)
        fig.update_xaxes(tickangle=-25)
        st.plotly_chart(clean_plot(fig, 460), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.info("No employee data available.")


# -------------------- APPLY LEAVE --------------------

elif menu == "📝 Apply Leave":
    st.markdown('<div class="card"><div class="card-title">Submit Leave Application</div>', unsafe_allow_html=True)

    if employee_df.empty:
        st.warning("No employees found. Load demo data from FastAPI docs first.")
    else:
        employee_df["display_name"] = employee_df["employee_id"] + " - " + employee_df["name"]

        with st.form("leave_form"):
            if st.session_state.role == "Employee":
                own_employee = employee_df[employee_df["employee_id"] == st.session_state.user_id]

                if not own_employee.empty:
                    selected_row = own_employee.iloc[0]
                    st.info("Employee login detected. Leave will be applied only for your employee ID.")
                else:
                    selected_row = employee_df.iloc[0]
                    st.warning("Demo employee ID not found in employee table. Using first employee record.")
            else:
                selected_employee = st.selectbox("Select Employee *", employee_df["display_name"].tolist())
                selected_row = employee_df[employee_df["display_name"] == selected_employee].iloc[0]

            col1, col2 = st.columns(2)

            with col1:
                st.text_input("Employee Number", value=selected_row["employee_id"], disabled=True)
                st.text_input("Employee Name", value=selected_row["name"], disabled=True)
                st.text_input("Department", value=selected_row["department"], disabled=True)

            with col2:
                leave_type = st.selectbox(
                    "Leave Type *",
                    ["Casual Leave", "Sick Leave", "Earned Leave", "Emergency Leave"]
                )
                start_date = st.date_input("Start Date *", date.today())
                end_date = st.date_input("End Date *", date.today())

            reason = st.text_area("Reason for Leave *")
            total_days = (end_date - start_date).days + 1

            st.info(f"Calculated Leave Days: {total_days}")

            submit = st.form_submit_button("Submit Leave Request")

            if submit:
                if total_days <= 0:
                    st.error("End date should be after start date.")
                elif not reason.strip():
                    st.error("Please enter reason for leave.")
                else:
                    r = requests.post(
                        f"{API_URL}/apply-leave/",
                        params={
                            "employee_id": selected_row["employee_id"],
                            "employee_name": selected_row["name"],
                            "leave_type": leave_type,
                            "start_date": str(start_date),
                            "end_date": str(end_date),
                            "total_days": total_days,
                            "reason": reason
                        }
                    )

                    if r.status_code == 200:
                        st.success("Leave request submitted successfully. It is now visible in Manager Approval Dashboard.")
                    else:
                        st.error("Unable to submit leave request.")

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------- MANAGER APPROVAL --------------------

elif menu == "✅ Manager Approval Dashboard":
    if leave_df.empty:
        st.info("No leave requests available.")
    else:
        pending_df = leave_df[leave_df["status"].astype(str).str.strip().str.lower() == "pending"]

        p1, p2, p3 = st.columns(3)
        p1.markdown(f'<div class="metric-card"><div class="metric-title">Pending Approvals</div><div class="metric-value">{len(pending_df)}</div></div>', unsafe_allow_html=True)
        p2.markdown(f'<div class="metric-card"><div class="metric-title">Total Requests</div><div class="metric-value">{len(leave_df)}</div></div>', unsafe_allow_html=True)
        p3.markdown(f'<div class="metric-card"><div class="metric-title">Approval Queue</div><div class="metric-value">{len(pending_df)}</div></div>', unsafe_allow_html=True)

        st.write("")

        if pending_df.empty:
            st.success("No pending approvals. All leave requests are completed.")

        for _, row in pending_df.iterrows():
            emp_dept = "Not Available"

            if not employee_df.empty:
                match = employee_df[employee_df["employee_id"] == row["employee_id"]]
                if not match.empty:
                    emp_dept = match.iloc[0]["department"]

            st.markdown(f"""
            <div class="approval-card">
                <div class="approval-title">Leave Request #{row['id']}</div>
                <div class="info-row"><span class="info-label">Employee Number:</span> {row['employee_id']}</div>
                <div class="info-row"><span class="info-label">Employee Name:</span> {row['employee_name']}</div>
                <div class="info-row"><span class="info-label">Department:</span> {emp_dept}</div>
                <div class="info-row"><span class="info-label">Leave Type:</span> {row['leave_type']}</div>
                <div class="info-row"><span class="info-label">Duration:</span> {row['start_date']} to {row['end_date']}</div>
                <div class="info-row"><span class="info-label">Total Days:</span> {row['total_days']}</div>
                <div class="info-row"><span class="info-label">Reason:</span> {row['reason']}</div>
                <div class="info-row"><span class="info-label">Status:</span> {status_badge(row['status'])}</div>
            </div>
            """, unsafe_allow_html=True)

            c1, c2, c3 = st.columns([1, 1, 5])

            if c1.button("Approve", key=f"approve_{row['id']}"):
                requests.put(f"{API_URL}/leave/{row['id']}/approve")
                st.success("Leave approved.")
                st.rerun()

            if c2.button("Reject", key=f"reject_{row['id']}"):
                requests.put(f"{API_URL}/leave/{row['id']}/reject")
                st.error("Leave rejected.")
                st.rerun()


# -------------------- EMPLOYEE DIRECTORY --------------------

elif menu == "👥 Employee Directory":
    st.markdown('<div class="card"><div class="card-title">Employee Directory</div>', unsafe_allow_html=True)

    if not employee_df.empty:
        search = st.text_input("Search Employee", placeholder="Search by name, employee number, department, manager")
        display_df = employee_df.copy()

        if search:
            search_lower = search.lower()
            display_df = display_df[
                display_df.astype(str).apply(lambda row: row.str.lower().str.contains(search_lower).any(), axis=1)
            ]

        c1, c2, c3 = st.columns(3)
        c1.metric("Employees", len(display_df))
        c2.metric("Departments", display_df["department"].nunique())
        c3.metric("Managers", display_df["manager"].nunique())

        st.write("")
        st.markdown("### Employee Cards")

        cards_df = display_df.head(12)

        for i in range(0, len(cards_df), 3):
            cols = st.columns(3)

            for j, col in enumerate(cols):
                if i + j < len(cards_df):
                    row = cards_df.iloc[i + j]
                    initials = "".join([p[0] for p in row["name"].split()[:2]]).upper()

                    col.markdown(f"""
                    <div class="employee-card">
                        <div class="employee-avatar">{initials}</div>
                        <div class="employee-name">{row['name']}</div>
                        <div class="employee-meta"><b>Employee Number:</b> {row['employee_id']}</div>
                        <div class="employee-meta"><b>Gender:</b> {row['gender']}</div>
                        <div class="employee-meta"><b>Designation:</b> {row['designation']}</div>
                        <div class="employee-meta"><b>Email:</b> {row['email']}</div>
                        <div class="employee-meta"><b>Manager:</b> {row['manager']}</div>
                        <div class="employee-tag">{row['department']}</div>
                    </div>
                    """, unsafe_allow_html=True)

        st.markdown("### Complete Employee Table")

        clean_df = display_df.rename(columns={
            "employee_id": "Employee Number",
            "name": "Employee Name",
            "department": "Department",
            "designation": "Designation",
            "email": "Email",
            "manager": "Reporting Manager",
            "gender": "Gender"
        })

        st.dataframe(
            clean_df[["Employee Number", "Employee Name", "Gender", "Department", "Designation", "Email", "Reporting Manager"]],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No employees found.")

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------- LEAVE STATISTICS --------------------

elif menu == "📊 Leave Statistics":
    st.markdown('<div class="card"><div class="card-title">Leave Analytics Dashboard</div>', unsafe_allow_html=True)

    if not leave_df.empty:
        col1, col2 = st.columns(2)

        with col1:
            status_count = leave_df.groupby("status").size().reset_index(name="count")
            fig = px.pie(
                status_count,
                names="status",
                values="count",
                hole=0.45,
                title="Leave Status Distribution"
            )
            st.plotly_chart(clean_pie(fig), use_container_width=True)

        with col2:
            type_count = leave_df.groupby("leave_type").size().reset_index(name="count")
            fig = px.bar(
                type_count,
                x="leave_type",
                y="count",
                text="count",
                title="Leave Type Analysis",
                labels={"leave_type": "Leave Type", "count": "Number of Requests"}
            )
            fig.update_traces(textposition="outside", cliponaxis=False)
            fig.update_xaxes(tickangle=-20)
            st.plotly_chart(clean_plot(fig), use_container_width=True)

        if not employee_df.empty:
            merged = leave_df.merge(employee_df[["employee_id", "department"]], on="employee_id", how="left")
            dept_count = merged.groupby("department").size().reset_index(name="count")

            fig = px.bar(
                dept_count,
                x="department",
                y="count",
                text="count",
                title="Department-wise Leave Requests",
                labels={"department": "Department", "count": "Leave Requests"}
            )
            fig.update_traces(textposition="outside", cliponaxis=False)
            st.plotly_chart(clean_plot(fig, 440), use_container_width=True)

    else:
        st.info("No leave statistics available.")

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------- LEAVE HISTORY --------------------

elif menu == "📄 Leave History":
    st.markdown('<div class="card"><div class="card-title">Leave History</div>', unsafe_allow_html=True)

    if not leave_df.empty:
        display_leave_df = leave_df.copy()

        if st.session_state.role == "Employee":
            display_leave_df = display_leave_df[
                display_leave_df["employee_id"] == st.session_state.user_id
            ]

        if not display_leave_df.empty:
            clean_df = display_leave_df.rename(columns={
                "employee_id": "Employee Number",
                "employee_name": "Employee Name",
                "leave_type": "Leave Type",
                "start_date": "Start Date",
                "end_date": "End Date",
                "total_days": "Total Days",
                "reason": "Reason",
                "status": "Status"
            })

            st.dataframe(
                clean_df[["Employee Number", "Employee Name", "Leave Type", "Start Date", "End Date", "Total Days", "Reason", "Status"]],
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("No leave history found for this employee.")
    else:
        st.info("No leave history found.")

    st.markdown('</div>', unsafe_allow_html=True)
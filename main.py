import streamlit as st

from services.auth_service import cookies, login, logout
from utils.constants import ROLES

# if "role" not in st.session_state:
#     st.session_state.role = None

# Restore role from cookie if session is empty
if "role" not in st.session_state:
    saved_role = cookies.get("role")
    if saved_role in ROLES:
        st.session_state.role = saved_role
    else:
        st.session_state.role = None

# if st.session_state.get("role"):
#     st.sidebar.success(f"Global Logged in as: {st.session_state.role}")
# else:
#     st.sidebar.warning("Not logged in")


role = st.session_state.role
print(f"Current role: {role=}")


user_1 = st.Page(
    "user/user_1.py",
    title="User Page",
    icon=":material/person:",
    default=(role == "User"),
)
user_2 = st.Page(
    "user/user_2.py",
    title="User Page 2",
    icon=":material/person:",
)

manager_1 = st.Page(
    "manager/manager_1.py",
    title="Manager Page",
    icon=":material/supervisor_account:",
    default=(role == "Manager"),
)
manager_2 = st.Page(
    "manager/manager_2.py",
    title="Manager Page 2",
    icon=":material/supervisor_account:",
)

admin_1 = st.Page(
    "admin/admin_1.py",
    title="Admin Page",
    icon=":material/admin_panel_settings:",
    default=(role == "Admin"),
)
admin_2 = st.Page(
    "admin/admin_2.py",
    title="Admin Page 2",
    icon=":material/admin_panel_settings:",
)

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
data_page = st.Page(
    "services/db_service.py", title="Data Page", icon=":material/database:"
)
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")

account_pages = [settings, logout_page, data_page]
user_pages = [user_1, user_2]
manager_pages = [manager_1, manager_2]
admin_pages = [admin_1, admin_2]

st.title("Request manager")

page_dict = {}

if role in ["User", "Manager", "Admin"]:
    page_dict["User"] = user_pages
if role in ["Manager", "Admin"]:
    page_dict["Manager"] = manager_pages
if role == "Admin":
    page_dict["Admin"] = admin_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()

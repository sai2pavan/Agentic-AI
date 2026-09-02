#Day 43: Introduction to streamlit and its features

# University Management System using Python and Streamlit

import streamlit as st  #used for fronted development

# config the fronted page

st .set_page_config(
    page_title="University Management System", 
    layout="wide"
)

# page title
st.title("University Management Portal")

# creating a empyt list of colleges data
if ("colleges" not in st.session_state):
    st.session_state.colleges = []

#side bar menu
menu_choice = st.sidebar.selectbox(
    "SELECT ACTION",
    (
    "CREATE COLLEGE",
    "ADD STUDENT",
    "ADD TEACHER",
    "DISPLAY STUDENTS",
    "DISPLAY TEACHERS",
    "DISPLAY COLLEGES",
    )
)
class college:
    def __init__(self,cname): 
        self.cname = cname
        self.students = [] # empty list to store students data
        self.teachers = [] # empty list to store teachers data

    def add_student(self, student_name):
        self.students.append(student_name) # adding student name to the list of students
    def add_teacher(self, teacher_name):
        self.teachers.append(teacher_name) # adding teacher name to the list of teachers

# this function is used to find the college object by name from the list of colleges
    
def find_college(college_name):
    return next((clg for clg in st.session_state.colleges if clg.cname == college_name), None) # finding the college object by name
# creating new college
if menu_choice == "CREATE COLLEGE":
    cname = st.text_input("Enter New College Name")
    if st.button("CREATE"):
        clg_obj = college(cname) #creation a college class object 
        st.session_state.colleges.append(clg_obj) # storing the college object in the list of colleges
        st.success(f"College {cname} created successfully!") # success message  

# Adding student to the college
elif menu_choice == "ADD STUDENT":
    if not st.session_state.colleges:
        st.info("No colleges available. Please create a college first.")
    else:
        college_names = st.selectbox("Select or Choose College", [clg.cname for clg in st.session_state.colleges])
        roll_number = st.text_input("Enter Student Roll Number:")
        student_name = st.text_input("Enter Student Name:")
        branch = st.text_input("Enter Student Branch:")
        if st.button("ADD STUDENT"):
            if not (college_names and roll_number and student_name and branch):                st.error("Please enter or  fill all the above information.")
            else:
                clg = find_college(college_names)
                stu_obj = student(roll_number, student_name, branch) # creating a student class object
                clg.add_student(stu_obj) # adding the student object to the college
                st.success(f"Student {student_name} added to {college_names} successfully!") #

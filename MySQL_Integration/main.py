#  Solving exercises from the https://pynative.com/python-database-programming-exercise-with-solution/

import mysql.connector
import datetime
def get_connection():
    connection = mysql.connector.connect(host="localhost",
                                         database="python_db",
                                         user="root",
                                         password=""   
                                         )
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("You are connected to a MySQL database of version: {}".format(db_version))
        close_connection(connection)
    except(Exception, mysql.connector.Error) as error:
        print("Error while getting data {}".format(error))

print("Question 1: Print Database Version")
read_database_version()

def get_hospital_detail(hospital_id):
    try:
        query = "SELECT * FROM Hospital where hospital_id=%s"
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query,(hospital_id,))
        records = cursor.fetchall()
        print("Printing Hospital Record")
        for line in records:
            print("Hospital Id",line[0])
            print("Hospital Name",line[1])
            print("Bed count",line[2])
        close_connection(connection)
    except(Exception, mysql.connector.Error) as error:
        print("Error while getting data {}".format(error))

def get_doctor_detail(doctor_id):
    try:
        query = "SELECT * FROM Doctor where doctor_id=%s"
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query,(doctor_id,))
        records = cursor.fetchall()
        print("Printing Doctor record")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6])
        close_connection(connection)
    except(Exception, mysql.connector.Error) as error:
        print("Error while getting data {}".format(error))

print("Question 2: Read given hospital and doctor details \n")
get_hospital_detail(1)
print("\n")
get_doctor_detail(101)

def get_specialist_doctors_list(speciality, salary):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM Doctor where salary > %s AND speciality=%s"
        params = (salary,speciality)
        cursor.execute(query,params)
        records = cursor.fetchall()
        print("Printing Doctor record")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6])
        close_connection(connection)
    except(Exception,mysql.connector.Error) as error:
        print("Error while getting data {}".format(error))

print("Question 3: Get Doctors as per given Speciality\n")
get_specialist_doctors_list("Pediatric",20000)

def get_doctors(hospital_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        # Fetching hospital name
        query_hospital = "SELECT Hospital_Name from Hospital where hospital_id=%s"
        params_query_hospital = (hospital_id,)
        cursor.execute(query_hospital,params_query_hospital)
        hospital_name = cursor.fetchone()
        # Fetching the hospital's doctors
        query_doctors_hospital = "SELECT * FROM Doctor where hospital_id=%s"
        cursor.execute(query_doctors_hospital,params_query_hospital)
        doctors = cursor.fetchall()
        print("The hospital name is {} \n".format(hospital_name))
        for d in doctors:
            print("Doctor Id:", d[0])
            print("Doctor Name:", d[1])
            print("Hospital Id:", d[2])
            print("Joining Date:", d[3])
            print("Specialty:", d[4])
            print("Salary:", d[5])
            print("Experience:", d[6])
            print("\n")
    except(Exception,mysql.connector.Error) as error:
        print("Error while getting data {}".format(error))

print("Question 4:  Get List of doctors of a given Hospital Id\n")
get_doctors(1)

def update_doctor_experience(doctor_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        # Fetching doctor joining date
        query_date = "SELECT Joining_Date from Doctor where doctor_id=%s"
        query_params = (doctor_id,)
        cursor.execute(query_date,query_params)
        join_date = cursor.fetchone()[0]
        # Calculate experience
        experience_diff = datetime.date.today() - join_date
        experience_years = int(experience_diff.days / 365)
        # Updating doctor record
        query_update = "UPDATE Doctor set experience=%s where doctor_id=%s"
        query_update_params = (experience_years,doctor_id)
        cursor.execute(query_update,query_update_params)
        connection.commit()
        print("Doctor record updated")
        # Closing the connection
        close_connection(connection)
    except(Exception,mysql.connector.Error) as error:
        print("Error while getting data {}".format(error))

print("Question 5: Calculate and Update experience of all doctors  \n")
update_doctor_experience(101)

def insert_hospital_record():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        values = (65,"Superman clinic",700)
        query = "INSERT INTO Hospital (hospital_id,hospital_name,bed_count) VALUES (%s,%s,%s);"
        cursor.execute(query,values)
        connection.commit()
        close_connection(connection)
    except(Exception, mysql.connector.Error) as error:
        print("Error while getting data {}".format(error))

print("(Extra) Question 6: Insert a new hospital record")
insert_hospital_record()

def remove_hospital_record():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "DELETE FROM Hospital where hospital_id=%s"
        cursor.execute(query,(65,))
        connection.commit()
        print("Medical record deleted")
        close_connection(connection)
    except(Exception, mysql.connector.Error) as error:
        print("Error while getting data {}".format(error))


print("(Extra) Question 7: Remove a hospital record")
remove_hospital_record()


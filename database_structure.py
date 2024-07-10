import pymysql as pmql
def connect_to_database():
        connection = pmql.connect(
            host="localhost",
            user="root",
            password="root",
            port=3306,
            charset="utf8"
        )
        cur=connection.cursor()
        cur.execute("create database if not exists demo;")
        cur.execute("use demo")

        cur.execute("create table if not exists user (user_id int primary key,password varchar(30) not null, first_name varchar(50),last_name varchar(70));")
        cur.execute('''CREATE TABLE if not exists event (event_id INT AUTO_INCREMENT PRIMARY KEY,event_name VARCHAR(100),event_category VARCHAR(100),start_date DATE,end_date DATE,end_time TIME,start_time TIME,user_id INT,FOREIGN KEY (user_id) REFERENCES user(user_id));''')
        cur.execute('''CREATE TABLE  if not exists sponsor (
                    sponsor_id INT AUTO_INCREMENT PRIMARY KEY,
                    sponsor_name VARCHAR(100),
                    email VARCHAR(100),
                    event_id INT,
                    amount varchar(20),
                    user_id INT,
                    FOREIGN KEY (user_id) REFERENCES user(user_id),
                    FOREIGN KEY (event_id) REFERENCES event(event_id));''')
        cur.execute('''CREATE TABLE if not exists registration (
                   registration_id INT AUTO_INCREMENT PRIMARY KEY,
                   user_id INT,
                   event_id INT,
                   email varchar(100), 
                   first_name varchar(50),
                   last_name varchar(50),
                   registration_date DATE,
                   status VARCHAR(50),
                   FOREIGN KEY (user_id) REFERENCES user(user_id),
                   FOREIGN KEY (event_id) REFERENCES event(event_id));''')
        cur.execute('''CREATE TABLE if not exists attendees (
                   attendee_id INT AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(100),
                   email VARCHAR(100),
                   event_id INT,
                   FOREIGN KEY (event_id) REFERENCES event(event_id));''')
        cur.execute('''CREATE TABLE if not exists feedback (
                   feedback_id INT AUTO_INCREMENT PRIMARY KEY,
                   feedback_text TEXT,
                   event_id INT,
                   email VARCHAR(100), 
                   FOREIGN KEY (event_id) REFERENCES event(event_id));''')
        cur.execute('''CREATE TABLE if not exists invitation (
                   invitation_id INT AUTO_INCREMENT PRIMARY KEY,
                   email VARCHAR(100),
                   invitation_type VARCHAR(100),
                   invitation_status VARCHAR(50),
                   event_id INT,
                   FOREIGN KEY (event_id) REFERENCES event(event_id));''')
        cur.execute("desc user;")
        out=cur.fetchall()[0]
        print(out)
        connection.rollback()
        connection.commit()
        connection.close()
        return connection,cur

def insert_dummy_data(connection, cur):
    try:
        # Insert dummy data into user table
        cur.execute("INSERT INTO user (password, first_name, last_name) VALUES ('password123', 'John', 'Doe');")
        cur.execute("INSERT INTO user (password, first_name, last_name) VALUES ('password456', 'Jane', 'Smith');")
        
        # Insert dummy data into event table
        cur.execute("INSERT INTO event (event_name, event_category, start_date, end_date, start_time, end_time, user_id) VALUES ('Conference 2024', 'Business', '2024-07-01', '2024-07-03', '09:00:00', '17:00:00', 1);")
        cur.execute("INSERT INTO event (event_name, event_category, start_date, end_date, start_time, end_time, user_id) VALUES ('Workshop 2024', 'Education', '2024-08-10', '2024-08-11', '10:00:00', '16:00:00', 2);")
        
        # Insert dummy data into sponsor table
        cur.execute("INSERT INTO sponsor (sponsor_name, email, event_id, amount, user_id) VALUES ('Sponsor A', 'sponsorA@example.com', 1, '5000', 1);")
        cur.execute("INSERT INTO sponsor (sponsor_name, email, event_id, amount, user_id) VALUES ('Sponsor B', 'sponsorB@example.com', 2, '3000', 2);")
        
        # Insert dummy data into registration table
        cur.execute("INSERT INTO registration (user_id, event_id, email, first_name, last_name, registration_date, status) VALUES (1, 1, 'john.doe@example.com', 'John', 'Doe', '2024-06-25', 'paid');")
        cur.execute("INSERT INTO registration (user_id, event_id, email, first_name, last_name, registration_date, status) VALUES (2, 2, 'jane.smith@example.com', 'Jane', 'Smith', '2024-07-25', 'not_paid');")
        
        # Insert dummy data into attendees table
        cur.execute("INSERT INTO attendees (name, email, event_id) VALUES ('Attendee A', 'attendeeA@example.com', 1);")
        cur.execute("INSERT INTO attendees (name, email, event_id) VALUES ('Attendee B', 'attendeeB@example.com', 2);")
        
        # Insert dummy data into feedback table
        cur.execute("INSERT INTO feedback (feedback_text, event_id, email) VALUES ('Great event!', 1, 'john.doe@example.com');")
        cur.execute("INSERT INTO feedback (feedback_text, event_id, email) VALUES ('Informative workshop.', 2, 'jane.smith@example.com');")
        
        # Insert dummy data into invitation table
        cur.execute("INSERT INTO invitation (email, invitation_type, invitation_status, event_id) VALUES ('inviteeA@example.com', 'VIP', 'sent', 1);")
        cur.execute("INSERT INTO invitation (email, invitation_type, invitation_status, event_id) VALUES ('inviteeB@example.com', 'General', 'accepted', 2);")

        connection.commit()
        print("Dummy data inserted successfully!")
    except pmql.MySQLError as e:
        print(f"Error inserting dummy data: {e}")
        connection.rollback()

connection, cur = connect_to_database()
insert_dummy_data(connection, cur)
cur.close()
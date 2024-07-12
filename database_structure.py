import pymysql as pmql
def connect_to_database():
        connection = pmql.connect(
            host="localhost",
            user="root",
            password="sankalp",
            #port=3307,
            charset="utf8",
            connect_timeout=5
        )
        cur=connection.cursor()
        cur.execute("create database if not exists demo;")
        cur.execute("use demo")

        cur.execute("create table if not exists user (user_id int primary key,email varchar(100) not null,password varchar(30) not null, first_name varchar(50),last_name varchar(70));")
        cur.execute("ALTER TABLE user MODIFY user_id INT AUTO_INCREMENT;")
        cur.execute("ALTER TABLE user AUTO_INCREMENT = 10;")
        cur.execute('''CREATE TABLE if not exists event (event_id INT AUTO_INCREMENT PRIMARY KEY,event_name VARCHAR(100),event_category VARCHAR(100),start_date DATE,end_date DATE,end_time TIME,start_time TIME,user_id INT,FOREIGN KEY (user_id) REFERENCES user(user_id));''')
        cur.execute("ALTER TABLE event MODIFY event_id INT AUTO_INCREMENT;")
        cur.execute("ALTER TABLE event AUTO_INCREMENT = 101;")
        cur.execute('''CREATE TABLE  if not exists sponsor (
                    sponsor_id INT AUTO_INCREMENT PRIMARY KEY,
                    sponsor_name VARCHAR(100),
                    email VARCHAR(100),
                    event_id INT,
                    amount varchar(20),
                    user_id INT,
                    FOREIGN KEY (user_id) REFERENCES user(user_id),
                    FOREIGN KEY (event_id) REFERENCES event(event_id));''')
        cur.execute("ALTER TABLE sponsor MODIFY sponsor_id INT AUTO_INCREMENT;")
        cur.execute("ALTER TABLE sponsor AUTO_INCREMENT = 1001;")
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
        cur.execute("ALTER TABLE registration MODIFY registration_id INT AUTO_INCREMENT;")
        cur.execute("ALTER TABLE registration AUTO_INCREMENT = 1;")
        cur.execute('''CREATE TABLE if not exists attendees (
                   attendee_id INT AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(100),
                   email VARCHAR(100),
                   event_id INT,
                   FOREIGN KEY (event_id) REFERENCES event(event_id));''')
        cur.execute("ALTER TABLE attendees MODIFY attendee_id INT AUTO_INCREMENT;")
        cur.execute("ALTER TABLE attendees AUTO_INCREMENT = 100;")
        cur.execute('''CREATE TABLE if not exists feedback (
                   feedback_id INT AUTO_INCREMENT PRIMARY KEY,
                   feedback_text TEXT,
                   event_id INT,
                   email VARCHAR(100), 
                   FOREIGN KEY (event_id) REFERENCES event(event_id));''')
        cur.execute("ALTER TABLE feedback MODIFY feedback_id INT AUTO_INCREMENT;")
        cur.execute("ALTER TABLE feedback AUTO_INCREMENT = 11;")
        cur.execute('''CREATE TABLE if not exists invitation (
                   invitation_id INT AUTO_INCREMENT PRIMARY KEY,
                   email VARCHAR(100),
                   invitation_type VARCHAR(100),
                   invitation_status VARCHAR(50),
                   event_id INT,
                   FOREIGN KEY (event_id) REFERENCES event(event_id));''')

        
        
        
        
        
        cur.execute("ALTER TABLE invitation MODIFY invitation_id INT AUTO_INCREMENT;")
        cur.execute("ALTER TABLE invitation AUTO_INCREMENT = 1000;")
        cur.execute("desc user;")
        out=cur.fetchall()[0]
        print(out)
        connection.rollback()
        connection.commit()
        connection.close()
        return connection,cur

def insert_dummy_data():
    connection = pmql.connect(
            host="localhost",
            user="root",
            password="sankalp",
            #port=3307,
            charset="utf8",
            connect_timeout=5
        )
    cur=connection.cursor()
    cur.execute("create database if not exists demo;")
    cur.execute("use demo")
        # Insert dummy data into user table
    cur.execute("INSERT INTO user (email, password, first_name, last_name) VALUES ('john.doe@example.com', 'password123', 'John', 'Doe');")
    cur.execute("INSERT INTO user (email, password, first_name, last_name) VALUES ('jane.smith@example.com', 'password456', 'Jane', 'Smith');")
    cur.execute("INSERT INTO user (email, password, first_name, last_name) VALUES ('james.smith@example.com', 'password456', 'James', 'Smith');")
    cur.execute("INSERT INTO user (email, password, first_name, last_name) VALUES ('joo.smith@example.com', 'password456', 'Joo', 'Smith');")
    
#Insert dummy data into event table
    cur.execute("INSERT INTO event (event_name, event_category, start_date, end_date, start_time, end_time, user_id) VALUES ('Conference 2024', 'Business', '2024-07-01', '2024-07-03', '09:00:00', '17:00:00', 10);")
    cur.execute("INSERT INTO event (event_name, event_category, start_date, end_date, start_time, end_time, user_id) VALUES ('Tech Summit', 'Technology', '2024-08-15', '2024-08-17', '10:00:00', '18:00:00', 12);")
    cur.execute("INSERT INTO event (event_name, event_category, start_date, end_date, start_time, end_time, user_id) VALUES ('Health Expo', 'Health', '2024-09-05', '2024-09-07', '09:00:00', '17:00:00', 10);")
    cur.execute("INSERT INTO event (event_name, event_category, start_date, end_date, start_time, end_time, user_id) VALUES ('Education Fair', 'Education', '2024-10-10', '2024-10-12', '10:00:00', '18:00:00', 12);")
    
    # # Insert dummy data into sponsor table
    cur.execute("INSERT INTO sponsor (sponsor_name, email, event_id, amount, user_id) VALUES ('Company A', 'contact@companya.com', 101, '5000', 10);")
    cur.execute("INSERT INTO sponsor (sponsor_name, email, event_id, amount, user_id) VALUES ('Company B', 'info@companyb.com', 102, '10000', 12);")
    cur.execute("INSERT INTO sponsor (sponsor_name, email, event_id, amount, user_id) VALUES ('Company C', 'support@companyc.com', 101, '7500', 10);")
    cur.execute("INSERT INTO sponsor (sponsor_name, email, event_id, amount, user_id) VALUES ('Company D', 'hello@companyd.com', 102, '12000', 12);")
    
    # # Insert dummy data into registration table
    cur.execute("INSERT INTO registration (user_id, event_id, email, first_name, last_name, registration_date, status) VALUES (10, 101, 'john.doe@example.com', 'John', 'Doe', '2024-06-25', 'confirmed');")
    cur.execute("INSERT INTO registration (user_id, event_id, email, first_name, last_name, registration_date, status) VALUES (12, 102, 'jane.smith@example.com', 'Jane', 'Smith', '2024-07-30', 'confirmed');")
    cur.execute("INSERT INTO registration (user_id, event_id, email, first_name, last_name, registration_date, status) VALUES (10, 103, 'john.doe@example.com', 'John', 'Doe', '2024-08-20', 'confirmed');")
    cur.execute("INSERT INTO registration (user_id, event_id, email, first_name, last_name, registration_date, status) VALUES (12, 104, 'jane.smith@example.com', 'Jane', 'Smith', '2024-09-15', 'confirmed');")
    
    # # Insert dummy data into attendees table
    cur.execute("INSERT INTO attendees (name, email, event_id) VALUES ('Attendee One', 'attendee1@example.com', 101);")
    cur.execute("INSERT INTO attendees (name, email, event_id) VALUES ('Attendee Two', 'attendee2@example.com', 102);")
    cur.execute("INSERT INTO attendees (name, email, event_id) VALUES ('Attendee Three', 'attendee3@example.com', 103);")
    cur.execute("INSERT INTO attendees (name, email, event_id) VALUES ('Attendee Four', 'attendee4@example.com', 104);")
    
    # # Insert dummy data into feedback table
    cur.execute("INSERT INTO feedback (feedback_text, event_id, email) VALUES ('Great event!', 101, 'attendee1@example.com');")
    cur.execute("INSERT INTO feedback (feedback_text, event_id, email) VALUES ('Very informative.', 102, 'attendee2@example.com');")
    cur.execute("INSERT INTO feedback (feedback_text, event_id, email) VALUES ('Well organized.', 103, 'attendee3@example.com');")
    cur.execute("INSERT INTO feedback (feedback_text, event_id, email) VALUES ('Excellent speakers.', 104, 'attendee4@example.com');")
    
    # # Insert dummy data into invitation table
    cur.execute("INSERT INTO invitation (email, invitation_type, invitation_status, event_id) VALUES ('invitee1@example.com', 'VIP', 'accepted', 101);")
    cur.execute("INSERT INTO invitation (email, invitation_type, invitation_status, event_id) VALUES ('invitee2@example.com', 'General', 'pending', 102);")
    cur.execute("INSERT INTO invitation (email, invitation_type, invitation_status, event_id) VALUES ('invitee3@example.com', 'VIP', 'rejected', 103);")
    cur.execute("INSERT INTO invitation (email, invitation_type, invitation_status, event_id) VALUES ('invitee4@example.com', 'General', 'accepted', 104);")
    
    connection.commit()
    connection.close()

connection, cur = connect_to_database()
insert_dummy_data()
cur.close()

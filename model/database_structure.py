import pymysql as pmql

class Db():
      def __init__(self, main_app) :
            self.main = main_app
            self.connection= pmql.connect(
                  host="localhost",
                  user="root",
                  password="root",
                  charset="utf8",
                  # port = 3307
        )
            self.cur=self.connection.cursor()
            

      def create_database(self):
        self.db_name = "demo"
        query = f"create database if not exists {self.db_name};"
        created = self.cur.execute(query)
        if created:
            self.data=self.cur.execute("use demo")

            self.cur.execute("create table if not exists user (user_id int primary key,email varchar(100) not null,password varchar(30) not null, first_name varchar(50),last_name varchar(70));")
            self.cur.execute("ALTER TABLE user MODIFY user_id INT AUTO_INCREMENT;")
            self.cur.execute("ALTER TABLE user AUTO_INCREMENT = 10;")
            self.cur.execute('''CREATE TABLE if not exists event (event_id INT AUTO_INCREMENT PRIMARY KEY,event_name VARCHAR(100),event_category ENUM('Meeting', 'Seminar', 'Training Session', 'Political Events', 'Fundraisers','Celebration','Sports Event','Webinar'),address varchar(100),start_date DATE,end_date DATE,end_time TIME,start_time TIME,user_id INT,FOREIGN KEY (user_id) REFERENCES user(user_id));''')
            self.cur.execute("ALTER TABLE event MODIFY event_id INT AUTO_INCREMENT;")
            self.cur.execute("ALTER TABLE event AUTO_INCREMENT = 101;")
            self.cur.execute('''CREATE TABLE  if not exists sponsor (
                        sponsor_id INT AUTO_INCREMENT PRIMARY KEY,
                        sponsor_name VARCHAR(100),
                        email VARCHAR(100),
                        event_id INT,
                        amount varchar(20),
                        user_id INT,
                        FOREIGN KEY (user_id) REFERENCES user(user_id),
                        FOREIGN KEY (event_id) REFERENCES event(event_id));''')
            self.cur.execute("ALTER TABLE sponsor MODIFY sponsor_id INT AUTO_INCREMENT;")
            self.cur.execute("ALTER TABLE sponsor AUTO_INCREMENT = 1001;")
            self.cur.execute('''CREATE TABLE if not exists registration (
                        registration_id INT AUTO_INCREMENT PRIMARY KEY,
                        event_id INT,
                        organisation_name varchar(50),
                        email varchar(100), 
                        first_name varchar(50),
                        last_name varchar(50),
                        registration_date DATE,
                        contact_no varchar(12), 
                        status VARCHAR(50),
                        FOREIGN KEY (event_id) REFERENCES event(event_id));''')
            self.cur.execute("ALTER TABLE registration MODIFY registration_id INT AUTO_INCREMENT;")
            self.cur.execute("ALTER TABLE registration AUTO_INCREMENT = 1;")
            self.cur.execute('''CREATE TABLE if not exists attendees (
                        attendee_id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(100),
                        email VARCHAR(100),
                        event_id INT,
                        FOREIGN KEY (event_id) REFERENCES event(event_id));''')
            self.cur.execute("ALTER TABLE attendees MODIFY attendee_id INT AUTO_INCREMENT;")
            self.cur.execute("ALTER TABLE attendees AUTO_INCREMENT = 100;")
            self.cur.execute('''CREATE TABLE if not exists survey (
                        survey_id INT AUTO_INCREMENT PRIMARY KEY,
                        survey_name VARCHAR(100),
                        event_id INT,
                        FOREIGN KEY (event_id) REFERENCES event(event_id));''')
            self.cur.execute('''CREATE TABLE if not exists surveyResponse (
                        response_id INT AUTO_INCREMENT PRIMARY KEY, 
                        survey_id int,
                        response VARCHAR(100), 
                        FOREIGN KEY (survey_id) REFERENCES survey(survey_id));''')

            self.cur.execute('''CREATE TABLE if not exists feedback (
                        feedback_id INT AUTO_INCREMENT PRIMARY KEY,
                        feedback_text TEXT,
                        event_id INT,
                        email VARCHAR(100), 
                        FOREIGN KEY (event_id) REFERENCES event(event_id));''')
            self.cur.execute("ALTER TABLE feedback MODIFY feedback_id INT AUTO_INCREMENT;")
            self.cur.execute("ALTER TABLE feedback AUTO_INCREMENT = 11;")
            self.cur.execute('''CREATE TABLE if not exists invitation (
                        invitation_id INT AUTO_INCREMENT PRIMARY KEY,
                        email VARCHAR(100),
                        invitation_type ENUM('Speaker', 'VIP', 'Normal'),
                        invitation_status VARCHAR(50),
                        event_id INT,
                        FOREIGN KEY (event_id) REFERENCES event(event_id));''')

            self.cur.execute("ALTER TABLE invitation MODIFY invitation_id INT AUTO_INCREMENT;")
            self.cur.execute("ALTER TABLE invitation AUTO_INCREMENT = 1000;")
            self.cur.execute("desc user;")
            # out=self.cur.fetchall()[0]
            # print(out)
            self.connection.rollback()
            self.connection.commit()
            self.connection.close()
            return self.connection,self.cur
        else: 
            self.cur.close()
            try:
                  self.main.connect_to_database
            except:
                  print("Can't connect to database..")

      def insert_dummy_data(self):
          self.cur.execute("use demo")
        # Insert dummy data into user table
          self.cur.execute("INSERT INTO user (email, password, first_name, last_name) VALUES ('jane.smith@example.com', 'password456', 'Jane', 'Smith');")
          self.cur.execute("INSERT INTO user (email, password, first_name, last_name) VALUES ('james.smith@example.com', 'password456', 'James', 'Smith');")
    
#Insert dummy data into event table // event_categoryv datatype enum karna haii-- done
          self.cur.execute("INSERT INTO event (event_name, event_category,address ,start_date, end_date, start_time, end_time, user_id) VALUES ('Tech Summit', 'Training Session',' we dont know' ,'2024-08-15', '2024-08-17', '10:00:00', '18:00:00', 12);")
          self.cur.execute("INSERT INTO event (event_name, event_category,address , start_date, end_date, start_time, end_time, user_id) VALUES ('Health Expo', 'Seminar', ' we dont know'',2024-09-05', '2024-09-07', '09:00:00', '17:00:00', 10);")
          self.cur.execute("INSERT INTO event (event_name, event_category, address ,start_date, end_date, start_time, end_time, user_id) VALUES ('Education Fair', 'Webinar',' we dont know' ,'2024-10-10', '2024-10-12', '10:00:00', '18:00:00', 12);")
    
    # # Insert dummy data into sponsor table 
          self.cur.execute("create database if not exists demo;")
          self.cur.execute("INSERT INTO sponsor (sponsor_name, email, event_id, amount, user_id) VALUES ('Company B', 'info@companyb.com', 102, '10000', 12);")
          self.cur.execute("INSERT INTO sponsor (sponsor_name, email, event_id, amount, user_id) VALUES ('Company C', 'support@companyc.com', 101, '7500', 10);")
          self.cur.execute("INSERT INTO user (email, password, first_name, last_name) VALUES ('john.doe@example.com', 'password123', 'John', 'Doe');")
    
    # # Insert dummy data into registration table   # ORGANISATION NAME ADD phone no and delete user id---done
          self.cur.execute("INSERT INTO user (email, password, first_name, last_name) VALUES ('joo.smith@example.com', 'password456', 'Joo', 'Smith');")
          self.cur.execute("INSERT INTO registration (event_id, email, first_name, last_name, registration_date, status) VALUES ( 102, 'jane.smith@example.com', 'Jane', 'Smith', '2024-07-30', 'confirmed');")
          self.cur.execute("INSERT INTO registration ( event_id, email, first_name, last_name, registration_date, status) VALUES ( 103, 'john.doe@example.com', 'John', 'Doe', '2024-08-20', 'confirmed');")
          self.cur.execute("INSERT INTO event (event_name, event_category, start_date, end_date, start_time, end_time, user_id) VALUES ('Conference 2024', 'Meeting', '2024-07-01', '2024-07-03', '09:00:00', '17:00:00', 10);")
          self.cur.execute("INSERT INTO registration ( event_id, email, first_name, last_name, registration_date, status) VALUES ( 104, 'jane.smith@example.com', 'Jane', 'Smith', '2024-09-15', 'confirmed');")
    
    # # Insert dummy data into attendees table
          self.cur.execute("INSERT INTO attendees (name, email, event_id) VALUES ('Attendee Two', 'attendee2@example.com', 102);")
          self.cur.execute("INSERT INTO attendees (name, email, event_id) VALUES ('Attendee Three', 'attendee3@example.com', 103);")
          self.cur.execute("INSERT INTO sponsor (sponsor_name, email, event_id, amount, user_id) VALUES ('Company A', 'contact@companya.com', 101, '5000', 10);")
          self.cur.execute("INSERT INTO attendees (name, email, event_id) VALUES ('Attendee Four', 'attendee4@example.com', 104);")
 
          self.cur.execute("INSERT INTO sponsor (sponsor_name, email, event_id, amount, user_id) VALUES ('Company D', 'hello@companyd.com', 102, '12000', 12);")
    # # Insert dummy data into feedback table
          self.cur.execute("INSERT INTO feedback (feedback_text, event_id, email) VALUES ('Very informative.', 102, 'attendee2@example.com');")
          self.cur.execute("INSERT INTO registration ( event_id, email, first_name, last_name, registration_date, status) VALUES ( 101, 'john.doe@example.com', 'John', 'Doe', '2024-06-25', 'confirmed');")
          self.cur.execute("INSERT INTO feedback (feedback_text, event_id, email) VALUES ('Well organized.', 103, 'attendee3@example.com');")
          self.cur.execute("INSERT INTO feedback (feedback_text, event_id, email) VALUES ('Excellent speakers.', 104, 'attendee4@example.com');")
    
    # # Insert dummy data into invitation table // invitation type ko datatype enum karna haii --- done
          self.cur.execute("INSERT INTO invitation (email, invitation_type, invitation_status, event_id) VALUES ('invitee1@example.com', 'VIP', 'accepted', 101);")
          self.cur.execute("INSERT INTO attendees (name, email, event_id) VALUES ('Attendee One', 'attendee1@example.com', 101);")
          self.cur.execute("INSERT INTO invitation (email, invitation_type, invitation_status, event_id) VALUES ('invitee2@example.com', 'Normal', 'pending', 102);")
          self.cur.execute("INSERT INTO invitation (email, invitation_type, invitation_status, event_id) VALUES ('invitee3@example.com', 'VIP', 'rejected', 103);")
          self.cur.execute("INSERT INTO invitation (email, invitation_type, invitation_status, event_id) VALUES ('invitee4@example.com', 'Normal', 'accepted', 104);")
    # survey table create karna haii -- tables are done data in not inserted
          self.cur.execute("INSERT INTO invitation (email, invitation_type, invitation_status, event_id) VALUES ('invitee5@example.com', 'Speaker', 'accepted', 104);")
    
          self.cur.execute("INSERT INTO feedback (feedback_text, event_id, email) VALUES ('Great event!', 101, 'attendee1@example.com');")
          self.connection.commit()
          self.connection.close()



      







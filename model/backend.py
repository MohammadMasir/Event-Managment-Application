import customtkinter as ctk
from tkinter import *
import pymysql as pq

class DataClass():
    def __init__(self, main, user_id=None):
        self.main = main
        self.cursor = self.main.cur
        self.user_id = user_id # Initialize user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def is_first_time_user(self, user_id=None):
        if self.user_id is None:
            raise ValueError("User ID not set. Call set_user_id() first.")
        
        query = "SELECT event_id FROM event WHERE user_id = %s"
        self.cursor.execute(query, (self.user_id,))
        event_id_tuple = self.cursor.fetchone()
        if event_id_tuple == None:
            return True
        else:
            event_id = event_id_tuple[0]
            if event_id != None:
                return False
            else:
                return True

    def get_user_id(self):
        return self.user_id

    def check_existing_user_events(self, user_id=None):
        # self.set_user_id(user_id)  # Ensure user_id is set
        query = "SELECT * FROM event WHERE user_id = %s"
        self.cursor.execute(query, (self.user_id,))
        event_details = self.cursor.fetchall()
        user_event_details = {event[0]: event for event in event_details}
        
        if user_event_details:
            event_names = [event[1] for event in user_event_details.values()]
            latest_event_id = max(user_event_details.keys())
            latest_event = user_event_details[latest_event_id]
            
            self.main.update_screens(
                event_id=latest_event_id,
                event_name=event_names,
                event_category=latest_event[2],
                address=latest_event[3],
                start_date=latest_event[4],
                end_date=latest_event[5],
                start_time=latest_event[6],
                end_time=latest_event[7],
                # planner_email=self.planner_email
            )
        return user_event_details

    def insert_data(self, 
                    event_name, 
                    event_category, 
                    address, 
                    start_date, end_date, 
                    start_time, end_time, 
                    planner_email,
                    first_name,
                    last_name,
                    city,
                    capacity,
                    language,
                    mode
                    ):
        if self.user_id is None:
            raise ValueError("user_id is not set. Call set_user_id() before inserting data.")

        self.planner_email = planner_email

        sql = "INSERT INTO event (event_name, event_category, address, start_date, end_date, end_time, start_time, user_id, language, location, planner_email, format, capacity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (event_name, event_category, address, start_date, end_date, end_time, start_time, self.user_id, language, city, planner_email, mode, capacity))
        self.main.connection.commit()

        self.cursor.execute("SELECT * FROM event WHERE user_id = %s", (self.user_id,))
        events = self.cursor.fetchall()
        column_names = [desc[0] for desc in self.cursor.description]
        self.event_details = {event[0]: dict(zip(column_names, event)) for event in events}

        self.update_views()

    def update_views(self):
        if self.event_details:
            event_names = [event['event_name'] for event in self.event_details.values()]
            latest_event_id = max(self.event_details.keys())
            latest_event = self.event_details[latest_event_id]
            
            self.main.update_screens(
                event_id=latest_event_id,
                event_name=event_names,
                event_category=latest_event['event_category'],
                address=latest_event['address'],
                start_date=latest_event['start_date'],
                end_date=latest_event['end_date'],
                start_time=latest_event['start_time'],
                end_time=latest_event['end_time'],
                planner_email=self.planner_email
            )
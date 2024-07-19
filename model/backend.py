import customtkinter as ctk
from tkinter import *
import pymysql as pq

class DataClass():
    def __init__(self, main):
        super().__init__()

        self.main = main

        self.main.connect_to_database
        self.cursor = self.main.cur
    
    def insert_data(self, event_name=None, event_category=None, address=None, start_date=None, end_date=None, start_time=None, end_time=None, planner_email=None):
        self.event_name = event_name
        self.event_category = event_category
        self.address = address
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.planner_email = planner_email

        self.cursor.execute("use demo")
        self.cursor.execute("select user_id from user where email=%s",self.planner_email)
        user_id=self.cursor.fetchone()
        print(user_id)

        sql="INSERT INTO event (event_name, event_category,address ,start_date, end_date, start_time, end_time) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,(self.event_name, self.event_category, self.address, self.start_date, self.end_date, self.start_time, self.end_time))
        self.main.connection.commit()
        # Fetch all events
        self.cursor.execute("SELECT * FROM event")
        events = self.cursor.fetchall()
        # print(events)
        # print(self.cursor.description)
        # Get column names
        column_names = [desc[0] for desc in self.cursor.description]
        print(column_names,"\n")

        # Store event details in a dictionary
        self.event_details = {}
        # print(f"Event details : {self.event_details}\n")
        for event in events:
            event_id = event[0]  # Assuming event_id is the first column
            self.event_details[event_id] = event # dict(zip(column_names, event))...   TRY THIS
        print(f"Event details : {self.event_details}\n")
        print(f"event_details : {self.event_details[101]}")

        self.main.connection.close()

        # Call the update_views method to refresh the GUI
        self.update_views()

    def update_views(self):
        for event_id, event_data in self.event_details.items():
                self.event_details[event_id] = event_data[1]
                print(f"event_id = {event_id}\nevent_name : {event_data[1]}")
                self.main.update_screen([event_data[1]]) # TODO WORKING ON HOW TO GIVE COMMANDS TO THESE BUTTONS..
        # self.main.update_screens(self.event_name, self.event_category, self.address, self.start_date, self.end_date, self.start_time, self.end_time)
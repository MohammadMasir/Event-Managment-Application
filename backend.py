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
        self.cursor.execute("select * from event;")
        outcome=self.cursor.fetchall()#[0]
        self.main.connection.close()

    def update_views(self):
        self.main.update_screens(self.event_name, self.event_category, self.address, self.start_date, self.end_date, self.start_time, self.end_time)
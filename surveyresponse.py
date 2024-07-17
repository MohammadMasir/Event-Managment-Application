import customtkinter as ctk 
from PIL import Image
import tkinter as tk
from commonpages import Page

class SurveyResponsePage():
    def __init__(self, main_app, event_name=None):
        super().__init__()
        self.main = main_app
        self.parent = self.main.survey_tab

        self.event_name = event_name

    def set_screen(self):
        self.main.notebook.set("Survey and Feedback")
        for widget in self.parent.winfo_children():
            widget.pack_forget()

    def feedback_surveys_screen(self):
        for widget in self.parent.winfo_children():
            widget.pack_forget()
        self.survey_frame = ctk.CTkFrame(self.parent)
        self.survey_frame.pack(fill="both", expand=True)
        self.surveypage = Page(self.main, self.survey_frame, self.event_name, "Feedback Surveys")
        self.surveypage.title_frame(False)
        self.surveypage.content_frame()

    def responses_screen(self):
        self.set_screen()
        self.responses_frame = ctk.CTkFrame(self.parent)
        self.responses_frame.pack(fill="both", expand=True)
        self.responsespage = Page(self.main, self.responses_frame, self.event_name, "Responses")
        self.responsespage.title_frame(False)
        self.responsespage.content_frame()
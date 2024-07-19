import customtkinter as ctk 
from PIL import Image
import tkinter as tk
from view.commonpages import Page

class SurveyResponsePage():
    def __init__(self, main_app, event_name=None):
        super().__init__()
        self.main = main_app
        self.parent = self.main.survey_tab

        self.event_name = ""

    def set_screen(self):
        self.main.notebook.set("Survey and Feedback")
        for widget in self.parent.winfo_children():
            widget.pack_forget()

    def feedback_surveys_screen(self):
        for widget in self.parent.winfo_children():
            widget.pack_forget()
        self.survey_frame = ctk.CTkFrame(self.parent)
        self.survey_frame.pack(fill="both", expand=True)
        self.surveypage = Page(main_app=self.main, parent=self.survey_frame, heading="Feedback Surveys")
        self.surveypage.title_frame(False)
        self.surveypage.content_frame()

    def responses_screen(self):
        self.set_screen()
        self.responses_frame = ctk.CTkFrame(self.parent)
        self.responses_frame.pack(fill="both", expand=True)
        self.responsespage = Page(main_app=self.main, parent=self.responses_frame, heading="Responses")
        self.responsespage.title_frame(False)
        self.responsespage.content_frame()
import customtkinter as ctk 
from PIL import Image
import tkinter as tk
from view.commonpages import Page

class SurveyResponsePage():
    def __init__(self, main_app, parent,event_name,event_category=None, address=None, start_date=None, end_date=None, start_time=None, end_time=None, planner_email=None, city=None, mode=None, capacity=None):
        super().__init__()
        self.main = main_app
        self.parent = parent
        self.event_name = event_name
        self.count = 0

    def set_screen(self):
        self.main.notebook.set("Survey & Feedback")
        for widget in self.parent.winfo_children():
            widget.pack_forget()
#------------------------------------------------------------------------------------------------------------------
    def feedback_surveys_screen(self):
        self.count += 1
        if self.count <= 1:
            for widget in self.parent.winfo_children():
                widget.pack_forget()
        else:
            self.set_screen()

        self.survey_frame = ctk.CTkFrame(self.parent)
        self.survey_frame.pack(fill="both", expand=True)
        self.surveypage = Page(main_app=self.main, parent=self.survey_frame, event_name=self.event_name, heading="Feedback Surveys")
        self.surveypage.title_frame(False)
        self.surveypage.content_frame()

        self.surveys_label = ctk.CTkLabel(self.surveypage.scrollable_frame,text = "Surveys",text_color = "#000000",font = ("Segoe UI",21,"bold"))
        self.surveys_label.pack(anchor = "nw",padx = 15,pady = (10,0))

        self.survey_content_frame = ctk.CTkFrame(self.surveypage.scrollable_frame,fg_color = "#ffffff")
        self.survey_content_frame.pack(fill = "both",expand = True, padx=(10,90), pady=20)

        self.top_frame = ctk.CTkFrame(self.survey_content_frame,fg_color = "#ffffff",border_width = 1,border_color = "lightgray",height = 55)
        self.top_frame.pack(anchor = "nw",padx = 15,pady = (5,1),fill = "x")

        self.bottom_frame = ctk.CTkFrame(self.survey_content_frame,fg_color = "#ffffff",border_width = 1,border_color = "lightgray",height = 55)
        self.bottom_frame.pack(anchor = "nw",padx = 15,pady = (0,60),fill = "x")

        self.name_label = ctk.CTkLabel(self.top_frame,text = "Name",text_color = "#000000",font = ("Arial",15,"normal"))
        self.name_label.place(x = 5,y = 5)

        self.audience_label = ctk.CTkLabel(self.top_frame,text = "Audience",text_color = "#000000",font = ("Arial",15,"normal"))
        self.audience_label.place(x = 220,y = 5)

        self.availability_label = ctk.CTkLabel(self.top_frame,text = "Availability",text_color = "#000000",font = ("Arial",15,"normal"))
        self.availability_label.place(x = 440,y = 5)

        self.active_label = ctk.CTkLabel(self.top_frame,text = "Active",text_color = "#000000",font = ("Arial",15,"normal"))
        self.active_label.place(x = 570,y = 5)

        self.up_down_image = ctk.CTkImage(dark_image = Image.open(r"pics\elevator.png"),size = (25,25))
        self.up_down_image_button = ctk.CTkButton(self.top_frame,image = self.up_down_image,text = "",width = 27,fg_color = "#ffffff",hover_color = "lightgray",command = self.up_down_command)
        self.up_down_image_button.place(x = 720,y = 5)

        name_variable = tk.StringVar()
        name_variable.set("General Event Feedback")
        self.name_value = ctk.CTkLabel(self.bottom_frame,textvariable = name_variable,text_color = "#43B2E4",font = ("Arial",15,"normal"))
        self.name_value.place(x = 5,y = 5)
        
        audience_variable = tk.StringVar()
        audience_variable.set("All Event Registrants")
        self.audience_value = ctk.CTkLabel(self.bottom_frame,textvariable = audience_variable,text_color = "#000000",font = ctk.CTkFont("Arial",15,"normal"))
        self.audience_value.place(x = 220,y = 5)
        
        availability_variable = tk.StringVar()
        availability_variable.set("Always")
        self.availability_label = ctk.CTkLabel(self.bottom_frame,textvariable = availability_variable,text_color = "#000000",font = ("Arial",15,"normal"))
        self.availability_label.place(x = 440,y = 5)
        
        yes_variable = tk.StringVar()
        yes_variable.set("Yes")
        self.active_value = ctk.CTkLabel(self.bottom_frame,textvariable = yes_variable,text_color = "#000000",font = ("Arial",15,"normal"))
        self.active_value.place(x = 570,y = 5)

        self.survey_configuration_label = ctk.CTkLabel(self.surveypage.scrollable_frame,text = "Survey Configuration",text_color = "#000000",font = ("Segoe UI",21,"bold"))
        self.survey_configuration_label.pack(anchor = "nw",padx = 15,pady = (10,0))

        self.open_survey_button = ctk.CTkButton(self.surveypage.scrollable_frame,text = "Open Survey Designer",text_color = "#ffffff",fg_color = "#43B2E4",corner_radius = 7,hover_color = "blue",command = self.survey_designer_command)
        self.open_survey_button.pack(anchor = "nw",padx = 15,pady = 10)

        self.test_survey_button =  ctk.CTkButton(self.surveypage.scrollable_frame,text = "Test Survey",text_color = "#43B2E4",fg_color = "#ffffff",border_width = 1,border_color = "#43B2E4",corner_radius = 7,hover_color = "blue",command = self.test_survey_command)
        self.test_survey_button.pack(anchor = "nw",padx = 15,pady = 10)
#------------------------------------------------------------------------------------------------------------------
    def responses_screen(self):
        self.set_screen()
        self.responses_frame = ctk.CTkFrame(self.parent)
        self.responses_frame.pack(fill="both", expand=True)
        self.responsespage = Page(main_app=self.main, parent=self.responses_frame, event_name=self.event_name, heading="Responses")
        self.responsespage.title_frame(False)
        self.responsespage.content_frame()

        self.response_search = ctk.CTkEntry(self.responsespage.scrollable_frame,height = 40,placeholder_text = "Filter by name or code",placeholder_text_color = "#000000",width = 250,fg_color = "#ffffff",corner_radius = 5)
        self.response_search.pack(anchor = "ne",padx = (0,25),pady = 20)

        self.filter_image = ctk.CTkImage(dark_image = Image.open(r"pics\loupe.png"),size = (25,25))
        self.filter_image_button = ctk.CTkButton(self.response_search,image = self.filter_image,text = "",width = 35,fg_color = "#ffffff",hover_color = "lightgray",command = self.filter_command)
        self.filter_image_button.grid(row = 0,column = 0,sticky = "ne",padx = 10,pady = 5)

        self.response_content_frame = ctk.CTkFrame(self.responsespage.scrollable_frame,fg_color = "#ffffff")
        self.response_content_frame.pack(fill = "both",expand = True, padx=(10,90), pady=20)

        self.top_frame = ctk.CTkFrame(self.response_content_frame,fg_color = "#ffffff",border_width = 1,border_color = "lightgray",height = 55)
        self.top_frame.pack(anchor = "nw",padx = 15,pady = (10,1),fill = "x")

        self.bottom_frame = ctk.CTkFrame(self.response_content_frame,fg_color = "#ffffff",border_width = 1,border_color = "lightgray",height = 55)
        self.bottom_frame.pack(anchor = "nw",padx = 15,pady = (0,60),fill = "x")

        self.response_name_label = ctk.CTkLabel(self.top_frame,text = "Name",text_color = "#000000",font = ("Arial",15,"normal"))
        self.response_name_label.place(x = 5,y = 5)

        self.response_code_label = ctk.CTkLabel(self.top_frame,text = "Response Code",text_color = "#000000",font = ("Arial",15,"normal"))
        self.response_code_label.place(x = 220,y = 5)

        self.last_modified_label = ctk.CTkLabel(self.top_frame,text = "Last Modified",text_color = "#000000",font = ("Arial",15,"normal"))
        self.last_modified_label.place(x = 430,y = 5)

        self.duration_label = ctk.CTkLabel(self.top_frame,text = "Duration of Response",text_color = "#000000",font = ("Arial",15,"normal"))
        self.duration_label.place(x = 640,y = 5)
        
        response_variable = tk.StringVar()
        response_variable.set("You don't have any responses yet.")
        self.response_data = ctk.CTkLabel(self.bottom_frame,textvariable = response_variable,text_color = "#000000",height = 20,font = ctk.CTkFont("Arial",20,"bold"))
        self.response_data.place(x = 230,y = 10)

#-------------------------------------------------------------------------------------------------------------------
    def up_down_command(self):
        pass

    def survey_designer_command(self):
        pass

    def test_survey_command(self):
        pass

    def filter_command(self):
        pass



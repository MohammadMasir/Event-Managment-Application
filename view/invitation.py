import customtkinter as ctk 
from PIL import Image
import tkinter as tk
from view.commonpages import Page

class InviteeAttendeePage():
    def __init__(self, main_app, parent, event_name=None):
        super().__init__()
        self.main = main_app
        self.parent = parent
        self.event_name = event_name
        self.count = 0

    def set_screen(self):
        self.main.notebook.set("Invitation & Attendees")
        for widget in self.parent.winfo_children():
            widget.pack_forget()

    def invitation_list_screen(self):
        self.count += 1
        if self.count <= 1:
            for widget in self.parent.winfo_children():
                widget.pack_forget()
        else:
            self.set_screen()

        self.inv_list_frame = ctk.CTkFrame(self.parent)
        self.inv_list_frame.pack(fill="both", expand=True)
        self.invitationpage = Page(main_app=self.main, parent=self.inv_list_frame, event_name=self.event_name, heading="Invitation List")
        self.invitationpage.title_frame(False)
        self.invitationpage.content_frame()

    def event_emails(self):
        self.set_screen()
        self.emails_list_frame = ctk.CTkFrame(self.parent)
        self.emails_list_frame.pack(fill="both", expand=True)
        self.emailspage = Page(main_app=self.main, parent=self.emails_list_frame, event_name=self.event_name, heading="Event Emails")
        self.emailspage.title_frame(False)
        self.emailspage.content_frame()
#--------------------------------------------------------------------------------------------------------------  
    def planner_alerts(self):
        self.set_screen()
        self.plannerframe = ctk.CTkFrame(self.parent)
        self.plannerframe.pack(fill="both", expand=True)
        self.plannerpage = Page(main_app=self.main, parent=self.plannerframe, event_name=self.event_name, heading="Planner Alerts")
        self.plannerpage.title_frame(False)
        self.plannerpage.content_frame()

        self.planner_content_frame = ctk.CTkFrame(self.plannerpage.scrollable_frame,fg_color = "#ffffff")
        self.planner_content_frame.pack(fill = "both",expand = True, padx=(10,90), pady=20)

        self.top_frame = ctk.CTkFrame(self.planner_content_frame,fg_color = "#ffffff",border_width = 1,border_color = "lightgray",height = 55)
        self.top_frame.pack(anchor = "nw",padx = 15,pady = (10,1),fill = "x")

        self.bottom_frame = ctk.CTkFrame(self.planner_content_frame,fg_color = "#ffffff",border_width = 1,border_color = "lightgray",height = 55)
        self.bottom_frame.pack(anchor = "nw",padx = 15,pady = (0,30),fill = "x")
        
        self.name_label = ctk.CTkLabel(self.top_frame,text = "Name",text_color = "#000000",font = ("Arial",15,"normal"))
        self.name_label.place(x = 5,y = 5)

        self.category_label = ctk.CTkLabel(self.top_frame,text = "Category",text_color = "#000000",font = ("Arial",15,"normal"))
        self.category_label.place(x = 220,y = 5)

        self.type_label = ctk.CTkLabel(self.top_frame,text = "Type",text_color = "#000000",font = ("Arial",15,"normal"))
        self.type_label.place(x = 380,y = 5)

        self.recipients_label = ctk.CTkLabel(self.top_frame,text = "Recipients",text_color = "#000000",font = ("Arial",15,"normal"))
        self.recipients_label.place(x = 490,y = 5)

        self.active_label = ctk.CTkLabel(self.top_frame,text = "Active",text_color = "#000000",font = ("Arial",15,"normal"))
        self.active_label.place(x = 660,y = 5)

        self.up_down_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\elevator.png"),size = (25,25))
        self.up_down_image_button = ctk.CTkButton(self.top_frame,image = self.up_down_image,text = "",width = 27,fg_color = "#ffffff",hover_color = "lightgray",command = self.up_down_command)
        self.up_down_image_button.place(x = 770,y = 5)
        
        alert_variable = tk.StringVar()
        alert_variable.set("You do not have any email/SMS alerts.")
        self.alert_msg = ctk.CTkLabel(self.bottom_frame,textvariable = alert_variable,text_color = "#000000",height = 20,font = ctk.CTkFont("Arial",20,"bold"))
        self.alert_msg.place(x = 230,y = 10)

#------------------------------------------------------------------------------------------------------------------
    def attendee_list_screen(self):
        self.set_screen()
        self.attendee_list_frame = ctk.CTkFrame(self.parent)
        self.attendee_list_frame.pack(fill="both", expand=True)
        self.attendeepage = Page(main_app=self.main, parent=self.attendee_list_frame, event_name=self.event_name, heading="Attendee List")
        self.attendeepage.title_frame(False)
        self.attendeepage.content_frame() 
        
        self.top_frame1 = ctk.CTkFrame(self.attendeepage.scrollable_frame,fg_color = "#F0F0F0",height = 60)
        self.top_frame1.pack(anchor = "nw",padx = 15,pady = 10,fill = "x")

        self.view_combo = ctk.CTkOptionMenu(self.top_frame1,fg_color = "#ffffff",corner_radius = 5,button_color = "lightgray",button_hover_color = "#F0F0F0",dropdown_fg_color = "#F0F0F0",dropdown_hover_color = "lightgray",text_color = "#000000",values = ["","","","",""])
        self.view_combo.pack(side = "left")

        self.search_bar = ctk.CTkEntry(self.top_frame1,height = 40,placeholder_text = "send2atm",placeholder_text_color = "#000000",width = 250,fg_color = "#ffffff",corner_radius = 5)
        self.search_bar.pack(side = "right",padx = (0,25))

        self.filter_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\loupe.png"),size = (25,25))
        self.filter_image_button = ctk.CTkButton(self.search_bar,image = self.filter_image,text = "",width = 35,fg_color = "#ffffff",hover_color = "lightgray",command = self.filter_command)
        self.filter_image_button.grid(row = 0,column = 0,sticky = "ne",padx = 10,pady = 5)

        self.attendee_content_frame = ctk.CTkFrame(self.attendeepage.scrollable_frame,fg_color = "#ffffff")
        self.attendee_content_frame.pack(fill = "both",expand = True, padx=(10,90), pady=20)

        self.top_frame = ctk.CTkFrame(self.attendee_content_frame,fg_color = "#ffffff",border_width = 1,border_color = "lightgray",height = 55)
        self.top_frame.pack(anchor = "nw",padx = 15,pady = (10,1),fill = "x")

        self.bottom_frame = ctk.CTkFrame(self.attendee_content_frame,fg_color = "#ffffff",border_width = 1,border_color = "lightgray",height = 55)
        self.bottom_frame.pack(anchor = "nw",padx = 15,pady = (0,60),fill = "x")

        self.name_label = ctk.CTkLabel(self.top_frame,text = "Name",text_color = "#000000",font = ("Arial",15,"normal"))
        self.name_label.place(x = 5,y = 5)

        self.title_label = ctk.CTkLabel(self.top_frame,text = "Title",text_color = "#000000",font = ("Arial",15,"normal"))
        self.title_label.place(x = 220,y = 5)

        self.company_label = ctk.CTkLabel(self.top_frame,text = "Company",text_color = "#000000",font = ("Arial",15,"normal"))
        self.company_label.place(x = 380,y = 5)

        self.email_label = ctk.CTkLabel(self.top_frame,text = "Email",text_color = "#000000",font = ("Arial",15,"normal"))
        self.email_label.place(x = 490,y = 5)

        self.status_label = ctk.CTkLabel(self.top_frame,text = "Status",text_color = "#000000",font = ("Arial",15,"normal"))
        self.status_label.place(x = 660,y = 5)

        self.up_down_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\elevator.png"),size = (25,25))
        self.up_down_image_button = ctk.CTkButton(self.top_frame,image = self.up_down_image,text = "",width = 27,fg_color = "#ffffff",hover_color = "lightgray",command = self.up_down_command)
        self.up_down_image_button.place(x = 770,y = 5)

        invitee_variable = tk.StringVar()
        invitee_variable.set("No invitees match your criteria.")
        self.invitee_msg = ctk.CTkLabel(self.bottom_frame,textvariable = invitee_variable,text_color = "#000000",height = 20,font = ctk.CTkFont("Arial",20,"bold"))
        self.invitee_msg.place(x = 230,y = 10)
        
        self.lower_frame = ctk.CTkFrame(self.attendee_content_frame,fg_color = "#ffffff",height = 60)
        self.lower_frame.pack(anchor = "nw",padx = 15,pady = 0)

        self.results_per_page_label = ctk.CTkLabel(self.lower_frame,text = "Results Per Page",text_color = "#000000",font =  ctk.CTkFont("Arial",20,"normal"))
        self.results_per_page_label.grid(row = 0,column = 0,sticky = "w",pady = 0)

        self.result_dropdown = ctk.CTkOptionMenu(self.lower_frame,fg_color = "#F0F0F0",corner_radius = 5,width = 60,button_color = "lightgray",button_hover_color = "#F0F0F0",dropdown_fg_color = "#F0F0F0",dropdown_hover_color = "lightgray",text_color = "#000000",values = ["24","24","26","27","28"])
        self.result_dropdown.grid(row = 0,column = 1,padx = 10,pady = 0)

#------------------------------------------------------------------------------------------------------------------
    def certificates_screen(self):
        self.set_screen()
        self.certificates_frame = ctk.CTkFrame(self.parent)
        self.certificates_frame.pack(fill="both", expand=True)
        self.certificatespage = Page(main_app=self.main, parent=self.certificates_frame,event_name=self.event_name, heading="Certificates")
        self.certificatespage.title_frame(False)
        self.certificatespage.content_frame()

#-------------------------------------------------------------------------------------------------------------------

    def up_down_command(self):
        pass

    def filter_command(self):
        pass


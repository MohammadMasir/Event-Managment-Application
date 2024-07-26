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

        self.invitation_content_frame = ctk.CTkFrame(self.invitationpage.scrollable_frame,fg_color = "#ffffff")
        self.invitation_content_frame.pack(fill = "both",expand = True, padx=(10,90), pady=20)

        self.top_frame = ctk.CTkFrame(self.invitation_content_frame,fg_color = "#ffffff",border_width = 1,border_color = "lightgray",height = 55)
        self.top_frame.pack(anchor = "nw",padx = 15,pady = (10,0),fill = "x")

        self.bottom_frame = ctk.CTkFrame(self.invitation_content_frame,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
        self.bottom_frame.pack(anchor = "nw",padx = 15,pady = (0,5),fill = "both")

        self.name_label = ctk.CTkLabel(self.top_frame,text = "Name",text_color = "#000000",font = ("Arial",15,"normal"))
        self.name_label.place(x = 5,y = 5)

        self.list_members_label = ctk.CTkLabel(self.top_frame,text = "List Members",text_color = "#000000",font = ("Arial",15,"normal"))
        self.list_members_label.place(x = 220,y = 5)

        self.emails_label = ctk.CTkLabel(self.top_frame,text = "Emails",text_color = "#000000",font = ("Arial",15,"normal"))
        self.emails_label.place(x = 440,y = 5)

        self.up_down_image = ctk.CTkImage(dark_image = Image.open(r"pics\elevator.png"),size = (25,25))
        self.up_down_image_button = ctk.CTkButton(self.top_frame,image = self.up_down_image,text = "",width = 27,fg_color = "#ffffff",hover_color = "lightgray",command = self.up_down_command)
        self.up_down_image_button.place(x = 700,y = 5)

        self.internal_frame1 = ctk.CTkFrame(self.bottom_frame,fg_color = "#ffffff",height = 40,border_width = 1,border_color = "lightgray")
        self.internal_frame1.pack(fill = "x",padx = 5,pady = 1)
        
        internal_name_variable = tk.StringVar()
        internal_name_variable.set("Invitation list")
        self.internal_frame1_name = ctk.CTkLabel(self.internal_frame1,textvariable = internal_name_variable,text_color = "#43B2E4",font = ("Arial",17,"bold"))
        self.internal_frame1_name.place(x = 5,y = 5)

        self.mail_image = ctk.CTkImage(dark_image = Image.open(r"pics\mail.png"),size = (25,25))
        self.mail_image_button = ctk.CTkButton(self.internal_frame1,image = self.mail_image,text = "",width = 25,fg_color = "#ffffff",hover_color = "lightgray",command = self.mail_command)
        self.mail_image_button.place(x = 210,y = 5)
        
        members_variable = tk.StringVar()
        members_variable.set("2")
        self.members_value = ctk.CTkLabel(self.internal_frame1,textvariable = members_variable,text_color = "#000000",font = ("Arial",17,"bold"))
        self.members_value.place(x = 255,y = 5)
        
        email_value_variable = tk.StringVar()
        email_value_variable.set("21")
        self.email_value = ctk.CTkLabel(self.internal_frame1,textvariable = email_value_variable,text_color = "#000000",font = ("Arial",17,"bold"))
        self.email_value.place(x = 457,y = 5)

        self.internal_frame2 = ctk.CTkFrame(self.bottom_frame,fg_color = "#ffffff",height = 40,border_width = 1,border_color = "lightgray")
        self.internal_frame2.pack(fill = "x",padx = 5,pady = 0)

        self.internal_frame3 = ctk.CTkFrame(self.bottom_frame,fg_color = "#ffffff",height = 40,border_width = 1,border_color = "lightgray")
        self.internal_frame3.pack(fill = "x",padx = 5,pady = 0)

        self.internal_frame4 = ctk.CTkFrame(self.bottom_frame,fg_color = "#ffffff",height = 40,border_width = 1,border_color = "lightgray")
        self.internal_frame4.pack(fill = "x",padx = 5,pady = 0)

        self.internal_frame5 = ctk.CTkFrame(self.bottom_frame,fg_color = "#ffffff",height = 40,border_width = 1,border_color = "lightgray")
        self.internal_frame5.pack(fill = "x",padx = 5,pady = (1,5))

#-------------------------------------------------------------------------------------------------------------
    def event_emails(self):
        self.set_screen()
        self.emails_list_frame = ctk.CTkFrame(self.parent)
        self.emails_list_frame.pack(fill="both", expand=True)
        self.emailspage = Page(main_app=self.main, parent=self.emails_list_frame, event_name=self.event_name, heading="Event Emails")
        self.emailspage.title_frame(False)
        self.emailspage.content_frame()

        self.email_content_frame = ctk.CTkFrame(self.emailspage.scrollable_frame,fg_color = "#ffffff")
        self.email_content_frame.pack(fill = "both",expand = True,padx = (10,20),pady = 20)

        self.pre_event_label = ctk.CTkLabel(self.email_content_frame,text = "Pre-Event Emails",text_color = "#000000",font = ("Segoe UI",21,"bold"))
        self.pre_event_label.place(x = 15,y = 30)

        self.invitation_label = ctk.CTkLabel(self.email_content_frame,text = "Invitation",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.invitation_label.place(x = 30,y = 75)

        self.invitation_send1 = ctk.CTkLabel(self.email_content_frame,text = "Send:Manually to Undecided Invitees",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.invitation_send1.place(x = 30,y = 100)

        self.active_status1 = ctk.CTkLabel(self.email_content_frame,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.active_status1.place(x = 500,y = 85)

        self.switch1 = ctk.CTkSwitch(self.email_content_frame,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.switch1.place(x = 600,y = 75)

        self.invitation_reminder_label = ctk.CTkLabel(self.email_content_frame,text = "Invitation Reminder",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.invitation_reminder_label.place(x = 30,y = 150)

        self.invitation_send2 = ctk.CTkLabel(self.email_content_frame,text = "Send:Manually to Undecided Invitees",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.invitation_send2.place(x = 30,y = 180)

        self.active_status2 = ctk.CTkLabel(self.email_content_frame,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.active_status2.place(x = 500,y = 150)

        self.switch2 = ctk.CTkSwitch(self.email_content_frame,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.switch2.place(x = 600,y = 140)

        self.John_label = ctk.CTkLabel(self.email_content_frame,text = "John",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.John_label.place(x = 30,y = 225)

        self.invitation_send3 = ctk.CTkLabel(self.email_content_frame,text = "Send:Manually to Undecided Invitees",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.invitation_send3.place(x = 30,y = 260)

        self.active_status3 = ctk.CTkLabel(self.email_content_frame,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.active_status3.place(x = 500,y = 225)

        self.switch3 = ctk.CTkSwitch(self.email_content_frame,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.switch3.place(x = 600,y = 215)

        self.save_the_date_label = ctk.CTkLabel(self.email_content_frame,text = "Save the Date",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.save_the_date_label.place(x = 30,y = 300)

        self.invitation_send4 = ctk.CTkLabel(self.email_content_frame,text = "Send:Manually to Undecided Invitees",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.invitation_send4.place(x = 30,y = 335)

        self.active_status4 = ctk.CTkLabel(self.email_content_frame,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.active_status4.place(x = 500,y = 300)

        self.switch4 = ctk.CTkSwitch(self.email_content_frame,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.switch4.place(x = 600,y = 290)

        self.waitlist_notification_label = ctk.CTkLabel(self.email_content_frame,text = "Waitlist Notification",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.waitlist_notification_label.place(x = 30,y = 375)

        self.invitation_send5 = ctk.CTkLabel(self.email_content_frame,text = "Send:Manually to Waitlisted Invitees",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.invitation_send5.place(x = 500,y = 410)

        self.active_status5 = ctk.CTkLabel(self.email_content_frame,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.active_status5.place(x = 500,y = 375)

        self.switch5 = ctk.CTkSwitch(self.email_content_frame,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.switch5.place(x = 600,y = 365)

#-------------------------------------------------------------------------------------------------------------
        self.post_content_frame = ctk.CTkFrame(self.emailspage.scrollable_frame,fg_color = "#ffffff")
        self.post_content_frame.pack(fill = "both",expand = True,padx = (10,20),pady = 20)

        self.post_registration_label = ctk.CTkLabel(self.post_content_frame,text = "Post-Registration Emails",text_color = "#000000",font = ("Segoe UI",21,"bold"))
        self.post_registration_label.pack(anchor = "nw",padx = 5,pady = 5)

        self.left_frame = ctk.CTkFrame(self.post_content_frame,width = 400,fg_color = "#ffffff")
        self.left_frame.pack(side = "left",padx = 15,pady = 10,fill = "y")

        self.common_button_frame = ctk.CTkFrame(self.post_content_frame,width = 100,fg_color = "#ffffff")
        self.common_button_frame.pack(side = "right",padx = (0,10),pady = 10,fill = "y")

        self.common_active_frame = ctk.CTkFrame(self.post_content_frame,width = 200,fg_color = "#ffffff")
        self.common_active_frame.pack(side = "right",padx = (0,30),pady = 10,fill = "y")

        self.john_label = ctk.CTkLabel(self.left_frame,text = "John",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.john_label.pack(anchor = "nw",padx = 0,pady = 0)

        self.send_manual = ctk.CTkLabel(self.left_frame,text = "Send:Manually to All Invitees",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.send_manual.pack(anchor = "nw",padx = 0,pady = (1,5))

        self.approval_label = ctk.CTkLabel(self.left_frame,text = "Approval Pending Notification",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.approval_label.pack(anchor = "nw",padx = 0,pady = 10)

        self.automatic_label = ctk.CTkLabel(self.left_frame,text = "Send:Automatically to Registrants Pending Approval",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.automatic_label.pack(anchor = "nw",padx = 0,pady = (1,5))

        self.event_reminder_label = ctk.CTkLabel(self.left_frame,text = "Event Reminder",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.event_reminder_label.pack(anchor = "nw",padx = 0,pady = 10)

        self.accepted_label = ctk.CTkLabel(self.left_frame,text = "Send:Manually to Accepted Registrants",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.accepted_label.pack(anchor = "nw",padx = 0,pady = (1,5))

        self.modification_label = ctk.CTkLabel(self.left_frame,text = "Modification Confirmation",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.modification_label.pack(anchor = "nw",padx = 0,pady = 10)

        self.automatic_accepted_label = ctk.CTkLabel(self.left_frame,text = "Send:Automatically to Accepted Registrants",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.automatic_accepted_label.pack(anchor = "nw",padx = 0,pady = (1,5))

        self.registration_confirmation_label = ctk.CTkLabel(self.left_frame,text = "Registration Confirmation",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.registration_confirmation_label.pack(anchor = "nw",padx = 0,pady = 10)

        self.accepted_registrants = ctk.CTkLabel(self.left_frame,text = "Send:Automatically to Accepted Registrants",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.accepted_registrants.pack(anchor = "nw",padx = 0,pady = (1,5)) 

        self.guest_event_label = ctk.CTkLabel(self.left_frame,text = "Guest Event Reminder",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.guest_event_label.pack(anchor = "nw",padx = 0,pady = 10)

        self.accepted_guest =  ctk.CTkLabel(self.left_frame,text = "Send:Manually to Accepted Guest",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.accepted_guest.pack(anchor = "nw",padx = 0,pady = (1,5))

        self.guest_registration_label = ctk.CTkLabel(self.left_frame,text = "Guest Registration Notification",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.guest_registration_label.pack(anchor = "nw",padx = 0,pady = 10)

        self.automatic_guest = ctk.CTkLabel(self.left_frame,text = "Send:Automatically to Accepted Guest",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.automatic_guest.pack(anchor = "nw",padx = 0,pady = (1,5))

        self.administrator_confirmation_label = ctk.CTkLabel(self.left_frame,text = "Administrator Registration Confirmation ",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.administrator_confirmation_label.pack(anchor = "nw",padx = 0,pady = 10)

        self.automatic_administrator = ctk.CTkLabel(self.left_frame,text = "Send:Automatically to Administrator",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.automatic_administrator.pack(anchor = "nw",padx = 0,pady = (1,5))

        self.post_active1 = ctk.CTkLabel(self.common_active_frame,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.post_active1.pack(anchor = "n",pady = (0))

        self.post_active2 = ctk.CTkLabel(self.common_active_frame,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.post_active2.pack(anchor = "n",pady = (55,0))

        self.post_active3 = ctk.CTkLabel(self.common_active_frame,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.post_active3.pack(anchor = "n",pady = (55,0))

        self.post_active4 = ctk.CTkLabel(self.common_active_frame,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.post_active4.pack(anchor = "n",pady = (55,0))

        self.post_active5 = ctk.CTkLabel(self.common_active_frame,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.post_active5.pack(anchor = "n",pady = (55,0))

        self.post_active6 = ctk.CTkLabel(self.common_active_frame,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.post_active6.pack(anchor = "n",pady = (55,0))

        self.post_active7 = ctk.CTkLabel(self.common_active_frame,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.post_active7.pack(anchor = "n",pady = (55,0))

        self.post_active8 = ctk.CTkLabel(self.common_active_frame,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.post_active8.pack(anchor = "n",pady = (55,0))

        self.post_switch1 = ctk.CTkSwitch(self.common_button_frame,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.post_switch1.pack(anchor = "n",pady = (0,3))

        self.post_switch2 = ctk.CTkSwitch(self.common_button_frame,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.post_switch2.pack(anchor = "n",pady = (30,0))

        self.post_switch3 = ctk.CTkSwitch(self.common_button_frame,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.post_switch3.pack(anchor = "n",pady = (30,0))

        self.post_switch4 = ctk.CTkSwitch(self.common_button_frame,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.post_switch4.pack(anchor = "n",pady = (30,0))

        self.post_switch5 = ctk.CTkSwitch(self.common_button_frame,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.post_switch5.pack(anchor = "n",pady = (30,0))

        self.post_switch6 = ctk.CTkSwitch(self.common_button_frame,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.post_switch6.pack(anchor = "n",pady = (35,0))

        self.post_switch7 = ctk.CTkSwitch(self.common_button_frame,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.post_switch7.pack(anchor = "n",pady = (35,0))

        self.post_switch8 = ctk.CTkSwitch(self.common_button_frame,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.post_switch8.pack(anchor = "n",pady = (35,0))
#-------------------------------------------------------------------------------------------------------------

        self.declined_emails_frame = ctk.CTkFrame(self.emailspage.scrollable_frame,fg_color = "#ffffff")
        self.declined_emails_frame.pack(fill = "both",expand = True,padx = (10,20),pady = 20)

        self.declined_email_label = ctk.CTkLabel(self.declined_emails_frame,text = "Declined-Registration Emails",text_color = "#000000",font = ("Segoe UI",21,"bold"))
        self.declined_email_label.pack(anchor = "nw",padx = 5,pady = 5)

        self.left_frame1 = ctk.CTkFrame(self.declined_emails_frame,width = 400,fg_color = "#ffffff")
        self.left_frame1.pack(side = "left",padx = 15,pady = 10,fill = "y")

        self.common_button_frame1 = ctk.CTkFrame(self.declined_emails_frame,width = 100,fg_color = "#ffffff")
        self.common_button_frame1.pack(side = "right",padx = (0,10),pady = 10,fill = "y")

        self.common_active_frame1 = ctk.CTkFrame(self.declined_emails_frame,width = 200,fg_color = "#ffffff")
        self.common_active_frame1.pack(side = "right",padx = (0,30),pady = 10,fill = "y")

        self.approval_notification_label = ctk.CTkLabel(self.left_frame1,text = "Approval Denied Notification",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.approval_notification_label.pack(anchor = "nw",padx = 0,pady = 0)

        self.automatically_denied = ctk.CTkLabel(self.left_frame1,text = "Send:Automatically to Denied Registrants",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.automatically_denied.pack(anchor = "nw",padx = 0,pady = (1,5))

        self.cancellation_form_label = ctk.CTkLabel(self.left_frame1,text = "Cancellation Confirmation",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.cancellation_form_label.pack(anchor = "nw",padx = 0,pady = (10,0))

        self.automatically_cancelled = ctk.CTkLabel(self.left_frame1,text = "Send:Automatically to Cancelled Registrants",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.automatically_cancelled.pack(anchor = "nw",padx = 0,pady = (1,10))

        self.Regret_label = ctk.CTkLabel(self.left_frame1,text = "Regret",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.Regret_label.pack(anchor = "nw",padx = 0,pady = (10,0))

        self.automatically_invitees = ctk.CTkLabel(self.left_frame1,text = "Send:Automatically to Declined Invitees",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.automatically_invitees.pack(anchor = "nw",padx = 0,pady = (1,10))

        self.declined_active1 = ctk.CTkLabel(self.common_active_frame1,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.declined_active1.pack(anchor = "n",pady = (0))

        self.declined_active2 = ctk.CTkLabel(self.common_active_frame1,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.declined_active2.pack(anchor = "n",pady = (55,0))

        self.declined_active3 = ctk.CTkLabel(self.common_active_frame1,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.declined_active3.pack(anchor = "n",pady = (55,0))

        self.declined_switch1 =  ctk.CTkSwitch(self.common_button_frame1,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.declined_switch1.pack(anchor = "n",pady = (0))

        self.declined_switch2 = ctk.CTkSwitch(self.common_button_frame1,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.declined_switch2.pack(anchor = "n",pady = (30,0))

        self.declined_switch3 = ctk.CTkSwitch(self.common_button_frame1,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.declined_switch3.pack(anchor = "n",pady = (30,0))

#-------------------------------------------------------------------------------------------------------------

        self.post_event_emails_frame = ctk.CTkFrame(self.emailspage.scrollable_frame,fg_color = "#ffffff")
        self.post_event_emails_frame.pack(fill = "both",expand = True,padx = (10,20),pady = 20)
        
        self.post_event_email_label = ctk.CTkLabel(self.post_event_emails_frame,text = "Post-Event Emails",text_color = "#000000",font = ("Segoe UI",21,"bold"))
        self.post_event_email_label.pack(anchor = "nw",padx = 5,pady = 5)

        self.left_frame2 = ctk.CTkFrame(self.post_event_emails_frame,width = 400,fg_color = "#ffffff")
        self.left_frame2.pack(side = "left",padx = 15,pady = 10,fill = "y")

        self.common_button_frame2 = ctk.CTkFrame(self.post_event_emails_frame,width = 100,fg_color = "#ffffff")
        self.common_button_frame2.pack(side = "right",padx = (0,10),pady = 10,fill = "y")

        self.common_active_frame2 = ctk.CTkFrame(self.post_event_emails_frame,width = 200,fg_color = "#ffffff")
        self.common_active_frame2.pack(side = "right",padx = (0,30),pady = 10,fill = "y")

        self.event_feedback_label = ctk.CTkLabel(self.left_frame2,text = "Event Feedback",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.event_feedback_label.pack(anchor = "nw",padx = 0,pady = 0)

        self.event_feedback_down_label = ctk.CTkLabel(self.left_frame2,text = "Send:Manually to Attended Registrants",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.event_feedback_down_label.pack(anchor = "nw",padx = 0,pady = (1,5))

        self.event_feedback_reminder_label = ctk.CTkLabel(self.left_frame2,text = "Event Feedback Reminder",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.event_feedback_reminder_label.pack(anchor = "nw",padx = 0,pady = (10,0))

        self.event_feedback_reminder_down = ctk.CTkLabel(self.left_frame2,text = "Send:Manually to Attendees who haven't completed all of their feedback surveys",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.event_feedback_reminder_down.pack(anchor = "nw",padx = 0,pady = (1,10))

        self.guest_event_feedback_label =  ctk.CTkLabel(self.left_frame2,text = "Guest Event Feedback",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.guest_event_feedback_label.pack(anchor = "nw",padx = 0,pady = (10,0))

        self.guest_event_feedback_down = ctk.CTkLabel(self.left_frame2,text = "Send:Manually to Attended Guest",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.guest_event_feedback_down.pack(anchor = "nw",padx = 0,pady = (1,10))

        self.guest_event_feedback_reminder_label = ctk.CTkLabel(self.left_frame2,text = "Guest Event Feedback Reminder",text_color = "#000000",font = ctk.CTkFont("Arial",17,"bold"))
        self.guest_event_feedback_reminder_label.pack(anchor = "nw",padx = 0,pady = (10,0))

        self.guest_event_feedback_reminder_down = ctk.CTkLabel(self.left_frame2,text = "Send:Manually to Guest who haven't completed all of their feedback surveys",text_color = "#000000",font = ctk.CTkFont("Arial",17,"normal"))
        self.guest_event_feedback_reminder_down.pack(anchor = "nw",padx = 0,pady = (1,10))

        self.post_event_active1 = ctk.CTkLabel(self.common_active_frame2,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.post_event_active1.pack(anchor = "n",pady = (0))

        self.post_event_active2 = ctk.CTkLabel(self.common_active_frame2,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.post_event_active2.pack(anchor = "n",pady = (55,0))

        self.post_event_active3 = ctk.CTkLabel(self.common_active_frame2,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.post_event_active3.pack(anchor = "n",pady = (55,0))

        self.post_event_active4 = ctk.CTkLabel(self.common_active_frame2,text = "Active:",text_color = "#000000",font = ctk.CTkFont("Arial",20,"bold"))
        self.post_event_active4.pack(anchor = "n",pady = (55,0))

        self.post_event_switch1 = ctk.CTkSwitch(self.common_button_frame2,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.post_event_switch1.pack(anchor = "n",pady = (0))

        self.post_event_switch2 = ctk.CTkSwitch(self.common_button_frame2,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.post_event_switch2.pack(anchor = "n",pady = (30,0))

        self.post_event_switch3 = ctk.CTkSwitch(self.common_button_frame2,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.post_event_switch3.pack(anchor = "n",pady = (30,0))

        self.post_event_switch4 = ctk.CTkSwitch(self.common_button_frame2,height = 50,width = 50,text = "",corner_radius = 10,fg_color = "#43B2E4",button_color = "#F0F0F0",button_hover_color = "#F0F0F0",onvalue = "on",offvalue = "off")
        self.post_event_switch4.pack(anchor = "n",pady = (30,0))

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

        self.up_down_image = ctk.CTkImage(dark_image = Image.open(r"pics\elevator.png"),size = (25,25))
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

        self.filter_image = ctk.CTkImage(dark_image = Image.open(r"pics\loupe.png"),size = (25,25))
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

        self.up_down_image = ctk.CTkImage(dark_image = Image.open(r"pics\elevator.png"),size = (25,25))
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

    def mail_command(self):
        pass



def show_name(id, name):
    print(f"event_names : {event_names}")
    print(f"event_id : {id}\nevent_name : {name}")
    # print(name[-1])

details = {101 : (101, "TechFest", "Session", "Address1"),
        102 : (102, "TechFest2", "Session2", "Address2"),
        103 : (103, "TechFest3", "Session3", "Address3"),
        104 : (104, "TechFest4", "Session4", "Address4")
        }

event_names = []
for event_id, event_name in details.items():
    # print(event_name[1])
    event_names.append(event_name[1])

show_name(event_id, event_names[-1])

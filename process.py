import os
import json
import platform
import signal
from multiprocessing import Process
from web import check_seats
from multiprocessing import Process, Manager

global all_fields, processes

def load_and_start_processes():
    # Load existing data
    global all_fields, processes
    processes = []
    all_fields = list()
    try:
        if os.path.getsize('save.json') > 0:
            with open('save.json', 'r') as f:
                all_fields = json.load(f)
    except FileNotFoundError:
        pass

    # Start a process for each entry
    for entry in all_fields:
        p = Process(target=check_seats, args=(entry['subject'], entry['course'], entry['section'], entry['seat_type'], entry['sender_email'], entry['password'], entry['recipient_email'], entry['url'], int(entry['time_input'])))
        p.start()
        processes.append(p)
        entry['pid'] = p.pid
    
    with open('save.json', 'w') as f:
        json.dump(list(all_fields), f)

    return all_fields   
      
def start_process(subject, course, section, seat_type, sender_email, password, recipient_email, time_input):
    global all_fields
    url = "https://www.courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept={subject}&course={course}&section={section}".format(subject=subject, course=course, section=section)
    # Create a dictionary for the current entry
    current_entry = {
        'subject': subject,
        'course': course,
        'section': section,
        'url': url,
        'sender_email': sender_email,
        'password': password,
        'seat_type': seat_type,
        'recipient_email': recipient_email,
        'time_input': time_input
    }
        
    # ghuy uzfa jgdy zakz
        
    # Start a new process for the current entry
    p = Process(target=check_seats, args=(subject, course, section, seat_type, sender_email, password, recipient_email, url, int(time_input)))
    p.start()    
    current_entry['pid'] = p.pid
    processes.append(p)
    # Add the current entry to all_fields
    all_fields.append(current_entry)

    # Save data
    with open('save.json', 'w') as f:
        json.dump(list(all_fields), f)
        
    return current_entry

    
def delete_process(subject, course, section, seat_type, sender_email, password, recipient_email, time_input):
    global all_fields
    url = "https://www.courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept={subject}&course={course}&section={section}".format(subject=subject, course=course, section=section)
    selected_entry = {
        'subject': subject,
        'course': course,
        'section': section,
        'url': url,
        'sender_email': sender_email,
        'password': password,
        'seat_type': seat_type,
        'recipient_email': recipient_email,
        'time_input': time_input,
    }
    
    # Find the index of the entry in all_fields that matches selected_entry on the first 9 fields
    selected_index = next((index for (index, d) in enumerate(all_fields) if {k: d[k] for k in list(d.keys())[:-1]} == selected_entry), None)

    # If a matching entry is found in all_fields, remove it
    if selected_index is not None:
        selected_entry = all_fields[selected_index]
        all_fields.pop(selected_index)
    else:
        print("The selected entry does not exist in the list.")
    
        
        # Stop the process
    if platform.system() == 'Windows':
        os.system(f'taskkill /PID {selected_entry["pid"]} /F')
    else:
        os.kill(selected_entry['pid'], signal.SIGTERM)

    # Save data
    with open('save.json', 'w') as f:
        json.dump(all_fields, f) 
        
def exit_processes():
    for p in processes:
        p.terminate()
    
        

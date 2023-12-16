from tkinter import *
from tkinter import ttk
from process import start_process, delete_process, load_and_start_processes

def create_gui():
    def delete_selected():
        selected_item = treeview.selection()[0]
        values = treeview.item(selected_item, 'values')
        delete_process(values[0].split()[0], values[0].split()[1], values[0].split()[2], values[1], values[2], values[3], values[4], values[5])
        treeview.delete(selected_item)
        
    def start():
        entry = start_process(subject.get(), course.get(), section.get(), seat_type.get(), sender_email.get(), password.get(), recipient_email.get(), time_input.get())
        insert_entry(entry)
        
    def insert_entry(entry):
        course_name = entry['subject'] + " " + entry['course'] + " " + entry['section']
        treeview.insert('', 'end', values=(course_name, entry['seat_type'], entry['sender_email'], entry['password'], entry['recipient_email'], entry['time_input']))
    
    window = Tk()
    window.title("Course Seat Notifier")
    window.resizable(True, True)

    # Add padding and spacing to the window
    for i in range(9):
        window.grid_rowconfigure(i, pad=10, weight=1)
    for i in range(2):
        window.grid_columnconfigure(i, pad=10, weight=1)

    # Create labels and entry fields with padding
    Label(window, text="Sender Email").grid(row=0, padx=10, pady=2)
    Label(window, text="Password (more info in README)").grid(row=1, padx=10, pady=2)
    Label(window, text="Subject (E.g. COMM)").grid(row=2, padx=10, pady=2)
    Label(window, text="Course (E.g. 205)").grid(row=3, padx=10, pady=2)
    Label(window, text="Section (E.g. 202)").grid(row=4, padx=10, pady=2)
    Label(window, text="Seat Type (General/Restricted)").grid(row=5, padx=10, pady=2)
    Label(window, text="Recipient Email").grid(row=6, padx=10, pady=2)
    Label(window, text="Check Time Interval (minutes - min 2)").grid(row=7, padx=10, pady=2)

    # Create entry fields
    sender_email = Entry(window)
    password = Entry(window)
    subject = Entry(window)
    course = Entry(window)
    section = Entry(window)
    seat_type = Entry(window)
    recipient_email = Entry(window)
    time_input = Entry(window)

    # Grid entry fields with padding
    sender_email.grid(row=0, column=1, padx=10, pady=2)
    password.grid(row=1, column=1, padx=10, pady=2)
    subject.grid(row=2, column=1, padx=10, pady=2)
    course.grid(row=3, column=1, padx=10, pady=2)
    section.grid(row=4, column=1, padx=10, pady=2)
    seat_type.grid(row=5, column=1, padx=10, pady=2)
    recipient_email.grid(row=6, column=1, padx=10, pady=2)
    time_input.grid(row=7, column=1, padx=10, pady=2)
    
        # Create the start button
    Button(window, text="Add", command=start).grid(row=9, column=0, columnspan=2, sticky='nsew', pady=4)
    # Create the Delete button
    Button(window, text="Delete", command=delete_selected).grid(row=10, column=0, columnspan=2, sticky='nsew', pady=4)
    
    # Create the table
    columns = ('#1', '#2', '#3', '#4', '#5', '#6')
    treeview = ttk.Treeview(window, columns=columns, show='headings')
    treeview.heading('#1', text='Course')
    treeview.heading('#2', text='Seat Type')
    treeview.heading('#3', text='Sender Email')
    treeview.heading('#4', text='Password')
    treeview.heading('#5', text='Recipient Email')
    treeview.heading('#6', text='Time Input')
    treeview.grid(row=11, column=0, columnspan=2)
    
    all_fields = load_and_start_processes()
    for entry in all_fields:
        insert_entry(entry)
    window.mainloop()
    


    
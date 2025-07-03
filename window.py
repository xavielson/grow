import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import alarm
import datetime
import timer
import data_manager


class MainWindow(tk.Tk):   
    
    def __init__(self):
        super().__init__()
        self.geometry("187x310+600+300")
        self.title("Grow da Galera")
        
        now = datetime.datetime.now()
        self.current_time = now.strftime("%a %d/%m/%y %H:%M:%S")
        
        self.rega_vega_label = tk.Label(self, text=" Rega Vega: ", font=("Arial", 14))        
        self.rega_vega_button = tk.Button(self, name="rega_vega", text="⚫", font=("Arial", 14), height=1, width=1, command=lambda: alarm.toggle_relay(alarm.rega_vega))
        
        self.rega_flora_label = tk.Label(self, text=" Rega Flora: ", font=("Arial", 14))        
        self.rega_flora_button = tk.Button(self, name="rega_flora", text="⚫", font=("Arial", 14), height=1, width=1, command=lambda: alarm.toggle_relay(alarm.rega_flora))

        self.led_vega_label = tk.Label(self, text=" Led Vega: ", font=("Arial", 14))
        self.led_vega_button = tk.Button(self, name="led_vega", text="⚫", font=("Arial", 14), height=1, width=1, command=lambda: alarm.toggle_relay(alarm.led_vega))
        
        self.led_flora_label = tk.Label(self, text=" Led Flora: ", font=("Arial", 14))
        self.led_flora_button = tk.Button(self, name="led_flora", text="⚫", font=("Arial", 14), height=1, width=1, command=lambda: alarm.toggle_relay(alarm.led_flora))
        
        self.wavemaker_label = tk.Label(self, text=" Wavemaker: ", font=("Arial", 14))
        self.wavemaker_button = tk.Button(self, name="wavemaker", text="⚫", font=("Arial", 14), height=1, width=1, command=lambda: alarm.toggle_relay(alarm.wavemaker))
        
        self.runoff_label = tk.Label(self, text=" Runoff: ", font=("Arial", 14))
        self.runoff_button = tk.Button(self, name="runoff", text="⚫", font=("Arial", 14), height=1, width=1, command=lambda: alarm.toggle_relay(alarm.runoff))
        
        self.lights = [self.rega_vega_button,
                       self.rega_flora_button,
                       self.led_vega_button,
                       self.led_flora_button,
                       self.wavemaker_button,
                       self.runoff_button]

        self.clock_label = tk.Label(self, text=self.current_time, font=("Arial", 13))

        self.add_alarm_setting_button = tk.Button(self, text="Settings", command=self.create_settings_window)
        self.open_trigger_list_button = tk.Button(self, text="Open Trigger List", command=self.create_trigger_list_window)
        
        self.rega_vega_label.grid(row=1, column=0, sticky="w")
        #self.rega_vega_status.grid(row=0, column=1, sticky="w")
        self.rega_vega_button.grid(row=1, column=2, sticky="w")
        self.rega_flora_label.grid(row=2, column=0, sticky="w")
        #self.rega_flora_status.grid(row=1, column=1, sticky="w")
        self.rega_flora_button.grid(row=2, column=2, sticky="w")
        self.led_vega_label.grid(row=3, column=0, sticky="w")
        self.led_vega_button.grid(row=3, column=2, sticky="w")
        self.led_flora_label.grid(row=4, column=0, sticky="w")
        self.led_flora_button.grid(row=4, column=2, sticky="w")
        self.wavemaker_label.grid(row=5, column=0, sticky="w")
        self.wavemaker_button.grid(row=5, column=2, sticky="w")
        self.runoff_label.grid(row=6, column=0, sticky="w")
        self.runoff_button.grid(row=6, column=2, sticky="w")        
        
        self.add_alarm_setting_button.grid(row=7, column=0, columnspan=4)
        #self.open_trigger_list_button.grid(row=8, column=0, columnspan=4)
        
        self.clock_label.grid(row=9, column=0, columnspan=4)
        
        self.windows = []
        
    def create_settings_window(self):

        hour = []
        for i in range(24):
            if i > 9:
                hour.append(str(i))
            else:
                hour.append("0" + str(i))
        minute_second = []
        for i in range(60):
            if i > 9:
                minute_second.append(str(i))
            else:
                minute_second.append("0" + str(i))
        
        self.settings_window = tk.Toplevel(self)
        self.list_frame = tk.Frame(self.settings_window)
        self.list_frame.pack()
        
        self.trigger_frame_label_row = tk.Frame(self.settings_window)
        self.trigger_frame_label_row.pack()
        self.middle_frame = tk.Frame(self.settings_window)
        self.middle_frame.pack(pady=10)
        self.trigger_frame_options_row = tk.Frame(self.middle_frame)
        self.trigger_frame_options_row.pack(side="left", padx=10)
        
        self.trigger_frame_options_row2 = tk.Frame(self.middle_frame)
        self.trigger_frame_options_row2.pack(side="left", padx=20)
        self.trigger_frame_button_row = tk.Frame(self.settings_window)
        self.trigger_frame_button_row.pack()   

        self.add_alarm_setting_button["state"] = "disable"
        
        self.windows.append(self.settings_window)
        
        self.settings_window.geometry("+800+300")
        self.settings_window.title("Lista de Triggers")
        
        self.trigger_listbox = tk.Listbox(self.list_frame)
        
        def show_rega_vega_alarms():
            #self.relay_list.set("Rega Vega")
            return self.get_lista_alarmes(self.trigger_listbox, "rega_vega")
        
        def show_rega_flora_alarms():
            #self.relay_list.set("Rega Flora")
            return self.get_lista_alarmes(self.trigger_listbox, "rega_flora")


        self.regavega_button = tk.Button(self.list_frame,
                                         text="Rega Vega",
                                         command=show_rega_vega_alarms)

        self.regaflora_button = tk.Button(self.list_frame,
                                         text="Rega Flora",
                                         command=show_rega_flora_alarms)
        self.ledvega_button = tk.Button(self.list_frame,
                                         text="Led Vega",
                                         command=lambda: self.get_lista_alarmes(self.trigger_listbox, 
                                                                                "led_vega"))
        self.ledflora_button = tk.Button(self.list_frame,
                                         text="Led Flora",
                                         command=lambda: self.get_lista_alarmes(self.trigger_listbox, 
                                                                                "led_flora"))
        self.wavemaker_button = tk.Button(self.list_frame,
                                         text="Wavemaker",
                                         command=lambda: self.get_lista_alarmes(self.trigger_listbox, 
                                                                                "wavemaker"))
        self.runoff_button = tk.Button(self.list_frame,
                                         text=" Runoff ",
                                         command=lambda: self.get_lista_alarmes(self.trigger_listbox, 
                                                                                "runoff")) 
            #label
        create_alarm_label = tk.Label(self.trigger_frame_options_row, 
                                      text="    ", 
                                      font=("Arial", 10))

        #relay combobox
        #self.relay_list = tk.StringVar()
        #self.relay_combobox = ttk.Combobox(self.trigger_frame_options_row, 
        #                              textvariable=self.relay_list, 
        #                              width=9)        
        #self.relay_combobox['values'] = data_manager.relays
        #self.relay_combobox['state'] = 'readonly'

        

        hour_list = tk.StringVar()
        hour_combobox = ttk.Combobox(self.trigger_frame_options_row, 
                                     textvariable=hour_list, 
                                     width=3)
        hour_combobox["values"] = hour
        
        minute_list = tk.StringVar()
        minute_combobox = ttk.Combobox(self.trigger_frame_options_row, 
                                       textvariable=minute_list, 
                                       width=3)
        minute_combobox["values"] = minute_second
        
        second_list = tk.StringVar()
        second_combobox = ttk.Combobox(self.trigger_frame_options_row, 
                                       textvariable=second_list, 
                                       width=3)
        second_combobox["values"] = minute_second

        #onoff radiobutton
        selected_status_button = tk.BooleanVar()

        on = ttk.Radiobutton(self.trigger_frame_options_row2, 
                             text="On   ", 
                             variable=selected_status_button, 
                             value=True)
        
        off = ttk.Radiobutton(self.trigger_frame_options_row2, 
                              text="Off", 
                              variable=selected_status_button, 
                              value=False)        

        #labels
        #relay_label = tk.Label(self.trigger_frame_label_row, 
        #                       text="Relay", 
        #                       font=("Arial", 13),
        #                       width=10)
        
        time_label = tk.Label(self.trigger_frame_options_row, 
                              text="Time", 
                              font=("Arial", 13))
        
        status_label = tk.Label(self.trigger_frame_options_row2, 
                                text="Status", 
                                font=("Arial", 13))
        
        #add alarm button
        add_alarm_button = tk.Button(self.trigger_frame_button_row, 
                                     text="Set Alarm", 
                                     command=lambda: self.add_alarm(self.relay_combobox.get(), 
                                                                    hour_combobox.get(), 
                                                                    minute_combobox.get(), 
                                                                    second_combobox.get(), 
                                                                    selected_status_button))
                
        ### TRIGGER LIST ###  
        self.trigger_listbox.pack(side="left")
        self.regavega_button.pack(expand=True, fill='x')
        self.regaflora_button.pack(expand=True, fill='x')
        self.ledvega_button.pack(expand=True, fill='x')
        
        self.ledflora_button.pack(expand=True, fill='x')
        self.wavemaker_button.pack(expand=True, fill='x')
        self.runoff_button.pack(expand=True, fill='x')

        ### ADD ALARM ###
        #create_alarm_label.pack()

        #relay_label.pack(side="left", expand=True, fill='x')
        time_label.pack()
        status_label.pack()

        #self.relay_combobox.current(0)  # Set default value
      

        #self.relay_combobox.pack(side="left")
        hour_combobox.pack(side="left")
        minute_combobox.pack(side="left")
        second_combobox.pack(side="left")
        on.pack(side="left")
        off.pack(side="left")

        add_alarm_button.pack()

        self.settings_window.protocol("WM_DELETE_WINDOW", self.close_settings_window)

    def close_settings_window(self):
        
        self.settings_window.destroy()
        self.add_alarm_setting_button['state'] = 'normal'   
    
    def create_trigger_list_window(self):
        
#         global trigger_list_window

        self.trigger_list_window = tk.Toplevel(self)
        self.list_frame = tk.Frame(self.trigger_list_window)
        self.list_frame.pack()
        
        self.row1_buttons_frame = tk.Frame(self.trigger_list_window)
        self.row1_buttons_frame.pack()
        self.row2_buttons_frame = tk.Frame(self.trigger_list_window)
        self.row2_buttons_frame.pack()
        
        self.open_trigger_list_button["state"] = "disable"
        
        self.windows.append(self.trigger_list_window)
        
        self.trigger_list_window.geometry("+800+300")
        self.trigger_list_window.title("Lista de Triggers")
        
        self.trigger_listbox = tk.Listbox(self.list_frame)
        
        self.regavega_button = tk.Button(self.list_frame,
                                         text="Rega Vega",
                                         command=lambda: self.get_lista_alarmes(self.trigger_listbox, "rega_vega"))
        self.regaflora_button = tk.Button(self.list_frame,
                                         text="Rega Flora",
                                         command=lambda: self.get_lista_alarmes(self.trigger_listbox, "rega_flora") )
        self.ledvega_button = tk.Button(self.list_frame,
                                         text="Led Vega",
                                         command=lambda: self.get_lista_alarmes(self.trigger_listbox, "led_vega"))
        self.ledflora_button = tk.Button(self.list_frame,
                                         text="Led Flora",
                                         command=lambda: self.get_lista_alarmes(self.trigger_listbox, "led_flora"))
        self.wavemaker_button = tk.Button(self.list_frame,
                                         text="Wavemaker",
                                         command=lambda: self.get_lista_alarmes(self.trigger_listbox, "wavemaker"))
        self.runoff_button = tk.Button(self.list_frame,
                                         text=" Runoff ",
                                         command=lambda: self.get_lista_alarmes(self.trigger_listbox, "runoff")) 
                
        #self.get_lista_alarmes(self.trigger_listbox)  
        self.trigger_listbox.pack(side="left")
        self.regavega_button.pack(expand=True, fill='x')
        self.regaflora_button.pack(expand=True, fill='x')
        self.ledvega_button.pack(expand=True, fill='x')
        
        self.ledflora_button.pack(expand=True, fill='x')
        self.wavemaker_button.pack(expand=True, fill='x')
        self.runoff_button.pack(expand=True, fill='x')       
        
        self.trigger_list_window.protocol("WM_DELETE_WINDOW", self.close_trigger_list_window)
    
    def close_trigger_list_window(self):
        
        self.trigger_list_window.destroy()
        self.open_trigger_list_button['state'] = 'normal'   
    
    def get_lista_alarmes(self, listbox):
        
        x = 1
        for alarme in data_manager.lista_alarmes:
            if alarme.status == 1:
                status = "On"
            elif alarme.status == 0:
                status = "Off"
            listbox.insert(x, alarme.relay_str+" "+alarme.time+" "+status)
            x = x+1        

    def get_lista_alarmes(self, listbox, relay):
        self.trigger_listbox.delete(0, "end")  # Clear the listbox before inserting new items         
        x = 1
        for alarme in data_manager.lista_alarmes:
            if alarme.status == 1:
                status = "On"
            elif alarme.status == 0:
                status = "Off"
            if alarme.relay_str == relay:
                listbox.insert(x, alarme.relay_str+" "+alarme.time+" "+status)
                x = x+1
            else:
                pass     
        
    def create_alarm_setting_window(self):    
        hour = []
        for i in range(24):
            if i > 9:
                hour.append(str(i))
            else:
                hour.append("0" + str(i))
        minute_second = []
        for i in range(60):
            if i > 9:
                minute_second.append(str(i))
            else:
                minute_second.append("0" + str(i))

        self.alarm_setting_window = tk.Toplevel(self)
        self.add_alarm_setting_button["state"] = "disable"
        self.windows.append(self.alarm_setting_window)
        
        self.alarm_setting_window.geometry("315x120+810+300")
        self.alarm_setting_window.title("Adicionar Alarme")

        #label
        create_alarm_label = tk.Label(self.alarm_setting_window, text="    ", font=("Arial", 10))

        #relay combobox
        relay_list = tk.StringVar()
        relay_combobox = ttk.Combobox(self.alarm_setting_window, textvariable=relay_list, width=9)        
        relay_combobox['values'] = data_manager.relays
        relay_combobox['state'] = 'readonly'

        hour_list = tk.StringVar()
        hour_combobox = ttk.Combobox(self.alarm_setting_window, textvariable=hour_list, width=2)
        hour_combobox["values"] = hour
        
        minute_list = tk.StringVar()
        minute_combobox = ttk.Combobox(self.alarm_setting_window, textvariable=minute_list, width=2)
        minute_combobox["values"] = minute_second
        
        second_list = tk.StringVar()
        second_combobox = ttk.Combobox(self.alarm_setting_window, textvariable=second_list, width=2)
        second_combobox["values"] = minute_second 

        #onoff radiobutton
        selected_status_button = tk.BooleanVar()
        on = ttk.Radiobutton(self.alarm_setting_window, text="On", variable=selected_status_button, value=True)
        off = ttk.Radiobutton(self.alarm_setting_window, text="Off", variable=selected_status_button, value=False)        

        #labels
        relay_label = tk.Label(self.alarm_setting_window, text="Relay", font=("Arial", 13))
        time_label = tk.Label(self.alarm_setting_window, text="Time", font=("Arial", 13))
        status_label = tk.Label(self.alarm_setting_window, text="Status", font=("Arial", 13))
        
        #add alarm button
        add_alarm_button = tk.Button(self.alarm_setting_window, text="Set Alarm", command=lambda: self.add_alarm(relay_combobox.get(), hour_combobox.get(), minute_combobox.get(), second_combobox.get(), selected_status_button))    
        
        #positions
        create_alarm_label.grid(row=0, column=1, columnspan=3)

        relay_label.grid(row=1, column=0)
        time_label.grid(row=1, column=1, columnspan=3)
        status_label.grid(row=1, column=4, columnspan=3)

        relay_combobox.grid(row=2, column=0, padx=5)
        hour_combobox.grid(row=2, column=1)
        minute_combobox.grid(row=2, column=2)
        second_combobox.grid(row=2, column=3)
        on.grid(row=2, column=4, padx=5, sticky="e")
        off.grid(row=2, column=5)

        add_alarm_button.grid(row=5, column=1, columnspan=3, pady=10)
        
        self.alarm_setting_window.protocol("WM_DELETE_WINDOW", self.close_alarm_setting_window)
        
    def close_alarm_setting_window(self):
        self.alarm_setting_window.destroy()
        self.add_alarm_setting_button['state'] = 'normal'
        
    def update_main_window(self):
        
        for light in self.lights:
            alarm.update_lights(light)        
   
        now = datetime.datetime.now()
        self.current_time = now.strftime("%a %d/%m/%y %H:%M:%S")
        self.clock_label.config(text=self.current_time)
        
        timer.timer()
        self.after(100, self.update_main_window)  # Update every 1/10 sec

    def add_alarm(self, relay, hora, mins, segs, status):
        
        if data_manager.check_time_input(hora, mins, segs) == True:
            data_manager.insert_alarm(relay, hora, mins, segs, status.get())
            
        else:            
            messagebox.showerror("Erro", "Hora Invalida", parent=self.alarm_setting_window)
        



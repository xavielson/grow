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
        self.geometry("+600+300")
        self.title("Grow da Galera")
        
        now = datetime.datetime.now()
        self.current_time = now.strftime("%a %d/%m/%y %H:%M:%S")
        
        self.rega_vega_label = tk.Label(self, text="  Rega Vega:", 
                                        font=("Arial", 14))        
        self.rega_vega_button = tk.Button(self, name="rega_vega", 
                                          text="⚫", font=("Arial", 14), 
                                          height=1, 
                                          width=1, 
                                          command=lambda: 
                                          alarm.toggle_relay(alarm.rega_vega))
        
        self.rega_flora_label = tk.Label(self, 
                                         text="  Rega Flora:",
                                          font=("Arial", 14))        
        self.rega_flora_button = tk.Button(self, 
                                           name="rega_flora",
                                           text="⚫", 
                                           font=("Arial", 14), 
                                           height=1, width=1, 
                                           command=lambda: 
                                           alarm.toggle_relay(alarm.rega_flora))

        self.led_vega_label = tk.Label(self, 
                                       text="  Led Vega:", 
                                       font=("Arial", 14))
        self.led_vega_button = tk.Button(self, 
                                         name="led_vega", 
                                         text="⚫", 
                                         font=("Arial", 14), 
                                         height=1, 
                                         width=1, 
                                         command=lambda: 
                                         alarm.toggle_relay(alarm.led_vega))
        
        self.led_flora_label = tk.Label(self, 
                                        text="  Led Flora:", 
                                        font=("Arial", 14))
        self.led_flora_button = tk.Button(self, 
                                          name="led_flora", 
                                          text="⚫", font=("Arial", 14), 
                                          height=1, 
                                          width=1, 
                                          command=lambda: 
                                          alarm.toggle_relay(alarm.led_flora))
        
        self.wavemaker_label = tk.Label(self, 
                                        text="  Wavemaker:", 
                                        font=("Arial", 14))
        self.wavemaker_button = tk.Button(self, 
                                          name="wavemaker", 
                                          text="⚫", 
                                          font=("Arial", 14), 
                                          height=1, 
                                          width=1, 
                                          command=lambda: 
                                          alarm.toggle_relay(alarm.wavemaker))
        
        self.runoff_label = tk.Label(self, text="  Runoff:", 
                                     font=("Arial", 14))      
        self.runoff_button = tk.Button(self, 
                                       name="runoff", 
                                       text="⚫", 
                                       font=("Arial", 14), 
                                       height=1, 
                                       width=1, 
                                       command=lambda: 
                                       alarm.toggle_relay(alarm.runoff))

        self.extra1_label = tk.Label(self, text="  Extra 1:", 
                                     font=("Arial", 14))        
        self.extra1_button = tk.Button(self, 
                                       name="extra1", 
                                       text="⚫", 
                                       font=("Arial", 14), 
                                       height=1, 
                                       width=1, 
                                       command=lambda: 
                                       alarm.toggle_relay(alarm.extra1))

        self.extra2_label = tk.Label(self, text="  Extra 2:", 
                                     font=("Arial", 14))        
        self.extra2_button = tk.Button(self, 
                                       name="extra2", 
                                       text="⚫", 
                                       font=("Arial", 14), 
                                       height=1, 
                                       width=1, 
                                       command=lambda: 
                                       alarm.toggle_relay(alarm.extra2))
        
        self.lights = [self.rega_vega_button,
                       self.rega_flora_button,
                       self.led_vega_button,
                       self.led_flora_button,
                       self.wavemaker_button,
                       self.runoff_button,
                       self.extra1_button,
                       self.extra2_button]

        self.clock_label = tk.Label(self, text=self.current_time, font=("Arial", 13))

        self.settings_button = tk.Button(self, text="Settings", command=self.create_settings_window) 

        self.top_space = tk.Label(self, text=" ", font=("Arial", 1))       
        
        self.top_space.grid(row=0, column=0, columnspan=4, pady=3)
        
        self.rega_vega_label.grid(row=2, column=0, sticky="w")
        self.rega_vega_button.grid(row=2, column=2, sticky="w")
        self.rega_flora_label.grid(row=3, column=0, sticky="w")
        self.rega_flora_button.grid(row=3, column=2, sticky="w")
        self.led_vega_label.grid(row=4, column=0, sticky="w")
        self.led_vega_button.grid(row=4, column=2, sticky="w")
        self.led_flora_label.grid(row=5, column=0, sticky="w")
        self.led_flora_button.grid(row=5, column=2, sticky="w")
        self.wavemaker_label.grid(row=6, column=0, sticky="w")
        self.wavemaker_button.grid(row=6, column=2, sticky="w")
        self.runoff_label.grid(row=7, column=0, sticky="w")
        self.runoff_button.grid(row=7, column=2, sticky="w")
        self.extra1_label.grid(row=8, column=0, sticky="w")
        self.extra1_button.grid(row=8, column=2, sticky="w")
        self.extra2_label.grid(row=9, column=0, sticky="w")
        self.extra2_button.grid(row=9, column=2, sticky="w")        
        
        self.settings_button.grid(row=10, column=0, columnspan=4, pady=8)
        
        self.clock_label.grid(row=11, column=0, columnspan=4)
        
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
        self.settings_window.geometry("+800+300")
        self.settings_window.title("Lista de Triggers")

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

        self.settings_button["state"] = "disable"
        
        self.windows.append(self.settings_window)

        self.trigger_listbox = tk.Listbox(self.list_frame, height=13)
        
        self.selected_relay = tk.StringVar()

        self.regavega_button = tk.Button(self.list_frame,
                                         text="Rega Vega",
                                         command=lambda: show_triggers("rega_vega"))

        self.regaflora_button = tk.Button(self.list_frame,
                                         text="Rega Flora",
                                         command=lambda: show_triggers("rega_flora"))

        self.ledvega_button = tk.Button(self.list_frame,
                                         text="Led Vega",
                                         command=lambda: show_triggers("led_vega"))

        self.ledflora_button = tk.Button(self.list_frame,
                                         text="Led Flora",
                                         command=lambda: show_triggers("led_flora"))     

        self.wavemaker_button = tk.Button(self.list_frame,
                                         text="Wavemaker",
                                         command=lambda: show_triggers("wavemaker"))

        self.runoff_button = tk.Button(self.list_frame,
                                         text=" Runoff ",
                                         command=lambda: show_triggers("runoff"))

        self.extra1_button = tk.Button(self.list_frame,
                                         text="Extra 1",
                                         command=lambda: show_triggers("extra1"))
        
        self.extra2_button = tk.Button(self.list_frame,
                                         text="Extra 2",
                                         command=lambda: show_triggers("extra2"))   
 
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
        
        time_label = tk.Label(self.trigger_frame_options_row, 
                              text="Time", 
                              font=("Arial", 13))
        
        status_label = tk.Label(self.trigger_frame_options_row2, 
                                text="Status", 
                                font=("Arial", 13))
        
        def add_trigger(relay, hora, mins, segs, status):
        
            if data_manager.check_time_input(hora, mins, segs):
                data_manager.insert_alarm(relay, hora, mins, segs, status.get())
                self.povoar_listbox_alarmes(self.trigger_listbox, self.selected_relay.get()) 
                
            else:            
                messagebox.showerror("Erro", "Hora Invalida", parent=self.settings_window)

        #add alarm button
        def set_trigger():
            add_trigger(self.selected_relay.get(), 
                             hour_combobox.get(), 
                             minute_combobox.get(), 
                             second_combobox.get(), 
                             selected_status_button)

        set_trigger_button = tk.Button(self.trigger_frame_button_row, 
                                       text="Set Trigger", 
                                       command=set_trigger)
        def delete_trigger():
            try:
                selected_trigger = self.trigger_listbox.get(self.trigger_listbox.curselection())
                relay, time, status = selected_trigger.split(" ", 2)
                print(relay, time, status)
                data_manager.delete_alarm(relay, time, status)
                self.povoar_listbox_alarmes(self.trigger_listbox, self.selected_relay.get())
            except tk.TclError:
                messagebox.showerror("Erro", "Selecione um trigger para deletar", parent=self.settings_window)

        del_trigger_button = tk.Button(self.trigger_frame_button_row, 
                                       text="Del Trigger",
                                       command=delete_trigger)         
        widgets_to_disable = [hour_combobox, minute_combobox, second_combobox, on, off, set_trigger_button, del_trigger_button]

        def enable_widgets(widgets):
            for widget in widgets:
                widget['state'] = 'normal'            

        def disable_widgets(widgets):
            for widget in widgets:
                widget['state'] = 'disabled'

        disable_widgets(widgets_to_disable)

        def show_triggers(relay):
            if set_trigger_button['state'] == 'disabled':
                enable_widgets(widgets_to_disable)
            else:
                pass
            self.selected_relay.set(relay)
            return self.povoar_listbox_alarmes(self.trigger_listbox, relay)

        ### TRIGGER LIST AND BUTTONS###  
        x = 0
        while x < 6:
            self.trigger_listbox.insert(x, "")
            x += 1       
        self.trigger_listbox.insert(7, " Selecione um relay  >>")
        self.trigger_listbox.pack(side="left")

        self.regavega_button.pack(expand=True, fill='x')
        self.regaflora_button.pack(expand=True, fill='x')
        self.ledvega_button.pack(expand=True, fill='x')        
        self.ledflora_button.pack(expand=True, fill='x')
        self.wavemaker_button.pack(expand=True, fill='x')
        self.runoff_button.pack(expand=True, fill='x')
        self.extra1_button.pack(expand=True, fill='x')
        self.extra2_button.pack(expand=True, fill='x')

        ### ADD ALARM ###

        time_label.pack()
        status_label.pack()

        hour_combobox.pack(side="left")
        minute_combobox.pack(side="left")
        second_combobox.pack(side="left")
        on.pack(side="left")
        off.pack(side="left")

        set_trigger_button.pack(side="left", padx=5)
        del_trigger_button.pack(side="left", padx=5)

        self.settings_window.protocol("WM_DELETE_WINDOW", self.close_settings_window)

    def close_settings_window(self):
        
        self.settings_window.destroy()
        self.settings_button['state'] = 'normal'   

    def povoar_listbox_alarmes(self, listbox, relay):
        listbox.delete(0, "end")  # Clear the listbox before inserting new items         
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
        if listbox.size() == 0:
            x = 0
            while x < 6:
                listbox.insert(x, "")
                x += 1 

            listbox.insert(7, " Relay sem Triggers") 
     
    def update_main_window(self):
        
        for light in self.lights:
            alarm.update_lights(light)        
   
        now = datetime.datetime.now()
        self.current_time = now.strftime("%a %d/%m/%y %H:%M:%S")
        self.clock_label.config(text=self.current_time)
        
        timer.timer()
        self.after(100, self.update_main_window)  # Update every 1/10 sec


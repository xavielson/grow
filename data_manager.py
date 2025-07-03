import alarm


relays = ['Rega Vega',
          'Rega Flora',
          'Led Vega',
          'Led Flora',
          'Wave Maker',
          'Bomba Runoff']

lista_alarmes = []

def update_data():
   
    with open("alarm_data.txt","r", encoding='utf-8') as file:
        
        lista_alarmes_raw = file.readlines()
        lista_alarmes.clear()
        
        for alarme in lista_alarmes_raw:            
            if alarme == "\n":
                pass            
            else:                
                alarme = alarme.replace("\n", "")
                alarme_splited = alarme.split("|")                
                lista_alarmes.append(alarm.Alarm(alarme_splited[0], alarme_splited[1], alarme_splited[2]))
            
def reset_data():
    lista_alarmes.clear()
    
def check_time_input(hora, mins, segs):
    time_for_check = [hora, mins, segs]
    ok_items = 0
    for item in time_for_check:
        if item.isdigit() == True:
            ok_items+=1
        else:
            pass
    if ok_items == 3 and int(hora) < 24 and int(mins) < 60 and int(segs) < 60:
        return True
    else:
        return False
    
def insert_alarm(relay, hora, mins, segs, status):
    with open("alarm_data.txt","a", encoding='utf-8') as file:
        
        if status == True:
            status_onoff = "On"
        elif status == False:
            status_onoff = "Off"
        
        relay = relay.replace(" ", "_")
        relay = relay.casefold()        
        
        new_line = relay+"|"+hora+":"+mins+":"+segs+"|"+ status_onoff    
        file.write("\n")
        file.write(new_line)
        file.write("\n")
        
    with open("alarm_data.txt","r+", encoding='utf-8') as file:        
        
        alarm_data_unorganized = file.readlines()
        alarm_data_unorganized.sort()       
        
    with open("alarm_data.txt","w", encoding='utf-8') as file:
        
        for line in alarm_data_unorganized:
            if line == "\n":
                pass
            else:            
                file.write(line)
    
    update_data()
            
def delete_alarm(relay, time, status):
    
    with open("alarm_data.txt","r", encoding='utf-8') as file:
        alarm_data = file.readlines()
    
    with open("alarm_data.txt","r+", encoding='utf-8') as file:
        file.truncate(0)  # Clear the file before writing new content
        for line in alarm_data:
            if line == "\n":
                pass
            else:
                if line.startswith(relay+"|"+time+"|"+status):                    
                    continue
                else:
                    file.write(line)

    update_data()        
    
        
        

    
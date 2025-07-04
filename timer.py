import datetime
import data_manager

#Logica do timer
def timer():
    
    now = datetime.datetime.now() # now = hora atual
    for alarm_setting in data_manager.lista_triggers: # pra cada linha na lista de alarmes
 
        if alarm_setting.time == now.strftime("%H:%M:%S"): # se o tempo bater
            if alarm_setting.status == 1 and alarm_setting.relay.value == 0: # se setar pra on e o relay estiver off
                alarm_setting.relay.on() # liga relay
            elif alarm_setting.status == 0 and alarm_setting.relay.value == 1: # se setar pra off e o relay estiver em on
                alarm_setting.relay.off() # desliga relay
            else: 
                pass
                
            

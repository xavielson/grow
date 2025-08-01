import gpiozero
import data_manager

# Setar Pins
REGA_VEGA_PIN = 2
REGA_FLORA_PIN = 3
LED_VEGA_PIN = 4
LED_FLORA_PIN = 17
WAVEMAKER_PIN = 27
RUNOFF_PIN = 22
EXTRA1_PIN = 10
EXTRA2_PIN = 9

# Iniciar Pins/criar Outputs
rega_vega = gpiozero.OutputDevice(REGA_VEGA_PIN, active_high=False, initial_value=False)
rega_flora = gpiozero.OutputDevice(REGA_FLORA_PIN, active_high=False, initial_value=False)
led_vega = gpiozero.OutputDevice(LED_VEGA_PIN, active_high=False, initial_value=False)
led_flora = gpiozero.OutputDevice(LED_FLORA_PIN, active_high=False, initial_value=False)
wavemaker = gpiozero.OutputDevice(WAVEMAKER_PIN, active_high=False, initial_value=False)
runoff = gpiozero.OutputDevice(RUNOFF_PIN, active_high=False, initial_value=False)
extra1 = gpiozero.OutputDevice(EXTRA1_PIN, active_high=False, initial_value=False)
extra2 = gpiozero.OutputDevice(EXTRA2_PIN, active_high=False, initial_value=False)

# Checa se algum led deve ser ligado no start

def get_led_triggers():
    for line in data_manager.lista_triggers:
        if line.relay_str == "led_vega":
            if line.relay.value == 0:

                print(line.time)

def check_led_state_on_start(hora_liga, hora_desliga):
    
    lista = []

    y=1
    while y<3:
        x=1
        while x<25:
            lista.append(x)
            x += 1    
        y += 1

    hora_atual=13
    if hora_liga > hora_desliga:

        for i, j in enumerate(lista):
            if j == hora_liga:
                index_hora_liga = i
                break

        for i, j in enumerate(lista):
            if j == hora_desliga:
                index_hora_desliga = i

        x = index_hora_liga

        while x < index_hora_desliga:
            if lista[x] == hora_atual:
                return True
            else:
                return False
            x += 1

    if hora_liga < hora_desliga:

        if hora_atual > hora_liga and hora_atual < hora_desliga:
            return True
        else:
            return False

    
# Liga e desliga os relés
def toggle_relay(relay):
    if relay.value == 0:
        relay.on()
    elif relay.value == 1:
        relay.off()
# Atualiza as "luzes" de acordo com o estado dos relés      
def update_lights(light):
    if str(light) == ".rega_vega":
        if rega_vega.value == 0:
            light.configure(fg="red", activeforeground="red")
        elif rega_vega.value == 1:
            light.configure(fg="green", activeforeground="green")
            
    elif str(light) == ".rega_flora":
        if rega_flora.value == 0:
            light.configure(fg="red", activeforeground="red")
        elif rega_flora.value == 1:
            light.configure(fg="green", activeforeground="green")
            
    elif str(light) == ".led_vega":
        if led_vega.value == 0:
            light.configure(fg="red", activeforeground="red")
        elif led_vega.value == 1:
            light.configure(fg="green", activeforeground="green")
            
    elif str(light) == ".led_flora":
        if led_flora.value == 0:
            light.configure(fg="red", activeforeground="red")
        elif led_flora.value == 1:
            light.configure(fg="green", activeforeground="green")
            
    elif str(light) == ".wavemaker":
        if wavemaker.value == 0:
            light.configure(fg="red", activeforeground="red")
        elif wavemaker.value == 1:
            light.configure(fg="green", activeforeground="green")

    elif str(light) == ".runoff":
        if runoff.value == 0:
            light.configure(fg="red", activeforeground="red")
        elif runoff.value == 1:
            light.configure(fg="green", activeforeground="green")

    elif str(light) == ".extra1":
        if extra1.value == 0:
            light.configure(fg="red", activeforeground="red")
        elif extra1.value == 1:
            light.configure(fg="green", activeforeground="green")   

    elif str(light) == ".extra2":
        if extra2.value == 0:
            light.configure(fg="red", activeforeground="red")
        elif extra2.value == 1:
            light.configure(fg="green", activeforeground="green")           
# Classe Trigger
class Trigger:
    def __init__(self, relay, time, status):
        if relay == "rega_vega":            
            self.relay = rega_vega
            self.relay_str = relay
        elif relay == "rega_flora":            
            self.relay = rega_flora
            self.relay_str = relay
        elif relay == "led_vega":            
            self.relay = led_vega
            self.relay_str = relay
        elif relay == "led_flora":      
            self.relay = led_flora
            self.relay_str = relay
        elif relay == "wavemaker":            
            self.relay = wavemaker
            self.relay_str = relay
        elif relay == "runoff":            
            self.relay = runoff
            self.relay_str = relay
        elif relay == "extra1":
            self.relay = extra1
            self.relay_str = relay
        elif relay == "extra2":
            self.relay = extra2
            self.relay_str = relay
        else:
            raise ValueError("Invalid relay name")
         
        self.time = time
        if status == "On":
            self.status = 1
        elif status == "Off":
            self.status = 0
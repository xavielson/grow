import data_manager
import window
import alarm

# Initialize the data manager and load the data     
data_manager.update_data()
# Checar se as luzes devem ser ligadas
# alarm.check_led_state_on_start(alarm.led_vega)
# alarm.check_led_state_on_start(alarm.led_flora)
alarm.get_led_triggers()
# Cria a janela principal
main_window = window.MainWindow()
# Atualiza a janela principal com os dados carregados
main_window.update_main_window()
# Inicia o loop principal da janela
main_window.mainloop()
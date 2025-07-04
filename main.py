import data_manager
import window

# Initialize the data manager and load the data     
data_manager.update_data()

# Cria a janela principal
main_window = window.MainWindow()
# Atualiza a janela principal com os dados carregados
main_window.update_main_window()
# Inicia o loop principal da janela
main_window.mainloop()
import PySimpleGUI as sg 
import random

reset = False
user_in = 0
images = ["piedra.png", "papel.png", "tijera.png"]


layout = [[sg.Button(key="-USER_IN-", image_filename=images[0]),
		   sg.Button("JUGAR!", size=(12,5), key="-PLAY-"), 
		   sg.Image(key="-COMP_IN-", size=(180,140))]]

window = sg.Window("piedra-Papel-Tijera", layout=layout)

while True:
	event, values = window.read()

	if event == sg.WIN_CLOSED:
		break

	#control boton del usuario
	if event == "-USER_IN-":
		if not reset:
			user_in = (user_in+1)%3 #0, 1, 2, 0, 1, 2, 0,....
			window["-USER_IN-"].update(image_filename=images[user_in])

	#control boton jugar
	if event == "-PLAY-":
		if not reset:
			comp_in = random.randint(0,2)
			window["-COMP_IN-"].update(filename=images[comp_in])
			window["-PLAY-"].update("RESET")

			#validar los resultados
			if user_in == comp_in:  #empate
				window["-PLAY-"].update(button_color=("white", "yellow"))

			elif user_in == 0:  #user piedra
				if comp_in==1:  #comp Papel
					window["-PLAY-"].update(button_color=("white", "red"))		
				elif comp_in==2:  #comp tijera
					window["-PLAY-"].update(button_color=("white", "green"))		

			elif user_in == 1:  #user papel
				if comp_in==0:  #comp Piedra
					window["-PLAY-"].update(button_color=("white", "green"))		
				elif comp_in==2:  #comp tijera
					window["-PLAY-"].update(button_color=("white", "red"))		

			elif user_in == 2:  #user tijera
				if comp_in==0:  #comp piedra
					window["-PLAY-"].update(button_color=("white", "red"))		
				elif comp_in==1:  #comp papel
					window["-PLAY-"].update(button_color=("white", "green"))		
	
		#si dice RESET, se reeinicia el juego
		else:
			window["-PLAY-"].update("JUGAR!", button_color=("white", sg.theme_background_color()))
			window["-USER_IN-"].update(image_filename=images[0])
			window["-COMP_IN-"].ipdate(filename=None)

		#intercambio de la variable reset
		reste = not reset

window.close()
import pygame
import random
import time
import os


def load_image(name):
    path = os.path.join('', name)
    return pygame.image.load(path).convert() 

pygame.init()
icono = pygame.image.load("images/icon.png")
pygame.display.set_icon(icono)


serp_tamano = 10
ancho = 900
altura = 500

Blanco = (255, 255, 255)
Azul = (96, 111, 140)
Negro = (0, 0, 0)
Rojo = (255, 0, 0)
Verde = (0, 153, 0)
Lila = (128, 0, 128)

superficie = pygame.display.set_mode((ancho,altura))
pygame.display.set_caption('Serpiente')

reloj = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)


def serpiente(serp_tamano, listaSerpiente):
    for i in listaSerpiente:
        pygame.draw.rect(superficie, Negro, [i[0],i[1], serp_tamano, serp_tamano])

def text_objetos(text, color):
    textSuperficie = font.render(text, True, color)
    return textSuperficie, textSuperficie.get_rect()

def message_to_screen(msg, color, x_displace=0, y_displace=0):
    textSur, textRect = text_objetos(msg,color)
    textRect.center = (ancho/2)+ x_displace, (altura/2)+ y_displace
    superficie.blit(textSur, textRect)

def pausa():
    
    pausado = True
    while pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()
            if event.type == pygame.KEYDOWN:
            	if event.key == pygame.K_c:
               	   pausado = False

            	elif event.key == pygame.K_s:
                     pygame.quit()
                     quit()

        background = load_image('images/pausa_1.jpg')
        superficie.fill(Blanco)
        superficie.blit(background, [ 280,50])
        message_to_screen("Pausa",Negro, 0, -140)
        message_to_screen("Para continuar, presione c ", Negro, 0, 170)
        pygame.display.update()
        reloj.tick(5)

def puntos(score):
    text = font.render("Puntos: "+str(score), True, Negro)
    superficie.blit(text, [0,0])

def intro_juego():

    intro = True
    while intro:
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			pygame.quit()
    			quit()
    	if event.type == pygame.KEYDOWN:
	      	if event.key == pygame.K_c:
	    		intro = False

	        elif event.key == pygame.K_s:
	        	pygame.quit()
	           	quit()

      	background = load_image('images/intro_1.jpg')
      	superficie.fill(Blanco)
      	superficie.blit(background, [ 250, 0])
      	message_to_screen("Bienvenido", Negro, 0, -220)
      	message_to_screen("El objetivo del juego es controlar una serpiente usando", Azul, 0, -170)
      	message_to_screen("las flechas de movimiento para comer manzanas", Azul, 0, -120)
      	message_to_screen("Al comer la manzana roja, la serpiente crece 1 cuadro y cada 3 manzanas rojas aumenta la rapidez en 1.", Azul, 0,-70)
      	message_to_screen("Al comer la manzana verde, la serpiente aumenta la rapidez en 1.", Negro, 0, -20)
      	message_to_screen("Al comer la manzana lila, la serpiente crece 10 cuadros.", Azul, 0, 30)
      	message_to_screen("Si la serpiente toca el borde o a si misma, pierdes.", Azul, 0, 80)
      	message_to_screen("Para pausar partida, presiona tecla P.", Azul, 0, 130)
      	message_to_screen("Para continuar partida, presiona tecla C.", Negro, 0, 180)
      	message_to_screen("Para terminar de jugar y salir, presiona tecla S.", Azul, 0, 230)
      	pygame.display.update()
    	reloj.tick(10)

def gameLoop():

    gameExit = False
    gameOver = False

    mover_x = 300
    mover_y = 300

    mover_x_cambio = 0
    mover_y_cambio = 0

    listaSerpiente = []
    largoSerpiente = 1

    cuadro = 15
    rapidez = cuadro        
    num_rojas = 0
        
    pulsar_sonido = pygame.mixer.Sound("sound/Song.ogg")
    pulsar_sonido.set_volume(0.50)
    pulsar_sonido.play(18)

    background = load_image('images/fondo_v1.jpeg')
    background_over = load_image('images/over_1.jpg')
	    
    azarManzana_roja_X = round(random.randrange(0, ancho - 10)/10.0)*10.0
    azarManzana_roja_Y = round(random.randrange(0, altura - 10)/10.0)*10.0

    azarManzana_verde_X = round(random.randrange(0, ancho - 10)/10.0)*10.0
    azarManzana_verde_Y = round(random.randrange(0, altura - 10)/10.0)*10.0

    azarManzana_lila_X = round(random.randrange(0, ancho - 10)/10.0)*10.0
    azarManzana_lila_Y = round(random.randrange(0, altura - 10)/10.0)*10.0
   
    while not gameExit:

        while gameOver == True:

            superficie.blit(background_over, [0,0])
            message_to_screen("Si desea continuar presione la tecla c", Blanco, 0, 150)
            message_to_screen("Para salir presione la tecla S", Blanco, 0, 200)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_s:
                      gameExit = True
                      gameOver = False
                   if event.key == pygame.K_c:
                   	  gameLoop()

        for event in pygame.event.get():
        	if event.type == pygame.QUIT:
        		gameExit = True
        	if event.type == pygame.KEYDOWN:
        		if event.key == pygame.K_LEFT:
        			mover_x_cambio = -serp_tamano
        			mover_y_cambio = 0
        		elif event.key == pygame.K_RIGHT:
        			mover_x_cambio = serp_tamano
        			mover_y_cambio = 0
        	 	elif event.key == pygame.K_UP:
				mover_y_cambio = -serp_tamano
				mover_x_cambio = 0
			elif event.key == pygame.K_DOWN:
				mover_y_cambio = serp_tamano
				mover_x_cambio = 0
			elif event.key == pygame.K_p:
				pausa()
              
	if mover_x >= ancho or mover_x < 0 or mover_y >= altura or mover_y < 0:
		gameOver = True
		
	mover_x += mover_x_cambio
	mover_y += mover_y_cambio
	superficie.blit(background, [ 0, 0])
        pygame.draw.rect(superficie, Rojo, [azarManzana_roja_X, azarManzana_roja_Y, 10, 10])
        pygame.draw.rect(superficie, Verde, [azarManzana_verde_X, azarManzana_verde_Y, 10, 10])
        pygame.draw.rect(superficie, Lila, [azarManzana_lila_X, azarManzana_lila_Y, 10, 10])

        cabezaSerpiente = []
        cabezaSerpiente.append(mover_x)
        cabezaSerpiente.append(mover_y)
        listaSerpiente.append(cabezaSerpiente)

        if len(listaSerpiente) > largoSerpiente:
		del listaSerpiente[0]
        for eachSegment in listaSerpiente[:-1]:
        	if eachSegment == cabezaSerpiente:
        		gameOver = True

        serpiente(serp_tamano, listaSerpiente)
        puntos(largoSerpiente-1)
        message_to_screen("Rapidez: "+ str(rapidez),Negro,-400,-220)
        pygame.display.update()

        if mover_x == azarManzana_roja_X and mover_y == azarManzana_roja_Y:
        	pygame.mixer.music.load("Song.ogg")
        	azarManzana_roja_X = round(random.randrange(0, ancho - 10)/10.0)*10.0
        	azarManzana_roja_Y = round(random.randrange(0, altura - 10)/10.0)*10.0
        	largoSerpiente += 1
        	num_rojas += 1
        	if num_rojas ==3:
            		rapidez +=1
              		num_rojas = 0

        if mover_x == azarManzana_verde_X and mover_y == azarManzana_verde_Y:
        	azarManzana_verde_X = round(random.randrange(0, ancho - 10)/10.0)*10.0
        	azarManzana_verde_Y = round(random.randrange(0, altura - 10)/10.0)*10.0
        	rapidez += 1
	    
	if mover_x == azarManzana_lila_X and mover_y == azarManzana_lila_Y:
		azarManzana_lila_X = round(random.randrange(0, ancho - 10)/10.0)*10.0
		azarManzana_lila_Y = round(random.randrange(0, altura - 10)/10.0)*10.0
		largoSerpiente += 10

	reloj.tick(rapidez)

intro_juego()
gameLoop()


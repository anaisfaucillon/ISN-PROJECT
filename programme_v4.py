import pygame
from pygame.locals import *
from constantes import *

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.mouse.set_visible(0)

# SON pris sur https://themushroomkingdom.net/wav.shtml


#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((largeur, longeur))


#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)

#Musique d'Ouverture
son = pygame.mixer.Sound('musique\son2.wav')
son.play(loops=0, maxtime=0, fade_ms=0)


#Images ------------------------------------------
accueil = pygame.image.load(image_accueil).convert()
accueilB = pygame.image.load(image_accueilB).convert()
accueilC = pygame.image.load(image_accueilC).convert()
end = pygame.image.load(image_end).convert()
#perso fond noir
perso = pygame.image.load(image_perso).convert_alpha()
#persoB fond blanc
persoB = pygame.image.load(image_persoB).convert_alpha()

#Jeu Niveau 1 ------------------------------------------
def niveau1() :
    fenetre.blit(perso, (800,200))
    pygame.display.flip()   
    position_perso = perso.get_rect()
    position_perso = position_perso.move(1000, 300) 
    #fenetre.blit(perso, position_perso)
    #pygame.display.flip()
    continuer = 1
    while continuer:
        #Re-collage
        fenetre.blit(accueilB, (0,0))
        fenetre.blit(perso, position_perso)
        #Rafraichissement
        pygame.display.flip()
        print(position_perso)
        for evt in pygame.event.get():
            #print(evt.type)
            if position_perso == (60,260,77,95):
                print ("gagné")
                continuer = 0
                fenetre.blit(accueilC, (0,0))
                pygame.display.flip()
                niveau2()
            if evt.type == pygame.locals.KEYDOWN:
                if evt.key == K_UP:   #Si "flèche haut"
                    #On monte le perso
                    position_perso = position_perso.move(0,-20)
                if evt.key == K_DOWN: #Si "flèche bas"
                    #On descend le perso
                   position_perso = position_perso.move(0,20)
                if evt.key == K_LEFT: #Si "flèche gauche"
                    #On bouge le perso a gauche
                    position_perso = position_perso.move(-20,0)
                if evt.key == K_RIGHT:    #Si "flèche droite"
                    #On bouge le perso a droite
                    position_perso = position_perso.move(20,0)
                if evt.key == K_x:
                    continuer = 0
                    fenetre.blit(end, (0,0))
                    pygame.display.flip()

   
#Jeu Niveau 2 ------------------------------------------
def niveau2() :
    #Gestion du timer
    TpsZero = pygame.time.get_ticks()
    #Gestion de la position 
    position_perso = perso.get_rect()
    position_perso = position_perso.move(0, 160) 
    #fenetre.blit(perso, position_perso)
    #pygame.display.flip()
    accueilC = pygame.image.load(image_accueilC).convert()
    continuer = 1
 
    while continuer:
        #Re-collage
        #Gestion du timer---------------------------------------
        seconds = (pygame.time.get_ticks() - TpsZero) / 1000
        print(seconds)
        titre_fenetre = str(seconds)
        pygame.display.set_caption(titre_fenetre)
        pygame.display.flip()
        #Gestion du timer -------------------------------------
        fenetre.blit(accueilC, (0,0))
        fenetre.blit(persoB, position_perso)
        #Rafraichissement
        #background.blit(text, textpos)
        pygame.display.flip()
        for evt in pygame.event.get():
            #print(position_perso)
            if position_perso == (1080,640,77,95):
                print ("gagné")
                continuer = 0
                son = pygame.mixer.Sound('musique\son9.wav')
                son.play(loops=0, maxtime=0, fade_ms=0)
                font = pygame.font.Font(None, 36)
                text = font.render("Fin ", 1, (10, 10, 10))
                background = pygame.Surface(screen.get_size())
                background = background.convert()
                background.fill((250, 250, 250))
                textpos = text.get_rect(centerx=background.get_width()/2)
                background.blit(text, textpos)
                screen.blit(background, (0, 0))
                pygame.display.flip()
                
                fenetre.blit(end, (0,0))
                pygame.display.flip()
                
            if position_perso == (510, 190, 77, 95):
               son = pygame.mixer.Sound('musique\son7.wav')
               son.play(loops=0, maxtime=0, fade_ms=0)
               print ("image a changer 1")
               accueilC = pygame.image.load(image_accueilE).convert()
               fenetre.blit(accueilC, (0,0))
               fenetre.blit(perso, position_perso)
                   
            if position_perso == (330, 520, 77, 95):
               son = pygame.mixer.Sound('musique\son4.wav')
               son.play(loops=0, maxtime=0, fade_ms=0)
               print ("image a changer 2 ")
               accueilC = pygame.image.load(image_accueilF).convert()
               fenetre.blit(accueilC, (0,0))
               fenetre.blit(perso, position_perso)
                    
            if position_perso == (600, 640, 77, 95):
               son = pygame.mixer.Sound('musique\son5.wav')
               son.play(loops=0, maxtime=0, fade_ms=0)
               print ("image a changer 3")
               accueilC = pygame.image.load(image_accueilG).convert()
               fenetre.blit(accueilC, (0,0))
               fenetre.blit(perso, position_perso)
                       
            if position_perso == (870, 640, 77, 95):                                    
               son = pygame.mixer.Sound('musique\son10.wav')
               son.play(loops=0, maxtime=0, fade_ms=0)
               print ("image a changer 4")
               accueilC = pygame.image.load(image_accueilH).convert()
               fenetre.blit(accueilC, (0,0))
               fenetre.blit(perso, position_perso)
                
            if evt.type == pygame.locals.KEYDOWN:
                if evt.key == K_UP:   #Si "flèche haut"
                    #On monte le perso
                    position_perso = position_perso.move(0,-30)
                if evt.key == K_DOWN: #Si "flèche bas"
                    #On descend le perso
                   position_perso = position_perso.move(0,30)
                if evt.key == K_LEFT: #Si "flèche gauche"
                    #On bouge le perso a gauche
                    position_perso = position_perso.move(-30,0)
                if evt.key == K_RIGHT:    #Si "flèche droite"
                    #On bouge le perso a droite
                    position_perso = position_perso.move(30,0)
                if evt.key == K_x:
                    continuer = 0
                    fenetre.blit(end, (0,0))
                    pygame.display.flip()


    
fenetre.blit(accueil, (0,0))

#Titre
pygame.display.set_caption(titre_fenetre)

continuer_accueil = 1
continuer_jeu = 1
                
#BOUCLE PRINCIPALE------------------------------------------
                   
continuer_accueil = 1
while continuer_accueil:
    pygame.display.flip()
    for event in pygame.event.get():
       #print(event.type)
        if event.type == pygame.locals.KEYDOWN:
            if event.key == K_s:
                #print("Niveau 1")
                #fenetre.blit(niveau, (0,0))
                #pygame.display.flip()
                son = pygame.mixer.Sound('musique\son1.wav')
                son.play(loops=0, maxtime=0, fade_ms=0)
                niveau1()
                
            if event.key == K_q:
                print("END")
                fenetre.blit(end, (0,0))
                pygame.display.flip()
                continuer_accueil = 0

       #probleme du calvier en qwerty        
            if event.key == K_a:
                print("END")
                fenetre.blit(end, (0,0))
                pygame.display.flip()
                continuer_accueil = 0
                
        elif event.type == MOUSEBUTTONDOWN :
                fenetre = pygame.display.set_mode((1,0))
                fenetre.blit(end, (0,0))
                pygame.display.flip()
                continuer_accueil = 0



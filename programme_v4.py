#import sys
import pygame
from pygame.locals import *
from constantes import *
from sys import *

pygame.init()

# Copyright (c) -------------------------------
# Les sons proviennent de https://themushroomkingdom.net/wav.shtml
# Les images proviennent de
    # https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1399813-premieres-fenetres
    # SITE KL-Architectes / # Couloir des laboratoires du lycée Georges-de-la-Tour à Metz
    # SITE PARCOURSUP Parcoursup // © Fotolia
    # Retravaillé ISSU DU SITE GachatLife

#Ouverture de la fenêtre Pygame
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
    pygame.display.set_caption("Niveau 1 , trouve la sortie en déplacant le personnage avec les flèche du clavier ")
    pygame.display.flip()   
    position_perso = perso.get_rect()
    position_perso = position_perso.move(1000, 300) 
    continuer = 1
    while continuer:
        #Rafraichissement
        fenetre.blit(accueilB, (0,0))
        fenetre.blit(perso, position_perso)
        pygame.display.flip()
        #print(position_perso)
        for evt in pygame.event.get():
            #print(evt.type)
            if position_perso == (60,260,77,95):
                # Sortie Trouvée 
                continuer = 0
                fenetre.blit(accueilC, (0,0))
                pygame.display.flip()
                # Acces au Niveau 2
                niveau2()
            if evt.type == pygame.locals.KEYDOWN:
                if evt.key == K_UP:
                    #Si "flèche haut"
                    #On monte le perso
                    position_perso = position_perso.move(0,-20)
                if evt.key == K_DOWN:
                    #Si "flèche bas"
                    #On descend le perso
                   position_perso = position_perso.move(0,20)
                if evt.key == K_LEFT:
                    #Si "flèche gauche"
                    #On bouge le perso a gauche
                    position_perso = position_perso.move(-20,0)
                if evt.key == K_RIGHT:
                    #Si "flèche droite"
                    #On bouge le perso a droite
                    position_perso = position_perso.move(20,0)
                if evt.key == K_x:
                    continuer = 0
                    fenetre.blit(end, (0,0))
                    pygame.display.flip()


        
#Jeu Niveau 2 ------------------------------------------
def niveau2() :

    #création d'une fonte pour l'affichage du score et des bonus
    #None = on prend la police par défaut de pygame, on augmente juste les tailles
    score_font = pygame.font.Font(None, 40)
    bonusA_font = pygame.font.Font(None, 50)
    
    #Gestion du timer
    TpsZero = pygame.time.get_ticks()
    
    #Gestion de la position 
    position_perso = perso.get_rect()
    position_perso = position_perso.move(0, 160)
    
    accueilC = pygame.image.load(image_accueilC).convert()
    pygame.display.set_caption("Niveau 2 , trouve la sortie en déplacant le plus vite possible le personnage et trouve les bonus")
    continuer = 1
    Bonus = 0
 
    while continuer:
         
        #Gestion du timer
        seconds = (pygame.time.get_ticks() - TpsZero) / 1000
        #On prend le temps que du 2nd Niveau et pas depuis le début du jeu ( - TpsZero)
        
        score = score_font.render(format(str(seconds) ), 1, (255,0,0))
        bonusA = bonusA_font.render(format(str(Bonus) ), 1, (255,0,0))

        #Rafraichissement des images, des timer, des bonus, du personnage
        fenetre.blit(accueilC, (0,0))
        fenetre.blit(persoB, position_perso)
        fenetre.blit(score, (1075, 260))
        fenetre.blit(bonusA, (740, 360))
        pygame.display.flip()
        
        for evt in pygame.event.get():
            if position_perso == (1080,640,77,95):
                #Sortie Trouvée
                continuer = 0
                #font = pygame.font.Font(None, 36)
                #text = font.render("Fin ", 1, (10, 10, 10))
                #Text = pygame.font.Font(None, 30)
                #On affiche le résultat 
                screen = pygame.display.set_mode((1200,800), 0, 32)
                score_board(screen,seconds, Bonus)
                
            if position_perso == (510, 190, 77, 95):
                #Bonus 1 Trouvé
                son = pygame.mixer.Sound('musique\son7.wav')
                son.play(loops=0, maxtime=0, fade_ms=0)
                accueilC = pygame.image.load(image_accueilE).convert()
                fenetre.blit(accueilC, (0,0))
                fenetre.blit(perso, position_perso)
                Bonus = Bonus + 1
                   
            if position_perso == (330, 520, 77, 95):
                #Bonus 2 Trouvé
                son = pygame.mixer.Sound('musique\son4.wav')
                son.play(loops=0, maxtime=0, fade_ms=0)
                accueilC = pygame.image.load(image_accueilF).convert()
                fenetre.blit(accueilC, (0,0))
                fenetre.blit(perso, position_perso)
                Bonus = Bonus + 1
                    
            if position_perso == (600, 640, 77, 95):
                #Bonus 3 Trouvé
                son = pygame.mixer.Sound('musique\son5.wav')
                son.play(loops=0, maxtime=0, fade_ms=0)
                accueilC = pygame.image.load(image_accueilG).convert()
                fenetre.blit(accueilC, (0,0))
                fenetre.blit(perso, position_perso)
                Bonus = Bonus + 1
                       
            if position_perso == (870, 640, 77, 95):
                #Bonus 4 Trouvé
                son = pygame.mixer.Sound('musique\son10.wav')
                son.play(loops=0, maxtime=0, fade_ms=0)
                accueilC = pygame.image.load(image_accueilH).convert()
                fenetre.blit(accueilC, (0,0))
                fenetre.blit(perso, position_perso)
                Bonus = Bonus + 1
                
            if evt.type == pygame.locals.KEYDOWN:
                if evt.key == K_UP:
                    #Si "flèche haut" on monte le perso
                    position_perso = position_perso.move(0,-30)
                if evt.key == K_DOWN:
                    #Si "flèche bas" on descend le perso
                   position_perso = position_perso.move(0,30)
                if evt.key == K_LEFT:
                    #Si "flèche gauche" on bouge le perso a gauche
                    position_perso = position_perso.move(-30,0)
                if evt.key == K_RIGHT:
                    #Si "flèche droite" on bouge le perso a droite
                    position_perso = position_perso.move(30,0)
                if evt.key == K_x:
                    continuer = 0
                    fenetre.blit(end, (0,0))
                    pygame.display.flip()

#Gestion du Score et de la fin du Niveau 2 ------------------------------------------
def score_board(screen, scorefinal, bonus):

    Text = pygame.font.Font(None, 60)

    # On va lire dans le fichier le dernier high score
    file = open('high_score.txt','r+')
    highscore = float(file.read())
    file.close()

    screen.blit(end, (0,0))

    # Format du temps et des bonus
    # '%d' % (42,)
    # '%f' % (3.141592653589793,)
    
    text2 = Text.render('Le temps est de : %f'  % scorefinal, 50, (255,0,0))
    #couleur de la fonte (ici rouge) / (255, 0, 0)
    screen.blit(text2, (100,100))
    text2 = Text.render('Les bonus sont de : %d' %  bonus, 5, (255,0,0))
 
    screen.blit(text2, (100,150))
        
    scorefinal = scorefinal - bonus
    #print (scorefinal)
    text1 = Text.render('Score Final : %f' % scorefinal, 5, (255,0,0))
    screen.blit(text1, (100,200))
                    
    if scorefinal<=highscore:  
        file = open('high_score.txt','w+')
        file.write(str(scorefinal))
        file.close()               
        text2 = Text.render('Bravo !! Nouveau Highscore: %f' % scorefinal, 5, (255,0,0))
        screen.blit(text2, (100,250))
        son = pygame.mixer.Sound('musique\son9.wav')
        son.play(loops=0, maxtime=0, fade_ms=0)
        
    else:
        text2 = Text.render('Perdu !! Il fallait faire moins de: %f' % highscore, 5, (255,0,0))
        screen.blit(text2, (100,250))
        son = pygame.mixer.Sound('musique\son8.wav')
        son.play(loops=0, maxtime=0, fade_ms=0)
        
#Debut------------------------------------------
                    
fenetre.blit(accueil, (0,0))

#Titre
pygame.display.set_caption("Début du Jeu ")

pygame.display.flip()

continuer_accueil = 1
continuer_jeu = 1
                
#BOUCLE PRINCIPALE------------------------------------------
                   
continuer_accueil = 1
while continuer_accueil:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.locals.KEYDOWN:
            if event.key == K_s:
                #print("Niveau 1")
                #fenetre.blit(niveau, (0,0))
                #pygame.display.flip()
                son = pygame.mixer.Sound('musique\son1.wav')
                son.play(loops=0, maxtime=0, fade_ms=0)
                # Acces au Niveau 1
                niveau1()
                
            if event.key == K_q:
                print("END")
                fenetre.blit(end, (0,0))
                pygame.display.flip()
                continuer_accueil = 0

               #cas du calvier en qwerty  / azerty         
            if event.key == K_a:
                print("END")
                fenetre.blit(end, (0,0))
                pygame.display.flip()
                continuer_accueil = 0
                
        #On arrete ausi avec un clic de souris
            #elif event.type == MOUSEBUTTONDOWN :
                #fenetre = pygame.display.set_mode((1,0))
                #fenetre.blit(end, (0,0))
                #pygame.display.flip()
                #continuer_accueil = 0



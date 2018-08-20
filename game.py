import random

import pygame


pygame.init()



class Player():
    posX = 250
    posY = 600
    slika = pygame.image.load('auto.png')
    brzina = 4
    hitbox = pygame.Rect(posX, posY, 100, 180)

class Prepreka():
    posX = 0
    posY = -100
    slika = pygame.image.load('kutija.png')
    hitbox = pygame.Rect(posX, posY, 100, 100)
    def __init__(self, x):
        self.posX = x

    def __str__(self):
        return str(self.posX) + "\t" + str(self.posY)

class Moci():
    posX = 0
    posY = -100
    ime = ""
    slika = pygame.image.load("2x.png")
    hitbox = pygame.Rect(posX, posY, 100, 100)
    trajanje = 500
    pokupljena = False
    def __init__(self, slika, ime, posX):
        self.ime = ime
        self.slika = slika
        self.posX = posX

def gameMainLoop():
    global run, poeni, listaPrepreka, backgroundSpeed, brzinaFlag, stitFlag
    backgroundSpeed = 5
    run = True
    listaPrepreka = []
    poeni = 0
    igrac.posX = 250
    igrac.posY = 600
    igrac.hitbox = pygame.Rect(igrac.posX, igrac.posY, 100, 180)
    while run:
        pygame.time.delay(10)
        refreshScreen()
        stvarajPrepreke()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pygame.Rect(550, 0, 50, 50).collidepoint(x, y):
                    pauzaFlag = True
                    while pauzaFlag:
                        for r in pygame.event.get():
                            if r.type == pygame.MOUSEBUTTONDOWN:
                                pauzaFlag = False
                            if r.type == pygame.QUIT:
                                run = False
                                pauzaFlag = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if igrac.posX > 70:
                igrac.posX -= igrac.brzina
                igrac.hitbox = pygame.Rect(igrac.posX, igrac.posY, 100, 180)
        elif keys[pygame.K_RIGHT]:
            if igrac.posX < 430:
                igrac.posX += igrac.brzina
                igrac.hitbox = pygame.Rect(igrac.posX, igrac.posY, 100, 180)
        if keys[pygame.K_UP]:
            if igrac.posY > 10:
                igrac.posY -= igrac.brzina
                igrac.hitbox = pygame.Rect(igrac.posX, igrac.posY, 100, 180)
        elif keys[pygame.K_DOWN]:
            if igrac.posY < 600:
                igrac.posY += igrac.brzina
                igrac.hitbox = pygame.Rect(igrac.posX, igrac.posY, 100, 180)

        for prepreka in listaPrepreka:
            if igrac.hitbox.colliderect(prepreka.hitbox) and not moc.pokupljena:
                gameOver()
            elif igrac.hitbox.colliderect(prepreka.hitbox) and moc.pokupljena and moc.ime == "2x":
                gameOver()
        if igrac.hitbox.colliderect(moc.hitbox):
            moc.pokupljena = True



def refreshScreen():
    global backgroundOffset, mocFlag, mocPravac, mocCounter, stitFlag, brzinaFlag
    inicijalnaBrzina = backgroundSpeed
    prozor.blit(background, (0, backgroundOffset))
    pygame.draw.rect(prozor, (255, 0, 0), igrac.hitbox, 5)
    prozor.blit(pauza, (550, 0))

    for prepreka in listaPrepreka:
        if moc.pokupljena and moc.ime == "2x":
            prepreka.posY += backgroundSpeed*2
        else:
            prepreka.posY += inicijalnaBrzina
        prozor.blit(prepreka.slika, (prepreka.posX, prepreka.posY))
        prepreka.hitbox = pygame.Rect(prepreka.posX, prepreka.posY, 100, 100)
        if prepreka.posY > 900:
            listaPrepreka.remove(prepreka)
    if mocFlag:
        if moc.pokupljena:
            moc.trajanje -= 1
        if moc.trajanje == 0:
            moc.pokupljena = False
        if not moc.pokupljena:
            prozor.blit(moc.slika, (moc.posX, moc.posY))
            pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(moc.posX, moc.posY, 100, 100), 5)

        if moc.posX < 70 or moc.posX > 430:
            mocPravac *= -1
        moc.posX += mocPravac*5
        moc.posY += 1
        moc.hitbox = pygame.Rect(moc.posX, moc.posY, 100, 100)
        if moc.posY > 850:
            mocFlag = False
    for prepreka in listaPrepreka:
        pygame.draw.rect(prozor, (255, 0, 0), prepreka.hitbox, 5)
    if moc.pokupljena and moc.ime == "2x":
        backgroundOffset += backgroundSpeed*2
    else:
        backgroundOffset += backgroundSpeed
    if backgroundOffset > 0:
        backgroundOffset = -800
    prozor.blit(igrac.slika, (igrac.posX, igrac.posY))
    poeniPrint()

    pygame.display.flip()

def stvarajPrepreke():
    global mocFlag, moc
    if random.randint(1, 100) == 50:
        listaPrepreka.append(Prepreka(random.choice(pozicijePreprekaX)))
    if random.randint(1, 10) == 5 and not mocFlag:
        randomBroj = random.randint(0, 1)
        moc = Moci(listaMociSlika[randomBroj], listaMociImena[randomBroj], random.choice(pozicijePreprekaX))
        mocFlag = True

def gameOver():
    global run
    run = False
    gameOver = pygame.image.load('gameOver.png')
    prozor.fill((0, 0, 0))
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text1 = "Osvojili ste " + str(poeni) + " poena!"
    text11 = font.render(text1, True, (255, 255, 255))
    prozor.blit(text11, (140, 150))
    playAgainRect = pygame.Rect(200, 420, 75, 75)
    quitRect = pygame.Rect(325, 420, 75, 75)
    prozor.blit(gameOver, (125, 200))
    prozor.blit(pygame.image.load('playAgain.png'), (200, 420))
    prozor.blit(pygame.image.load('quit.png'), (325, 420))
    pygame.display.flip()
    cekaj = True
    while cekaj:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                if playAgainRect.collidepoint(x, y):
                    cekaj = False
                    gameMainLoop()
                elif quitRect.collidepoint(x, y):
                    run = False
                    cekaj = False
                    pygame.quit()
                    quit()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

def poeniPrint():
    global poeni, backgroundSpeed
    text1 = "Poeni: "
    text2 = str(poeni)
    text3 = "Brzina: " + str(backgroundSpeed)
    font = pygame.font.SysFont('Comic Sans MS', 15)
    text1 = font.render(text1, True, (0, 0, 0))
    text2 = font.render(text2, True, (0, 0, 0))
    text3 = font.render(text3, True, (0, 0, 0))
    poeni += backgroundSpeed
    if int(poeni / 1000) + backgroundSpeed > backgroundSpeed:
        backgroundSpeed = 5 + (int(poeni / 1000 / 2))
    if moc.pokupljena:
        poeniText = "Moc: " + str(moc.trajanje)
        poeniText = font.render(poeniText, True, (0, 0, 0))
        prozor.blit(poeniText, (5, 50))
    prozor.blit(text1, (5, 5))
    prozor.blit(text2, (5, 20))
    prozor.blit(text3, (5, 35))



run = True
mocFlag = False
moc = Moci(pygame.image.load("2x.png"), "2x", 70)
mocPravac = 1
pozicijePreprekaX = (70, 190, 310, 430)
listaPrepreka = []
listaMociImena = ["2x", "stit"]
listaMociSlika = [pygame.image.load("2x.png"), pygame.image.load("stit.png")]
poeni = 0
background = pygame.image.load('put4trake.png')
pauza = pygame.image.load("pauza.png")
prozor = pygame.display.set_mode((600, 800))
backgroundOffset = -800
backgroundSpeed = 5
igrac = Player()
gameMainLoop()

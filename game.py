import random
import sqlite3

import pygame


pygame.init()



class Player():
    posX = 250
    posY = 600
    slika = pygame.image.load("auto.png")
    brzina = 6
    hitbox = pygame.Rect(posX, posY, 100, 180)

class Prepreka():
    posX = 0
    posY = -100
    slika = pygame.image.load("kutija.png")
    hitbox = pygame.Rect(posX, posY, 100, 100)
    slomljena = False
    def __init__(self, x):
        self.posX = x

    def __str__(self):
        return str(self.posX) + "\t" + str(self.posY)

class Moci():
    posX = 0
    posY = -100
    ime = ""
    slika = pygame.image.load("brzina.png")
    hitbox = pygame.Rect(posX, posY, 100, 100)
    trajanje = 500
    pokupljena = False
    balon = pygame.image.load("balon.png")
    def __init__(self, slika, ime, posX):
        self.ime = ime
        self.slika = slika
        self.posX = posX

    def __del__(self):
        pass

def mainMenu():
    menu = True
    menuSlika = pygame.image.load("menuSlika.png")

    while menu:
        prozor.blit(menuSlika, (0, 0))
        #pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(220, 355, 160, 50), 5)
        #pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(220, 430, 160, 50), 5)
        #pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(225, 580, 150, 50), 5)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pygame.Rect(220, 355, 160, 50).collidepoint(x, y):
                    menu = False
                if pygame.Rect(225, 580, 150, 50).collidepoint(x, y):
                    menu = False
                    pygame.quit()
                    quit()
                if pygame.Rect(220, 430, 160, 50).collidepoint(x, y):
                    helpMenu()
    unesiImeMeni()
    gameMainLoop()

def pauzaMenu():
    pauzaFlag = True
    pauzaSlika = pygame.image.load("pauseMenu.png")
    prozor.blit(pauzaSlika, (0, 0))
    #pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(109, 363, 75, 75), 1)
    #pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(210, 363, 75, 75), 1)
    #pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(313, 363, 75, 75), 1)
    #pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(414, 363, 75, 75), 1)

    pygame.display.flip()
    while pauzaFlag:
        for r in pygame.event.get():
            if r.type == pygame.MOUSEBUTTONDOWN:
                x, y = r.pos
                if pygame.Rect(109, 363, 75, 75).collidepoint(x, y):
                    pauzaFlag = False
                if pygame.Rect(210, 363, 75, 75).collidepoint(x, y):
                    gameMainLoop()
                if pygame.Rect(313, 363, 75, 75).collidepoint(x, y):
                    mainMenu()
                if pygame.Rect(414, 363, 75, 75).collidepoint(x, y):
                    pygame.quit()
                    quit()
            if r.type == pygame.QUIT:
                pygame.quit()
                quit()


def helpMenu():
    helpFlag = True
    helpSlika = pygame.image.load("help.png")
    while helpFlag:
        prozor.blit(helpSlika, (0, 0))
        #pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(210, 680, 160, 50), 5)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pygame.Rect(210, 680, 160, 50).collidepoint(x, y):
                    helpFlag = False
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def unesiImeMeni():
    global ime
    clock = pygame.time.Clock()

    input_box = pygame.Rect(150, 300, 300, 45)
    color_inactive = pygame.Color('gray')
    color_active = pygame.Color('white')
    color = color_active
    active = True
    text = ''
    done = False
    font = pygame.font.SysFont('Comic Sans MS', 30)
    labelaIme = "Unesite vase ime:"
    labelaIme = font.render(labelaIme, True, (255, 255, 255))
    imeRect = labelaIme.get_rect()
    imeRect.centerx = prozor.get_rect().centerx
    imeRect.centery = 200
    pygame.display.flip()
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = True
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        ime = text
                        text = ''
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        prozor.fill((0, 0, 0))
        prozor.blit(labelaIme, imeRect)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        #width = max(200, txt_surface.get_width() + 10)
        #input_box.w = width
        # Blit the text.
        prozor.blit(txt_surface, (input_box.x + 5, input_box.y))
        # Blit the input_box rect.
        pygame.draw.rect(prozor, color, input_box, 2)

        pygame.display.flip()
        clock.tick(50)





def gameMainLoop():
    global run, poeni, listaPrepreka, backgroundSpeed, brzinaFlag, stitFlag
    backgroundSpeed = 5
    run = True
    listaPrepreka = []
    poeni = 0
    igrac.posX = 250
    igrac.posY = 600
    igrac.hitbox = pygame.Rect(igrac.posX, igrac.posY, 100, 180)
    moc.pokupljena = False
    moc.trajanje = 0

    while run:
        #pygame.time.delay(10)
        clock = pygame.time.Clock()
        pygame.display.flip()
        refreshScreen()
        stvarajPrepreke()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pygame.Rect(550, 0, 50, 50).collidepoint(x, y):
                    pauzaMenu()


        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if igrac.posX > 70:
                igrac.posX -= igrac.brzina
                igrac.hitbox = pygame.Rect(igrac.posX, igrac.posY, 100, 180)
        elif keys[pygame.K_d]:
            if igrac.posX < 430:
                igrac.posX += igrac.brzina
                igrac.hitbox = pygame.Rect(igrac.posX, igrac.posY, 100, 180)
        if keys[pygame.K_w]:
            if igrac.posY > 10:
                igrac.posY -= igrac.brzina
                igrac.hitbox = pygame.Rect(igrac.posX, igrac.posY, 100, 180)
        elif keys[pygame.K_s]:
            if igrac.posY < 600:
                igrac.posY += igrac.brzina
                igrac.hitbox = pygame.Rect(igrac.posX, igrac.posY, 100, 180)

        for prepreka in listaPrepreka:
            if igrac.hitbox.colliderect(prepreka.hitbox) and not moc.pokupljena and not prepreka.slomljena:
                gameOver()
            elif igrac.hitbox.colliderect(prepreka.hitbox) and moc.pokupljena and moc.ime == "brzina" and not prepreka.slomljena:
                gameOver()

        if igrac.hitbox.colliderect(moc.hitbox) and not moc.pokupljena and mocFlag:
            moc.pokupljena = True
            moc.trajanje = 500
        clock.tick(50)




def refreshScreen():
    global backgroundOffset, mocFlag, mocPravac, backgroundSpeed
    inicijalnaBrzina = backgroundSpeed
    #if moc.pokupljena and moc.ime == "brzina" and moc.trajanje == 500:
        #backgroundSpeed = inicijalnaBrzina + 2

    prozor.blit(background, (0, backgroundOffset))
    #pygame.draw.rect(prozor, (255, 0, 0), igrac.hitbox, 5)
    prozor.blit(pauza, (550, 0))

    for prepreka in listaPrepreka:
        if moc.pokupljena and moc.ime == "brzina":
            prepreka.posY += backgroundSpeed+2
        else:
            prepreka.posY += inicijalnaBrzina
        if moc.pokupljena and moc.ime == "stit":
            if igrac.hitbox.colliderect(prepreka.hitbox):
                prepreka.slika = pygame.image.load("slomljenaKutija.png")
                prepreka.slomljena = True

        prozor.blit(prepreka.slika, (prepreka.posX, prepreka.posY))
        prepreka.hitbox = pygame.Rect(prepreka.posX, prepreka.posY, 100, 100)
        if prepreka.posY > 900:
            listaPrepreka.remove(prepreka)
    if mocFlag:
        if moc.pokupljena:
            moc.trajanje -= 1
        if moc.trajanje == 0:
            moc.pokupljena = False
            mocFlag = False
            moc.posY = 850
            backgroundSpeed = inicijalnaBrzina
        if moc.posY > 850 and not moc.pokupljena:
            mocFlag = False
        if moc.pokupljena and moc.ime == "stit":
            prozor.blit(moc.balon, (igrac.posX - 20, igrac.posY - 20))

        if not moc.pokupljena:
            prozor.blit(moc.slika, (moc.posX, moc.posY))
            #pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(moc.posX, moc.posY, 100, 100), 5)

        if moc.posX < 70 or moc.posX > 430:
            mocPravac *= -1
        moc.posX += mocPravac*5
        moc.posY += 5
        moc.hitbox = pygame.Rect(moc.posX, moc.posY, 100, 100)


    '''for prepreka in listaPrepreka:
        pygame.draw.rect(prozor, (255, 0, 0), prepreka.hitbox, 5)'''
    if moc.pokupljena and moc.ime == "brzina":
        backgroundOffset += backgroundSpeed+2
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
    global run, ime
    run = False
    gameOverSlika = pygame.image.load("gameOverMenu.png")
    prozor.blit(gameOverSlika, (0, 0))
    font = pygame.font.SysFont('Comic Sans MS', 30)
    imeLabela = font.render(str("Cestitamo " + ime + ','), True, (255, 255, 255))
    rectIme = imeLabela.get_rect()
    rectIme.centerx = prozor.get_rect().centerx
    rectIme.centery = 110
    poeniLabela = "Osvojili ste " + str(poeni) + " poena!"
    poeniLabela = font.render(poeniLabela, True, (255, 255, 255))
    rectPoeni = poeniLabela.get_rect()
    rectPoeni.centerx = prozor.get_rect().centerx
    rectPoeni.centery = 150
    #pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(161, 520, 75, 75), 1)
    #pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(264, 520, 75, 75), 1)
    #ygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(365, 520, 75, 75), 1)

    prozor.blit(imeLabela, rectIme)
    prozor.blit(poeniLabela, rectPoeni)
    pygame.display.flip()

    conn = sqlite3.connect('game.db')
    c = conn.cursor()
    #c.execute('INSERT INTO igrac (ime, poeni) values ("' + ime + '", ' + str(poeni) + ')')
    # conn.commit()
    # c.execute('delete from igrac where ime = "ImeIgraca"')
    # conn.commit()

    for row in c.execute('SELECT * FROM igrac'):
        print(row)
    conn.close()


    cekaj = True
    while cekaj:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                if pygame.Rect(161, 520, 75, 75).collidepoint(x, y):
                    cekaj = False
                    gameMainLoop()
                if pygame.Rect(264, 520, 75, 75).collidepoint(x, y):
                    cekaj = False
                    mainMenu()
                if pygame.Rect(365, 520, 75, 75).collidepoint(x, y):
                    pygame.quit()
                    quit()

            if event.type == pygame.QUIT:
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


ime = ''
run = True
mocFlag = False
moc = Moci(pygame.image.load("brzina.png"), "brzina", 70)
mocPravac = 1
pozicijePreprekaX = (70, 190, 310, 430)
listaPrepreka = []
listaMociImena = ["brzina", "stit"]
listaMociSlika = [pygame.image.load("brzina.png"), pygame.image.load("stit.png")]
poeni = 0
background = pygame.image.load('put4trake.png')
pauza = pygame.image.load("pauza.png")
prozor = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Highway to hell")
backgroundOffset = -800
backgroundSpeed = 5
igrac = Player()
mainMenu()
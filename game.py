import random
import sqlite3
import pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()


class Player:
    posX = 250
    posY = 600
    slika = pygame.image.load("slike/auto.png")
    brzina = 6
    hitbox = pygame.Rect(posX, posY, 100, 180)


class Prepreka:
    posX = 0
    posY = -100
    slika = pygame.image.load("slike/kutija.png")
    hitbox = pygame.Rect(posX, posY, 100, 100)
    slomljena = False

    def __init__(self, x):
        self.posX = x

    def __str__(self):
        return str(self.posX) + "\t" + str(self.posY)


class Moci:
    pos_x = 0
    pos_y = -100
    slika = pygame.image.load("slike/brzina.png")
    hitbox = pygame.Rect(pos_x, pos_y, 100, 100)
    trajanje = 500
    pokupljena = False
    balon = pygame.image.load("slike/balon.png")

    def __init__(self, slika, naziv, pos_x):
        self.ime = naziv
        self.slika = slika
        self.posX = pos_x

    def __del__(self):
        pass


def main_menu():
    global run, restartFlag, mainMenuFlag, helpMenuFlag, pauzaMenuFlag, scoreboardMenuFlag, unesiImeFleg, musicFlag, \
        soundFlag
    mainMenuFlag = True
    menu_slika = pygame.image.load("slike/menu_slika.png")
    mute_music = pygame.image.load("slike/MusicBela.png")
    mute_sound = pygame.image.load("slike/VolumeBela.png")
    while mainMenuFlag:
        prozor.blit(menu_slika, (0, 0))
        prozor.blit(mute_music, (550, 750))
        prozor.blit(mute_sound, (500, 750))
        if not soundFlag:
            pygame.draw.line(prozor, (255, 0, 0), (505, 795), (545, 755), 5)
        if not musicFlag:
            pygame.draw.line(prozor, (255, 0, 0), (555, 795), (595, 755), 5)
        # pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(222, 354, 160, 52), 1)
        # pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(222, 434, 160, 52), 1)
        # pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(98, 514, 408, 52), 1)
        # pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(225, 593, 152, 54), 1)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pygame.Rect(222, 354, 160, 52).collidepoint(x, y):
                    mainMenuFlag = False
                    unesiImeFleg = True
                if pygame.Rect(222, 434, 160, 52).collidepoint(x, y):
                    mainMenuFlag = False
                    helpMenuFlag = True
                if pygame.Rect(98, 514, 408, 52).collidepoint(x, y):
                    scoreboardMenuFlag = True
                    mainMenuFlag = False
                if pygame.Rect(550, 750, 50, 50).collidepoint(x, y):
                    if musicFlag:
                        pygame.mixer.music.pause()
                        musicFlag = False
                    else:
                        pygame.mixer.music.unpause()
                        musicFlag = True
                if pygame.Rect(500, 750, 50, 50).collidepoint(x, y):
                    if soundFlag:
                        soundFlag = False
                    else:
                        soundFlag = True
                if pygame.Rect(225, 593, 152, 54).collidepoint(x, y):
                    mainMenuFlag = False
                    pygame.quit()
                    quit()


def pauza_menu():
    global run, restartFlag, mainMenuFlag, helpMenuFlag, pauzaMenuFlag, scoreboardMenuFlag
    pauzaMenuFlag = True
    pauza_slika = pygame.image.load("slike/pause_menu.png")
    prozor.blit(pauza_slika, (0, 0))
    pygame.display.flip()
    while pauzaMenuFlag:
        for r in pygame.event.get():
            if r.type == pygame.MOUSEBUTTONDOWN:
                x, y = r.pos
                if pygame.Rect(109, 363, 75, 75).collidepoint(x, y):
                    pauzaMenuFlag = False
                if pygame.Rect(210, 363, 75, 75).collidepoint(x, y):
                    run = False
                    pauzaMenuFlag = False
                    restartFlag = True
                if pygame.Rect(313, 363, 75, 75).collidepoint(x, y):
                    pauzaMenuFlag = False
                    mainMenuFlag = True
                    run = False
                if pygame.Rect(414, 363, 75, 75).collidepoint(x, y):
                    pygame.quit()
                    quit()
            if r.type == pygame.QUIT:
                pygame.quit()
                quit()


def help_menu():
    global run, restartFlag, mainMenuFlag, helpMenuFlag, pauzaMenuFlag, scoreboardMenuFlag
    helpMenuFlag = True
    help_slika = pygame.image.load("slike/help.png")
    # pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(207, 676, 174, 50), 1)
    while helpMenuFlag:
        prozor.blit(help_slika, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pygame.Rect(207, 676, 174, 50).collidepoint(x, y):
                    helpMenuFlag = False
                    mainMenuFlag = True
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def unesi_ime_menu():
    global ime, mainMenuFlag, run, unesiImeFleg
    clock = pygame.time.Clock()
    input_box = pygame.Rect(150, 300, 300, 45)
    color_inactive = pygame.Color('gray')
    color_active = pygame.Color('white')
    color = color_active
    active = True
    text = ''
    done = False
    font = pygame.font.SysFont('Comic Sans MS', 30)
    labela_ime = "ENTER YOUR NAME"
    labela_ime = font.render(labela_ime, True, (255, 255, 255))
    ime_rect = labela_ime.get_rect()
    ime_rect.centerx = prozor.get_rect().centerx
    ime_rect.centery = 250
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if input_box.collidepoint(x, y):
                    active = True
                else:
                    active = False
                color = color_active if active else color_inactive
                if pygame.Rect(182, 402, 235, 52).collidepoint(x, y):
                    ime = text
                    if ime == '':
                        ime = "Nije uneto ime"
                    text = ''
                    done = True
                    unesiImeFleg = False
                    run = True
                if pygame.Rect(217, 481, 167, 52).collidepoint(x, y):
                    text = ''
                    done = True
                    mainMenuFlag = True
                    run = False
                    unesiImeFleg = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        ime = text
                        if ime == '':
                            ime = "Nije uneto ime"
                        text = ''
                        done = True
                        run = True
                        unesiImeFleg = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        prozor.fill((0, 0, 0))
        prozor.blit(pygame.image.load("slike/unesiImeDugmad.png"), (181, 400))
        # pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(182, 402, 235, 52), 1)
        # pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(217, 481, 167, 52), 1)
        prozor.blit(labela_ime, ime_rect)
        txt_surface = font.render(text, True, color)
        prozor.blit(txt_surface, (input_box.x + 5, input_box.y))
        pygame.draw.rect(prozor, color, input_box, 2)
        pygame.display.flip()
        clock.tick(50)


def score_menu():
    global run, restartFlag, mainMenuFlag, helpMenuFlag, pauzaMenuFlag, scoreboardMenuFlag
    scoreboardMenuFlag = True
    prozor.blit(pygame.image.load("slike/scoreBoard.png"), (0, 0))
    # pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(207, 676, 174, 50), 1)
    font = pygame.font.SysFont('Comic Sans MS', 30)
    offset_y = 140
    conn = sqlite3.connect("game.db")
    c = conn.cursor()
    for fetch in c.execute("select * from igrac order by poeni desc"):
        text_ime = font.render(fetch[0], True, (255, 255, 255))
        text_poeni = font.render(str(fetch[1]), True, (255, 255, 255))
        prozor.blit(text_ime, (100, offset_y))
        prozor.blit(text_poeni, (380, offset_y))
        offset_y += 46
    pygame.display.update()
    conn.close()
    while scoreboardMenuFlag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pygame.Rect(207, 676, 174, 50).collidepoint(x, y):
                    scoreboardMenuFlag = False
                    mainMenuFlag = True


def game_main_loop():
    global run, poeni, listaPrepreka, backgroundSpeed, restartFlag, soundFlag, musicFlag
    if restartFlag:
        restartFlag = False
    pygame.display.flip()
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
        clock = pygame.time.Clock()
        pygame.display.flip()
        refresh_screen()
        stvaraj_prepreke()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pygame.Rect(550, 0, 50, 50).collidepoint(x, y):
                    pauza_menu()
                if pygame.Rect(550, 50, 50, 50).collidepoint(x, y):
                    if soundFlag:
                        soundFlag = False
                    else:
                        soundFlag = True
                if pygame.Rect(550, 100, 50, 50).collidepoint(x, y):
                    if musicFlag:
                        pygame.mixer.music.pause()
                        musicFlag = False
                    else:
                        pygame.mixer.music.unpause()
                        musicFlag = True
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
                game_over()
            elif igrac.hitbox.colliderect(prepreka.hitbox) and moc.pokupljena and moc.ime == "brzina" and not \
                    prepreka.slomljena:
                game_over()

        if igrac.hitbox.colliderect(moc.hitbox) and not moc.pokupljena and mocFlag:
            if soundFlag:
                pygame.mixer.Sound('zvuci/stit.wav').play()
            moc.pokupljena = True
            moc.trajanje = 500
        clock.tick(50)


def refresh_screen():
    global backgroundOffset, mocFlag, mocPravac, backgroundSpeed, poeni
    inicijalna_brzina = backgroundSpeed
    # if moc.pokupljena and moc.ime == "brzina" and moc.trajanje == 500:
    # backgroundSpeed = inicijalna_brzina + 2

    prozor.blit(background, (0, backgroundOffset))
    # pygame.draw.rect(prozor, (255, 0, 0), igrac.hitbox, 5)
    prozor.blit(pauza, (550, 0))
    prozor.blit(mute_sound_game, (550, 50))
    prozor.blit(mute_music_game, (550, 100))
    if not soundFlag:
        pygame.draw.line(prozor, (255, 0, 0), (555, 95), (595, 55), 5)
    if not musicFlag:
        pygame.draw.line(prozor, (255, 0, 0), (555, 145), (595, 105), 5)

    for prepreka in listaPrepreka:
        if moc.pokupljena and moc.ime == "brzina":
            prepreka.posY += backgroundSpeed+2
        else:
            prepreka.posY += inicijalna_brzina
        if moc.pokupljena and moc.ime == "stit":
            if igrac.hitbox.colliderect(prepreka.hitbox) and not prepreka.slomljena:
                prepreka.slika = pygame.image.load("slike/slomljenaKutija.png")
                if soundFlag:
                    pygame.mixer.Sound('zvuci/crate_break.wav').play()
                prepreka.slomljena = True
                poeni += 500

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
            moc.pos_y = 850
            backgroundSpeed = inicijalna_brzina
        if moc.pos_y > 850 and not moc.pokupljena:
            mocFlag = False
        if moc.pokupljena and moc.ime == "stit":
            prozor.blit(moc.balon, (igrac.posX - 20, igrac.posY - 20))

        if not moc.pokupljena:
            prozor.blit(moc.slika, (moc.posX, moc.pos_y))
            # pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(moc.posX, moc.pos_y, 100, 100), 5)

        if moc.posX < 70 or moc.posX > 430:
            mocPravac *= -1
        moc.posX += mocPravac*5
        moc.pos_y += 5
        moc.hitbox = pygame.Rect(moc.posX, moc.pos_y, 100, 100)

    '''for prepreka in listaPrepreka:
        pygame.draw.rect(prozor, (255, 0, 0), prepreka.hitbox, 5)'''
    if moc.pokupljena and moc.ime == "brzina":
        backgroundOffset += backgroundSpeed+2
    else:
        backgroundOffset += backgroundSpeed
    if backgroundOffset > 0:
        backgroundOffset = -800
    prozor.blit(igrac.slika, (igrac.posX, igrac.posY))
    poeni_print()
    pygame.display.flip()


def stvaraj_prepreke():
    global mocFlag, moc
    if random.randint(1, 100) == 50:
        listaPrepreka.append(Prepreka(random.choice(pozicijePreprekaX)))
    if random.randint(1, 100) == 5 and not mocFlag:
        random_broj = random.randint(0, 1)
        moc = Moci(listaMociSlika[random_broj], listaMociImena[random_broj], random.choice(pozicijePreprekaX))
        mocFlag = True


def game_over():
    global run, restartFlag, mainMenuFlag, helpMenuFlag, pauzaMenuFlag, scoreboardMenuFlag, unesiImeFleg
    run = False
    if soundFlag:
        pygame.mixer.Sound('zvuci/game_over.wav').play()
    game_over_slika = pygame.image.load("slike/game_over_menu.png")
    prozor.blit(game_over_slika, (0, 0))
    font = pygame.font.SysFont('Comic Sans MS', 30)
    ime_labela = font.render(str("Cestitamo " + ime + ','), True, (255, 255, 255))
    rect_ime = ime_labela.get_rect()
    rect_ime.centerx = prozor.get_rect().centerx
    rect_ime.centery = 110
    poeni_labela = "Osvojili ste " + str(poeni) + " poena!"
    poeni_labela = font.render(poeni_labela, True, (255, 255, 255))
    rect_poeni = poeni_labela.get_rect()
    rect_poeni.centerx = prozor.get_rect().centerx
    rect_poeni.centery = 150
    # pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(161, 520, 75, 75), 1)
    # pygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(264, 520, 75, 75), 1)
    # ygame.draw.rect(prozor, (255, 0, 0), pygame.Rect(365, 520, 75, 75), 1)

    prozor.blit(ime_labela, rect_ime)
    prozor.blit(poeni_labela, rect_poeni)
    pygame.display.flip()

    conn = sqlite3.connect('game.db')
    c = conn.cursor()
    c.execute('update igrac set ime = "' + ime + '", poeni = ' + str(poeni) +
              ' where poeni = (select min(poeni) from igrac)')
    conn.commit()
    conn.close()

    cekaj = True
    while cekaj:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                if pygame.Rect(161, 520, 75, 75).collidepoint(x, y):
                    cekaj = False
                    restartFlag = True
                if pygame.Rect(264, 520, 75, 75).collidepoint(x, y):
                    cekaj = False
                    mainMenuFlag = True
                if pygame.Rect(365, 520, 75, 75).collidepoint(x, y):
                    pygame.quit()
                    quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def poeni_print():
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
        poeni_text = "Moc: " + str(moc.trajanje)
        poeni_text = font.render(poeni_text, True, (0, 0, 0))
        prozor.blit(poeni_text, (5, 50))
    prozor.blit(text1, (5, 5))
    prozor.blit(text2, (5, 20))
    prozor.blit(text3, (5, 35))


def glavni_loop():
    global run, restartFlag, mainMenuFlag, helpMenuFlag, pauzaMenuFlag, scoreboardMenuFlag, unesiImeFleg
    mainMenuFlag = True
    pygame.mixer.music.load("zvuci/Highway To Hell.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)
    while True:
        if mainMenuFlag:
            main_menu()
        elif unesiImeFleg:
            unesi_ime_menu()
        elif run:
            game_main_loop()
        elif restartFlag:
            game_main_loop()
        elif helpMenuFlag:
            help_menu()
        elif pauzaMenuFlag:
            pauza_menu()
        elif scoreboardMenuFlag:
            score_menu()


run = restartFlag = mainMenuFlag = helpMenuFlag = pauzaMenuFlag = scoreboardMenuFlag = unesiImeFleg = GameOverFlag \
    = False
ime = ''
mocFlag = False
musicFlag = soundFlag = True
moc = Moci(pygame.image.load("slike/brzina.png"), "brzina", 70)
mocPravac = 1
pozicijePreprekaX = (70, 190, 310, 430)
listaPrepreka = []
listaMociImena = ["brzina", "stit"]
listaMociSlika = [pygame.image.load("slike/brzina.png"), pygame.image.load("slike/stit.png")]
poeni = 0
background = pygame.image.load('slike/put4trake.png')
pauza = pygame.image.load("slike/pauza.png")
mute_music_game = pygame.image.load("slike/MusicCrna.png")
mute_sound_game = pygame.image.load("slike/VolumeCrna.png")
prozor = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Highway to hell")
backgroundOffset = -800
backgroundSpeed = 5
igrac = Player()
glavni_loop()

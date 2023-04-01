from pygame import *
from random import *
win_width = 700
win_height = 500
window  = display.set_mode((win_width,win_height))
display.set_caption('test')

mixer.init()
mixer.music.load('doom_03.-At-Doom_s-Gate.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
clock = time.Clock()
FPS = 60
background = transform.scale(image.load('Hell.jpg'),(win_width,win_height))

class GameSprite(sprite.Sprite):
    def __init__(self,sprite_image,check_x,check_y,sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image),(50,75))
        self.rect = self.image.get_rect()
        self.rect.x = check_x
        self.rect.y = check_y
        self.speed = sprite_speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and self.rect.x > 1 :
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < 643 :
            self.rect.x += self.speed
        if key_pressed[K_q] and self.rect.x > 1 :
            self.rect.x -= 30
        if key_pressed[K_e] and self.rect.x < 643 :
            self.rect.x += 30  
    def fire(self):
        bullet = Bullet('Teleport_anim.gif',self.rect.centerx,self.rect.top,11)
        bullets.add(bullet)

player = Player('Doom_Slayer.png',333,422,10)
lifes = 5
lost = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80,win_width -80)
            self.rect.y = 0
            lost = lost + 1
class Chaos(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80,win_width -80)
            self.rect.y = 0
class reven(Chaos):
    def ogon(self):  
        bullet = Bullet('Teleport_anim.gif',self.rect.centerx,self.rect.top,-11)
        bullets.add(bullet)

won = 0
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 15:
            self.kill()
#class BulletEnemy(GameSprite):
#    def update(self):
#        global lifes
#        self.rect.y -= self.speed
#        if :
#            global lifes
#            lifes = lifes - 1
#        if self.rect.y > 575:
#            self.kill()

font.init()
font1 = font.SysFont('Arial',36)
font2 = font.SysFont('Arial',36)
monsters = sprite.Group()
monsters2 = sprite.Group()
monsters3 = sprite.Group()
for i in range(0,5):
    monster = Enemy('pngegg.png',randint(80,win_width -80),0,randint(1,5))
    monsters.add(monster)
for i in range(0,3):
    monster2 = Chaos('clip.png',randint(80,win_width -80),0,randint(5,10))
    monsters2.add(monster2)
for i in range(0,1):
    monster3 = Enemy('Revenant_Image.png',randint(80,win_width -80),0,0)
    monsters3.add(monster3)
bullets = sprite.Group()
bulletsenemy = sprite.Group()
finish = True
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                player.fire()
    while finish:
        colides = sprite.groupcollide(monsters,bullets,True,True)
        for c in colides:
            score = score + 1
        window.blit(background,(0,0))
        text_lose = font1.render('пропущено: ' + str(lost),1,(255,255,255))
        text_won = font2.render('счет: ' + str(won),1,(255,255,255))
        window.blit(text_lose,(5,5))
        window.blit(text_won,(5,45))
        monsters.update()
        monsters2.update()
        player.update()
        bullets.update()
        bulletsenemy.update()
        monsters.draw(window)
        monsters2.draw(window)
        monsters3.draw(window)
        bullets.draw(window)
        bulletsenemy.draw(window)
        player.reset()
        clock.tick(FPS)
        if lost > 5:
            lose = font1.render(('демоны поработили землю'),1,(255,255,255))
            window.blit(lose,(100,250))
            finish = False
        if won >= 15:
            win = font1.render(('вы смогли отбить наподение демонов'),1,(255,255,255))
            window.blit(win,(100,250))
            finish = False
        display.update()

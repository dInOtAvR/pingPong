from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed= player_speed

        self.rect= self.image.get_rect()
        self.rect.x= player_x
        self.rect.y= player_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y<win_height-130:
            self.rect.y +=self.speed  
    

    def update_r(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<win_height-130:
            self.rect.y +=self.speed



back=(203,197,111)
win_width=600
win_height=500
window=display.set_mode((win_width,win_height))
window.fill(back)
display.set_caption('pingPong')

game=True
finish=False
clock= time.Clock()
FPS=60

racket1= Player("racket1.png", 25,200,12,120,7)
racket2= Player("racket2.png",565,200,12,120,7)
ball= GameSprite("joe-biden-40972.png",200,200,50,50,50)

speedx, speedy= 6,6
score1, score2 = 0,0

font.init()
font= font.Font(None,35)
score= font.render('0 : 0', True,(0,0,0))
lose= font.render('',True,(180,0,0))


while game:
    for e in event.get():
        if e.type== QUIT:
            game=False
    if not finish:
        window.fill(back)

        racket1.update_l()
        racket2.update_r()
        ball.rect.x  += speedx
        ball.rect.y += speedy

        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speedx *=-1

        if ball.rect.y<0 or ball.rect.y>win_height-50:
            speedy *= -1

        if ball.rect.x <0:
            score2 += 1
            ball.rect.x, ball.rect.y= 200,200
            speedx, speedy= 6,6
        
        if ball.rect.x>win_width-50:
            score1 += 1
            ball.rect.x, ball.rect.y= 200,200
            speedx, speedy= 6,6

        score= font.render(f'{score1} : {score2}',True,(0,0,0))
        window.blit(score,(285,0))
        racket1.reset()
        racket2.reset()
        ball.reset()

        if score1   >= 10:
            lose= font.render('Player 2 lost!',True,(180,0,0))
            finish=True
            window.blit(lose,(250,200))
        if score2   >= 10:
            lose= font.render('Player 1 lost!',True,(180,0,0))
            finish=True
            window.blit(lose,(250,200))
        
    else:
        finish= False
        time.delay(3000)
        ball.rect.x,ball.rect.y=200,200
        speedx,speedy=6,6
        racket1.rect.y,racket2.rect.y=200,200
        score1, score2 = 0,0
    
    display.update()
    clock.tick(FPS)

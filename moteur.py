"""import des librerie"""
import pygame
from os import path
from settings import *

vec = pygame.math.Vector2

"""creation de la classe player"""
class Player(pygame.sprite.Sprite):
    """la classe player sert à gérer les déplacements et les actions du joueur
        elle hérite de pygame.sprite.Sprite et prend comme argument la position du joueur en x , en y 
        ,son apparence sous la forme d'une chaine de caractère contenant le nom du fichier qui doit être placé dans le dossier img 
        et comme dernier argument la vie du joueur"""
    def __init__(self,posx,posy,skin,life):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(path.join(path.dirname(__file__), 'img'), skin)).convert_alpha()
        self.rect = self.image.get_rect()
        
        """creation des vecteur pour le deplasement"""
        self.pos = vec(posx, posy)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        
        """variable pour savoir ou doit se diriger le joueur"""
        self.move_D = False
        self.move_G = False
        
        """vie du joueur """
        self.life = life

    """fonction qui active le déplacement vers la gauche"""
    def move_g(self):
        self.move_G = True

    """fonction qui stoppe le déplacement vers la gauche"""
    def stop_move_g(self):
        self.move_G = False

    """fonction qui active le déplacement vers la droite"""
    def move_d(self):
        self.move_D = True

    """fonction qui stoppe le déplacement vers la droite"""
    def stop_move_d(self):
        self.move_D = False

    """fonction de saut qui se déclenche si le joueur et sur une plateforme"""
    def jump(self):
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20

    """fonction qui exécute un tir dans la direction de déplacement du joueur"""
    def shoot(self,skin):

        if self.life > 0:
            if self.vel.x >= 0:
                bullet = Bullet(self.rect.right, self.rect.centery, skin)
                bullet.speedx = 10
            elif self.vel.x < 0:
                bullet = Bullet(self.rect.left, self.rect.centery, skin)
                bullet.speedx = -10

            """on ajoute l'élément tirer dans le groupe bullets et all sprites"""
            all_sprites.add(bullet)
            bullets.add(bullet)

    """fonction l'actualisation de la position du joueur"""
    def update(self):
        """aplication d'une graviter au joueur"""
        self.acc = vec(0, GRAV)

        """le joueur accélère dans le sens de déplacement ordonné"""
        if self.move_G:
            self.acc.x = -PLAYER_ACC
        if self.move_D:
            self.acc.x = PLAYER_ACC

        """"application de l'équation de friction"""
        self.acc.x += self.vel.x * PLAYER_FRICTION

        """"application de l'équation de mouvement"""
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        """empêche le joueur de sortir l'écran sur x"""
        if self.pos.x > WIDTH :
            self.pos.x = WIDTH 
        if self.pos.x < 0:
            self.pos.x = 0

        self.rect.midbottom = self.pos


########################################################################################################################################

class Mobf(pygame.sprite.Sprite):
    """la classe Mobf sert à gérer les déplacements et les actions du monstre final
        elle hérite de pygame.sprite.Sprite et prend comme argument la position du Mostre en x , en y 
        ,son apparence sous la forme d'une chaine de caractère contenant le nom du fichier qui doit être placé dans le dossier img 
        ,la vie du monstre et sa cible. la différence avec la clase mob et que celle ci peut tirer des projectil """
    def __init__(self,posx,posy,skin,life,target):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(path.join(path.dirname(__file__), 'img'), skin)).convert_alpha()
        self.rect = self.image.get_rect()

        """creation des vecteur pour le deplasement"""
        self.pos = vec(posx,posy)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        """vie du monstre """
        self.life = life

        """cible du monstre"""
        self.target = target

    """fonction qui exécute un tir dans la direction de déplacement du monstre"""
    def shoot(self,skin):

        if self.life > 0:
            if self.vel.x >= 0:
                bullet = Bullet(self.rect.right, self.rect.centery, skin)
                bullet.speedx = 10
            elif self.vel.x < 0:
                bullet = Bullet(self.rect.left, self.rect.centery, skin)
                bullet.speedx = -10

            """on ajoute l'élément tirer dans le groupe bullets et all sprites"""
            all_sprites.add(bullet)
            bullets.add(bullet)

    """fonction l'actualisation de la position du monstre"""
    def update(self):
        """aplication d'une graviter au monstre"""
        self.acc = vec(0, GRAV)

        """le monstre accélère dans le sens ou se trouve ca cible"""
        if self.pos.x > self.target.pos.x:
            self.acc.x = -MOBF_ACC
        if self.pos.x < self.target.pos.x:
            self.acc.x = MOBF_ACC

        """"application de l'équation de friction"""
        self.acc.x += self.vel.x * PLAYER_FRICTION

        """"application de l'équation de mouvement"""
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        """empêche le monstre de sortir l'écran sur x"""
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0

        """tue le monstre s'il sort de l'écran sur y positif"""
        if self.pos.y > HEIGHT :
            self.kill()

        self.rect.midbottom = self.pos

########################################################################################################################################

class Mob(pygame.sprite.Sprite):
    """la classe Mobf sert à gérer les déplacements et les actions du monstre final
        elle hérite de pygame.sprite.Sprite et prend comme argument la position du Mostre en x , en y 
        ,son apparence sous la forme d'une chaine de caractère contenant le nom du fichier qui doit être placé dans le dossier img 
        ,la vie du monstre et sa cible"""
    def __init__(self,posx,posy,skin,life,target):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(path.join(path.dirname(__file__), 'img'), skin)).convert_alpha()
        self.rect = self.image.get_rect()
        
        """creation des vecteur pour le deplasement"""
        self.pos = vec(posx, posy)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        
        """vie du monstre """
        self.life = life
        
        """cible du monstre"""
        self.target = target

    """fonction l'actualisation de la position du monstre"""
    def update(self):
        """aplication d'une graviter au monstre"""
        self.acc = vec(0, GRAV)

        if self.pos.x > self.target.pos.x:
            self.acc.x = -MOB_ACC
        if self.pos.x < self.target.pos.x:
            self.acc.x = MOB_ACC

        """"application de l'équation de friction"""
        self.acc.x += self.vel.x * PLAYER_FRICTION

        """"application de l'équation de mouvement"""
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        """empêche le monstre de sortir l'écran sur x"""
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0

        """tue le monstre s'il sort de l'écran sur y positif"""
        if self.pos.y > HEIGHT :
            self.kill()

        self.rect.midbottom = self.pos


class Bullet(pygame.sprite.Sprite):
    """la class Bullet sert a créé des projectiles
        elle hérite de pygame.sprite.Sprite et p)rend comme argument la position d’apparition en x et y 
        et son apparence sous la forme d'une chaine de caractère contenant le nom du fichier qui doit être placé dans le dossier img"""

    def __init__(self, x, y, skin):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(path.join(path.dirname(__file__), 'img'), skin)).convert_alpha()
        self.image.set_alpha()
        self.rect = self.image.get_rect()

        """Positionnement du projectile """
        self.rect.bottom = y
        self.rect.centerx = x

    """fonction l'actualisation de la position du projectile"""
    def update(self):
        """"application de l'équation de mouvement"""
        self.rect.x += self.speedx

        """supprime le projectile si il sort de l’encrant"""
        if self.rect.x < 0:
            self.kill()

        if self.rect.x > WIDTH:
            self.kill()

        if self.rect.y < 0:
            self.kill()

        if self.rect.y > HEIGHT:
            self.kill()


class Platform(pygame.sprite.Sprite):
    """la class Platform sert a créé des plateformes
    elle hérite de pygame.sprite.Sprite et p)rend comme argument la position d’apparition en x et y 
    et son apparence sous la forme d'une chaine de caractère contenant le nom du fichier qui doit être placé dans le dossier img"""
    def __init__(self, x, y, skin):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(path.join(path.dirname(__file__), 'img'), skin)).convert_alpha()
        self.rect = self.image.get_rect()
        """positionnement de la plateforme""" 
        self.rect.x = x
        self.rect.y = y

class Level_builder():
    """la class Level_builder sert a construire le nivaux a partir d’un fichier texte
        elle prend pour argument le non du fichier texte qui doit se trouver dans le dossier level sous forme de chaine de caractère 
        et les différant apparence des plateforme sous la forme d'une chaine de caractère contenant le nom du fichier 
        qui doit être placé dans le dossier img"""  

    def __init__(self, level, skin_w, skin_p, skin_d):
        self.image_W = skin_w
        self.image_P = skin_p
        self.image_D = skin_d

        self.x = 0
        self.y = -4200

        """ouverture du fichier texte et enregistrement dans un tableaux"""
        self.map_data = []
        with open(path.join(path.join(path.dirname(__file__), 'level'), level), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    """fonction qui lie le tableau et place les différant plateforme"""
    def build_level(self):
        for row in self.map_data:
            for col in row:

                if col == "W":
                    w = Platform(self.x, self.y, self.image_P)
                    all_sprites.add(w)
                    walls.add(w)

                if col == "P":
                    p = Platform(self.x, self.y, self.image_P)
                    all_sprites.add(p)
                    platforms.add(p)

                if col == "D":
                    d = Platform(self.x, self.y-20, self.image_D)
                    p = Platform(self.x, self.y, self.image_P)
                    all_sprites.add(d)
                    all_sprites.add(p)
                    traps.add(d)
                    platforms.add(p)

                self.x += 50
            self.x = 0
            self.y += 40

"""fonction qui regarde si un projectile rentre en contact avec une entité""" 
def damage_bullets(entity):
    """enlevé 1 point de vie a l’entité par contact avec le projectile et supprime le projectile"""
    touch_bullets = pygame.sprite.spritecollide(entity, bullets, False)
    if touch_bullets:
        entity.life -= 1
        touch_bullets[0].kill()

    """tue l’ entité si sa vie et inferieur ou égale a 0"""
    if entity.life <= 0:
        entity.kill()

"""fonction qui regarde si un monstre rentre en contact avec une entité"""
def damage_mobs(entity):
    """enlevé 1 point de vie a l’entité par contact avec le monstre"""
    touch_mobs = pygame.sprite.spritecollide(entity, mobs, False)
    if touch_mobs:
        entity.life -= 1

    """tue l’ entité si sa vie et inferieur ou égale a 0"""
    if entity.life <= 0:
        entity.kill()

"""fonction qui regarde si un piège rentre en contact avec une entité"""
def damage_traps(entity):
    """enlevé 1 point de vie a l’entité par contact avec le piège"""
    touch_traps = pygame.sprite.spritecollide(entity, traps, False)
    if touch_traps:
        entity.life -= 1

    """tue l’ entité si sa vie et inferieur ou égale a 0"""
    if entity.life <= 0:
        entity.kill()

"""fonction qui gère la collision entre une entité et les plateformes"""
def colision_plat(entity):
    if entity.vel.y > 0:
        """ si l’entier rentre en contacte avec une plateforme ca position et égale a la position supérieur de cette plateforme"""
        hits = pygame.sprite.spritecollide(entity, platforms, False)
        if hits:
            entity.pos.y = hits[0].rect.top
            entity.vel.y = 0

"""fonction qui gère la collision entre une entité et les murs"""
def colision_wall(entity):
    if entity.vel.x < 0:
        hits = pygame.sprite.spritecollide(entity, walls, False)
        if hits:
            entity.pos.x = hits[0].rect.right + (entity.rect.w/2)
            entity.vel.x = 0

    if entity.vel.x > 0:
        hits = pygame.sprite.spritecollide(entity, walls, False)
        if hits:
            entity.pos.x = hits[0].rect.left - (entity.rect.w/2)
            entity.vel.x = 0


"""création de groupe pour regrouper les sprite"""
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
walls = pygame.sprite.Group()
traps = pygame.sprite.Group()
bullets = pygame.sprite.Group()
mobs = pygame.sprite.Group()
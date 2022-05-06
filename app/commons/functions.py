import pygame

def drawImage(window, src, height, width, left, top, defaultBackgroundColor = (255, 255, 255)):
    img = pygame.image.load(src)
    img.convert()
    el = img.get_rect()
    el.height = height
    el.width = width
    el.left = left
    el.top = top
    window.blit(img, el)
    pygame.draw.rect(window, defaultBackgroundColor, el, 1)


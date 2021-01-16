
import sys
import pygame



def showEndGameInterface(screen, exitcode, accuracy, game_images):
    font = pygame.font.Font(None, 24)
    text = font.render(f"Accuracy: {accuracy}%", True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery + 24
    while True:
        screen.fill(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if exitcode:
            screen.blit(game_images['youwin'], (0, 0))
        else:
            screen.blit(game_images['gameover'], (0, 0))
        screen.blit(text, text_rect)
        pygame.display.flip()

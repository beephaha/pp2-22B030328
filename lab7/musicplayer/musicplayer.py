import pygame

# initialize Pygame
pygame.init()

# set up screen and font
screen = pygame.display.set_mode((800, 200))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 36)

# set up music list and current index
music_list = [r"lab8/musicplayer/songs/kayrat-nurtas-ol-sen-emes.mp3"]
current_index = 0

# set up player and controller
pygame.mixer.init()
pygame.mixer.music.load(music_list[current_index])
playing = False

# draw initial screen
screen.fill((255, 255, 255))
text = font.render("Press SPACE to play/pause, LEFT/RIGHT to change the song", True, (0, 0, 0))
screen.blit(text, (20, 20))
pygame.display.update()

# main game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # toggle play/pause
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            elif event.key == pygame.K_LEFT:
                # go to previous song
                current_index -= 1
                if current_index < 0:
                    current_index = len(music_list) - 1
                pygame.mixer.music.load(music_list[current_index])
                pygame.mixer.music.play()
                playing = True
            elif event.key == pygame.K_RIGHT:
                # go to next song
                current_index += 1
                if current_index >= len(music_list):
                    current_index = 0
                pygame.mixer.music.load(music_list[current_index])
                pygame.mixer.music.play()
                playing = True

    # update screen
    screen.fill((255, 255, 255))
    text = font.render("Press SPACE to play/pause, LEFT/RIGHT to skip", True, (0, 0, 0))
    screen.blit(text, (20, 20))
    pygame.display.update()
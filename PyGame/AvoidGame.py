import random
import pygame
# 기본 초기화 (반드시 해야 할 부분)
pygame.init()

# 화면 크기 설정
Screen_width = 320  # 가로 크기
Screen_height = 480  # 세로 크기
Screen = pygame.display.set_mode((Screen_width, Screen_height))

pygame.display.set_caption("Avoid Game")  # 개임 타이틀 설정 게임 이름

# FPS
clock = pygame.time.Clock()

#########################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)

background = pygame.image.load(
    "/Users/jiseungmin/Desktop/PythonProJect/PyGame/background.png")
charaters = pygame.image.load(
    "/Users/jiseungmin/Desktop/PythonProJect/PyGame/character.png")
avoidchar = pygame.image.load(
    "/Users/jiseungmin/Desktop/PythonProJect/PyGame/balloon2.png")

# 케릭터
charaters_size = charaters.get_rect().size
charaters_width = charaters_size[0]
charaters_height = charaters_size[1]
charcter_xpos = (Screen_width/2) - (charaters_width/2)
charcter_ypos = Screen_height - charaters_height
charaters_speed = 1

# 피해야 하는 케릭터
avoidchar_size = avoidchar.get_rect().size
avoidchar_width = avoidchar_size[0]
avoidchar_height = avoidchar_size[1]
avoidchar_xpos = random.randint(0, Screen_width - avoidchar_width)
avoidchar_ypos = 0
avoidchar_speed = 10

x_pos = 0
y_pos = 0

game_font = pygame.font.Font(None, 40)
total_time = 30
start_ticks = pygame.time.get_ticks()
#########################################################################################

running = True  # 게임이 진행 중인가?
while running:
    dt = clock.tick(30)  # FPS

    # 2. 이벤트 처리 (키보드 , 마우스 등)
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 생기는가?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                x_pos -= charaters_speed
            elif event.key == pygame.K_RIGHT:
                x_pos += charaters_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_pos = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_pos = 0

    # 3. 게임 캐릭터 위치 정의
    charcter_xpos += x_pos * dt

    if charcter_xpos < 0:
        charcter_xpos = 0
    elif charcter_xpos > Screen_width - charaters_width:
        charcter_xpos = Screen_width - charaters_width

    if avoidchar_ypos > Screen_height:
        avoidchar_ypos -= 1

    avoidchar_ypos += avoidchar_speed
    if avoidchar_ypos > Screen_height:
        avoidchar_ypos = 0
        avoidchar_xpos = random.randint(0, Screen_width-avoidchar_width)

    # 4. 충돌 처리
    charcter_rect = charaters.get_rect()
    charcter_rect.left = charcter_xpos
    charcter_rect.top = charcter_ypos

    enemy_rect = avoidchar.get_rect()
    enemy_rect.left = avoidchar_xpos
    enemy_rect.top = avoidchar_ypos

  # 충돌 체크
    if charcter_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기
    Screen.blit(background, (0, 0))  # 배경 그리기
    Screen.blit(charaters, (charcter_xpos, charcter_ypos))  # 케릭터 그리기
    Screen.blit(avoidchar, (avoidchar_xpos, avoidchar_ypos))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(
        str(int(total_time - elapsed_time)), True, (255, 255, 255))
    Screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update()  # 게임 화면 다시그리기

pygame.quit()

import pygame
#########################################################################################
# 기본 초기화 (반드시 해야 할 부분)
pygame.init()

# 화면 크기 설정
Screen_width = 640  # 가로 크기
Screen_height = 320  # 세로 크기
Screen = pygame.display.set_mode((Screen_width, Screen_height))

pygame.display.set_caption("SeungminGame")  # 개임 타이틀 설정 게임 이름

# FPS
clock = pygame.time.Clock()

#########################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)

background = pygame.image.load(
    "/Users/jiseungmin/Desktop/PythonProJect/PyGame/background.png")  # 이미지 불러우기

# 캐릭터 가져오기
charcter = pygame.image.load(
    "/Users/jiseungmin/Desktop/PythonProJect/PyGame/character.png")
charcter_size = charcter.get_rect().size
charcter_width = charcter_size[0]  # 이미지 가로크기
charcter_height = charcter_size[1]  # 이미지 세로크기
charcter_xpos = (Screen_width/2) - (charcter_width/2)  # 케릭터 x 좌표
charcter_ypos = Screen_height - charcter_height  # 케릭터 y 좌표

x_topos = 0
y_topos = 0

# 케릭터 이동속도
charcter_speed = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load(
    "/Users/jiseungmin/Desktop/PythonProJect/PyGame/balloon2.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]  # 이미지 가로크기
enemy_height = enemy_size[1]  # 이미지 세로크기
enemy_xpos = (Screen_width/2) - (enemy_width/2)  # 케릭터 x 좌표
enemy_ypos = (Screen_height/2) - (enemy_height/2)  # 케릭터 y 좌표

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()

#########################################################################################

running = True  # 게임이 진행 중인가?
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 생기는가?
            running = False  # 게임이 진행중이 아님

    if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
        if event.key == pygame.K_LEFT:
            x_topos -= charcter_speed
        elif event.key == pygame.K_RIGHT:
            x_topos += charcter_speed
        elif event.key == pygame.K_UP:
            y_topos -= charcter_speed
        elif event.key == pygame.K_DOWN:
            y_topos += charcter_speed

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_topos = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            y_topos = 0

    charcter_xpos += x_topos * dt
    charcter_ypos += y_topos * dt

  # 가로 경계면 제한
    if charcter_xpos < 0:
        charcter_xpos = 0
    elif charcter_xpos > Screen_width - charcter_width:
        charcter_xpos = Screen_width - charcter_width

  # 세로 경계면 제한
    if charcter_ypos < 0:
        charcter_ypos = 0
    elif charcter_ypos > Screen_height - charcter_height:
        charcter_ypos = Screen_height - charcter_height

  # 충돌 처리를 위한 rect 정보 업데이트
    charcter_rect = charcter.get_rect()
    charcter_rect.left = charcter_xpos
    charcter_rect.top = charcter_ypos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_xpos
    enemy_rect.top = enemy_ypos

  # 충돌 체크
    if charcter_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    Screen.blit(background, (0, 0))  # 배경 그리기
    Screen.blit(charcter, (charcter_xpos, charcter_ypos))  # 케릭터 그리기
    Screen.blit(enemy, (enemy_xpos, enemy_ypos))  # 적 그리기

    # 타이머 집어넣기
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(
        str(int(total_time - elapsed_time)), True, (255, 255, 255))
    Screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update()  # 게임 화면 다시그리기


# 잠시 대기
pygame.time.delay(2000)

pygame.quit()

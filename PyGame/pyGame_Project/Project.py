# 나중에 게임을 만들때 프레임을 쓸려고 사용 하기 위한 파일임
from cgitb import small
import pygame
import os
#########################################################################################
# 기본 초기화 (반드시 해야 할 부분)
pygame.init()

# 화면 크기 설정
Screen_width = 520  # 가로 크기
Screen_height = 520  # 세로 크기
Screen = pygame.display.set_mode((Screen_width, Screen_height))

pygame.display.set_caption("Pang")  # 개임 타이틀 설정 게임 이름

# FPS
clock = pygame.time.Clock()

#########################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 케릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xpos = (Screen_width/2) - (character_width/2)
character_ypos = Screen_height - character_height - stage_height

# 캐릭터 이동방향
character_to_x = 0
# 캐릭터 스피드
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한번에 여러발 발사 가능
weapons = []

# 무기 이동속도
weapon_speed = 10

# 공 만들기
ball_image = [pygame.image.load(os.path.join(image_path, "balloon1.png")),
              pygame.image.load(os.path.join(image_path, "balloon2.png")),
              pygame.image.load(os.path.join(image_path, "balloon3.png")),
              pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# 공 크기에 따른 최초 스피드
balls_speed_y = [-18, -15, -12, -9]

# 공들
balls = []

# 최초 발생하는 큰 공
balls.append({
    "pos_x": 50,
    "pos_y": 50,
    "img_idx": 0,
    "to_x": 3,
    "to_y": -6,
    "init_spd_y": balls_speed_y[0]})

# 사라질 무기, 총
weapon_to_remove = -1
ball_to_remove = -1

# Font 정의
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks()  # 시작 시간 정의

gmae_result = "GAME OVER"  # 게임 메세지
#########################################################################################

running = True  # 게임이 진행 중인가?
while running:
    dt = clock.tick(60)  # FPS

    # 2. 이벤트 처리 (키보드 , 마우스 등)
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 생기는가?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_xpos + \
                    (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_ypos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_xpos += character_to_x

    if character_xpos < 0:
        character_xpos = 0
    elif character_xpos > Screen_width - character_width:
        character_xpos = Screen_width - character_width

    #  무기 위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]
    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_image[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로벽에 닿았을 때 공 이동 위치 변경 (튕겨나오는 효과)
        if ball_pos_x < 0 or ball_pos_x > Screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        if ball_pos_y >= Screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4. 충돌 처리

    # 캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_xpos
    character_rect.top = character_ypos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # 공 Rect 정보 업데이트
        ball_rect = ball_image[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        if character_rect.colliderect(ball_rect):
            running = False
            break

        # 공과 무기들 충돌처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # 무기 rect 정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            # 충돌 체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx
                ball_to_remove = ball_idx

               # 가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나눠주기
                if ball_img_idx < 3:

                   # 현재 공 크기 정보를 가지고 옴
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

               # 나눠진 공 정보
                    small_ball_rect = ball_image[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    # 왼쪽으로 튕겨나가는 공
                    balls.append({
                        "pos_x": ball_pos_x + (ball_width/2) - (small_ball_width/2),
                        "pos_y": ball_pos_y + (ball_height/2) - (small_ball_height/2),
                        "img_idx": ball_img_idx + 1,
                        "to_x": -3,
                        "to_y": -6,
                        "init_spd_y": balls_speed_y[ball_img_idx + 1]})

                # 오른쪽으로 튕겨나가는 공
                    balls.append({
                        "pos_x": ball_pos_x + (ball_width/2) - (small_ball_width/2),
                        "pos_y": ball_pos_y + (ball_height/2) - (small_ball_height/2),
                        "img_idx": ball_img_idx + 1,
                        "to_x": 3,
                        "to_y": -6,
                        "init_spd_y": balls_speed_y[ball_img_idx + 1]})
                break
        else:  # 계속 게임 진행
            continue  # 안쪽 for 문 조건이 맞지 않으면 contiune, 바깥 for문 계속 실행
        break  # 안쪽 for문에서 break를 만나면 여기로 진입가능 2중 for문을 한번에 탈출

    # 충돌된 공 or 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 모든 공을 없앤 경우 게임 종료(성공)
    if len(balls) == 0:
        gmae_result = "Misson Complete"
        running = False

    # 5. 화면에 그리기
    Screen.blit(background, (0, 0))
    for weapon_x_pos, weapon_y_pos in weapons:
        Screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        Screen.blit(ball_image[ball_img_idx], (ball_pos_x, ball_pos_y))

    Screen.blit(stage, (0, Screen_height - stage_height))
    Screen.blit(character, (character_xpos, character_ypos))

    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render("Time : {}".format(
        int(total_time - elapsed_time)), True, (255, 255, 255))
    Screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False

    pygame.display.update()  # 게임 화면 다시그리기

msg = game_font.render(gmae_result, True, (255, 255, 0))  # 노란색
msg_rect = msg.get_rect(center=(int(Screen_width/2), int(Screen_height/2)))
Screen.blit(msg, msg_rect)
pygame.display.update()

# 2초 대기
pygame.time.delay(2000)

pygame.quit()

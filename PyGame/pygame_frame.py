# 나중에 게임을 만들때 프레임을 쓸려고 사용 하기 위한 파일임
import pygame
#########################################################################################
# 기본 초기화 (반드시 해야 할 부분)
pygame.init()

# 화면 크기 설정
Screen_width = 640  # 가로 크기
Screen_height = 320  # 세로 크기
Screen = pygame.display.set_mode((Screen_width, Screen_height))

pygame.display.set_caption("게임 이름")  # 개임 타이틀 설정 게임 이름

# FPS
clock = pygame.time.Clock()

#########################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)

#########################################################################################

running = True  # 게임이 진행 중인가?
while running:
    dt = clock.tick(60)  # FPS

    # 2. 이벤트 처리 (키보드 , 마우스 등)
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 생기는가?
            running = False  # 게임이 진행중이 아님
    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update()  # 게임 화면 다시그리기

pygame.quit()

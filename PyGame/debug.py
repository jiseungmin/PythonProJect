balls = [1, 2, 3, 4, 5]
weapons = [33, 4214, 231, 3]

for ball_idx, ball_val in enumerate(balls):
    print("ball:", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapon :", weapon_val)
        if ball_val == weapon_val:
            print("공과 무기 충돌")
            break
    else:
        continue
    break

# 이중 for 문 브레이크

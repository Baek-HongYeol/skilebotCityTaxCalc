from sys import exit


def check_quit(c):
    command = ['q', 'quit']
    if c in command:
        return True
    else:
        return False


def check_buildings(buildings):
    if len(buildings) != 7:
        return False
    building_C = ['a','b','c','d','e','f','g','h','i','j','k','l','m','x']
    for i, c in enumerate(buildings):
        if c not in building_C:
            return False
        elif c == 'j' and (i != 0 or i != 6):
            print("항구는 맨 끝 칸에 배치하세요. ", end='')
            return False
    return True

def reset():
    init_message()
    return loop()

def init_message():
    print("")
    print("슷칼봇 도시의 집세 계산 프로그램입니다.")
    print("프로그램을 종료하시려면 q를 리셋하려면 r을 입력하세요")

def price_input():
    # return (0, 0)
    inputlist = ['q', 'quit', 'r']
    green = input("그린건설 주가 입력 : ")
    green = green.lower()
    while (not green.isdecimal()) and green not in inputlist:
        print("주가는 자연수여야 합니다.")
        green = input("그린건설 주가 재입력 : ")
        green = green.lower()
    if green in inputlist:
        return green, 0

    lus = input("러스관광 주가 입력 : ")
    lus = lus.lower()
    while (not lus.isdecimal()) and lus not in inputlist:
        print("주가는 자연수여야 합니다.")
        lus = input("러스관광 주가 재입력 : ")
        lus = lus.lower()
    if lus in inputlist:
        return lus, 0
    return green, lus


def weekend_input():
    weekend = ['y', 'n', 'yes', 'no', 'q', 'quit', 'r']
    print("산출일이 주말인지 입력하세요.")
    weekinput = input("맞다면 yes 아니면 no (y/n): ")
    weekinput = weekinput.lower()
    while weekinput not in weekend:
        print("다시 입력해주세요.")
        weekinput = input("주말이면 yes 아니면 no (y/n): ")
        weekinput = weekinput.lower()
    if check_quit(weekinput):
        return weekinput
    elif weekinput == 'r':
        return weekinput
    elif weekinput == 'y' or weekinput == 'yes':
        weekinput = input("일요일이면 yes 토요일이면 no (y/n): ")
        weekinput = weekinput.lower()
        while weekinput not in weekend:
            print("다시 입력해주세요.")
            weekinput = input("일요일이면 yes 토요일이면 no (y/n): ")
            weekinput = weekinput.lower()
        if check_quit(weekinput):
            return weekinput
        elif weekinput == 'r':
            return weekinput
    else:
        return '0'
    if weekinput == 'y' or weekinput == 'yes':
        return '2'
    elif weekinput == 'n' or weekinput == 'no':
        return '1'


def loop():
    more = True
    while more:
        print("")
        init_message()
        (green, lus) = price_input()
        if check_quit(green):
            return
        elif green == 'r':
            return reset()

        weekinput = weekend_input()
        if check_quit(green):
            return
        elif green == 'r':
            return reset()

        print("")
        print("공터=x, 주택=a, 편의점=b, 학교=c, 회사=d")
        print("병원=e, 은행=f, 백화점-g, 호텔=h, 카지노=i")
        print("항구=j, 경기장=k, 교회=l, 공장=m")
        buildings = input("배열할 건물을 띄어쓰기 없이 7자리 적으세요: ")
        buildings = buildings.lower()
        if check_quit(buildings):
            return
        elif buildings == 'r':
            init_message()
            continue
        while not check_buildings(buildings):
            print("잘못 입력되었습니다.")
            buildings = input("건물 배열 재입력: ")
            buildings = buildings.lower()
            if check_quit(buildings):
                return
            elif buildings == 'r':
                break
        if buildings == 'r':
            init_message()
            continue

        b_index = ['x', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
        multiples = [1, 1, 1, 1, 1, 1, 1]
        coefficient = (('공터', 1, (1, 0, 0.5)),
                       ('주택', 0), ('편의점', 2, (2, 2, 1, 3, 4), (3, 1, 2, 0.7)), ('학교', 2, (4, 1, 1, 3), (2, 1, 8, 0.5)),
                       ('회사', 1, (3, 10, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 2)), ('병원', 1, (0, 0, 1.5)),
                       ('은행', 1, (1, 1, 5, 5)),
                       ('백화점', 2, (1, 0, 3, 5), (0, 1, 2, 0)),
                       ('호텔', 2, (0, 9, 2, 4, 5, 6, 7, 10, 11, 12, 13, 2), (0, 1, 1, 0.5)),
                       ('카지노', 3, (2, 1, 1, 0.5), (0, 1, 9, 0.5), (1, 1, 8, 2)), ('항구', 1, (0, 3, 8, 9, 10, 3)),
                       ('경기장', 1, (2, 0, 0.2)), ('교회', 1, [2, 2, 1, 4, 1.5]), ('공장', 1, (3, 0, 0)))
        # ('건물이름', 효과 개수, (place, 건물종류개수, 종류,.. , 효과)..)
        # 효과 개수 == 0, nothing
        # place == 0, 전범위,
        # 건물종류개수 == 0, 모든 건물, 종류X

        if weekinput == '2':
            coefficient[12][2][4] = 5

        for i, b in enumerate(buildings):
            index = b_index.index(b)
            coef = coefficient[index]
            if b == 'k' and weekinput == '1':
                multiples[i] = multiples[i]*4
            for a in range(0, coef[1]):
                effect = coef[2+a]
                for ef_idx in range(0,7):
                    if ef_idx == i:
                        continue
                    elif abs(ef_idx-i) <= effect[0] or effect[0] == 0:
                        ef_build = []
                        for tempi in range(effect[1]):
                            ef_build.append(b_index[effect[2+tempi]])
                        if len(ef_build) == 0:
                            ef_build = b_index[:]
                        if buildings[ef_idx] in ef_build:
                            multiples[ef_idx] = multiples[ef_idx]*effect[-1]
        print('')
        names = "건물:"
        taxes = "집세:"
        b_tax = (0, 1, 2, 4, 6, 10, 20, 25, 30, 50, 15, 15, 0, 0)
        for b in buildings:
            names = names + ' %s' % coefficient[b_index.index(b)][0]
            taxes = taxes + ' %d,' % b_tax[b_index.index(b)]
        print(names)
        print(taxes[:-1])
        multiprint = list(map(lambda k: int(k) if int(k) == k else float("%.3f" % k), multiples))
        print('계수:', multiprint)
        result = 0
        for i, a in enumerate(buildings):
            index = b_index.index(a)
            if a == 'i':
                result = result + int(multiples[i] * b_tax[index] * int(lus))
            else:
                result = result + int(multiples[i] * b_tax[index] * int(green))

        print('총 집세 : ', result, '슷', sep='')
        qinput = input("계속하시려면 r, 종료하시려면 q를 누르세요. ")
        qinput = qinput.lower()
        inputlist = ['q', 'quit', 'r', 'reset']
        while qinput not in inputlist:
            print("다시 입력해주세요. ", end='')
            qinput = input()
            qinput = qinput.lower()
            if check_quit(qinput):
                return
            elif qinput == 'r':
                break

        if qinput == 'r':
            continue
        more = False


loop()
wait = input('Press <ENTER> to close this program')

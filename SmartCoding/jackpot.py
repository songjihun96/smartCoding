import random
import os
import time
def account(id):
    with open('login.txt', 'r') as f:
        temp = list(f.read().split(';'))
        for i in temp:
            if i == '' or i == '\n':
                temp.remove(i)
            else:
                continue
        f.close
    for i in temp:
        tt = list(i.split(':'))
        if id == tt[0]:
            return tt
    return 0
def account_set(id, player_m):
    t = id + ":" + str(player_m) + ';\n'
    print(t)
    with open('login.txt', 'w') as f:
        f.write(t+'\n')
        f.close()
    return 0
def jackpot():
    arr = [2, 3, 4, 5]
    num = random.choice(arr)
    return num

def check(com, n):
    if com > n:
        return "up"
    else:
        return "down"
nn = 1
while nn:
    oo = int(input("이미 회원이시면 1, 아니면 0을 입력해주세요. : "))
    if oo == 1:
        id = input("아이디를 입력해주세요 : ")
        yt = account(id)
        if yt != 0:
            print(f"환영합니다! {id}님!!")
            id = yt[0]
            player_money = int(yt[1])
            life = 5
            cnt = 1
            nn = 0
        else:
            ff = open('id_idx.txt', 'r')
            id = str(int(ff.readline()) + 1)
            ff.close()
            os.remove('id_idx.txt')
            ff = open('id_idx.txt', 'w')
            ff.write(id)
            ff.close()
            print(f"이제부터 플레이어님의 id는 {id} 입니다.")
            player_money = 100000
            account_set(id, player_money)
            life = 5
            cnt = 1
            nn = 0
    else:
        ff = open('id_idx.txt', 'r')
        id = str(int(ff.readline()) + 1)
        ff.close()
        os.remove('id_idx.txt')
        ff = open('id_idx.txt', 'w')
        ff.write(id)
        ff.close()
        print(f"이제부터 플레이어님의 id는 {id} 입니다.")
        player_money = 100000
        account_set(id, player_money)
        life = 5
        cnt = 1
        nn = 0

cho = True
while player_money > 10000 or cho == True:
    print("1 [배팅 할 돈]을 입력하면 게임 시작, 0 0을 입력하면 게임 종료 입니다. 배팅 후 정답 제출 기회는 총 5번 입니다.")
    print(f"현재 보유 금액 : {player_money}")
    if life == 0:
        player_money -= batting_money
        life = 5
    opt, batting_money = map(int, input().split(' '))
    if opt == 0:
        print("게임종료")
        break
    elif batting_money <= 0:
        print(f"배팅한 돈이 {batting_money}원입니다. 10000원 이상으로 입력해주세요.")
        continue
    else:
        com = random.randint(1, 11)
        while life > 0:
            me = int(input(f"1~10 사이의 숫자중 하나를 입력하세요! 남은 기회 : {life}, 그만 하시려면 -1을 입력하세요 : "))
            if me == com:
                nu = jackpot()
                get_money = batting_money * nu
                player_money += get_money
                print(f"정답입니다! {nu}배의 돈을 획득하셨습니다! 얻은 돈 : {get_money} 총 보유 금액 : {player_money}")
                print(f"{cnt}회 만에 맞추셨습니다.")
                life = 5
                continue
            elif me == -1:
                account_set(id, player_money)
                cho = False
                break
            else:
                life -= 1
                ss = check(com, me)
                print(f"오답입니다. 다시 선택해주세요..! {ss}")
                cnt+=1
account_set(id, player_money)
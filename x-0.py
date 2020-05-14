desk = [_ for _ in range(1,10)]


def main(desk):
    counter = 0
    win = False
    instr()
    while not win:
        draw(desk)
        if counter % 2 == 0:
            input_main("X")
        else:
            input_main("0")
        counter += 1
        if check_win(desk):
            break
        if counter >= 9:
            print("Ничья")
            break
    draw(desk)

def instr():
    print("Тут должна быть инструкция")

def draw(desk):
    print("-------------")
    for i in range(3):
        print("|", desk[i*3], "|", desk[1+(i*3)], "|", desk[2+(i*3)], "|")
        print("-------------")

def input_main(player_token):
    valid = False
    while not valid:
        move_pl = input("Ход игрока " + player_token +": ")
        try:
            move_pl = int(move_pl)
        except:
            print("Это не число!")
            continue
        if (move_pl <= 9) and (move_pl >= 1):
            if (str(desk[move_pl-1]) not in "X0"):
                desk[move_pl-1] = player_token
                valid = True
            else:
                print("Поле занято")
        else:
            print("Это не то число!")
    return



def check_win(desk):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if desk[each[0]] == desk[each[1]] == desk[each[2]]:
            print("Игрок",desk[each[0]], "выиграл партию!")
            return True
    return False

if __name__ == "__main__":
    main(desk)

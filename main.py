def print_rules():
    print('\nВас приветствует игра в крекстики-нолики! Игра, знакомая нам всем с детства!\n'
          'Первый игрок ходит крестиками, второй ходит ноликами.!\n'
          'Для ввода укажите координаты поля через пробел, например "0 1",'
          'где сначала идёт номер строки, а потом номер столбца!\n'
          'Для выхода из игры введите "выход" или "exit".\n')


def field_edit(field, edit=None):
    if field:
        if field[edit[0]][edit[1]] == -1:
            field[edit[0]][edit[1]] = edit[2]
        else:
            return False
    else:
        field = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
    field_print(field)
    return field


def field_print(field):
    print('\nИгровое поле:')
    field_line = '    0|1|2\n'
    for ind, row in enumerate(field):
        field_line += '  %d|' % ind
        for item in row:
            if item != -1:
                field_line += 'X|' if item == 0 else 'O|'
            else:
                field_line += ' |'
        field_line += '\n'
    print(field_line)


def create_players():
    first_name = input('Введите имя первого игрока: ')
    second_name = input('Введите имя второго игрока: ')
    players_info = [{'name': first_name, 'wins': 0}, {'name': second_name, 'wins': 0}]
    return players_info


def player_turn(turn_ind, players_info):
    turn_pref = {'exit': False, 'right': False, 'turn': []}
    turn_line = input('Ход игрока ' + players_info[turn_ind]['name'] + '. Введите номер поля: ')
    if turn_line not in ['выход', 'exit']:
        index = [int(x) if x.isdigit() else -1 for x in turn_line.split()]
        if len(index) == 2:
            if index[0] in [0, 1, 2] and index[1] in [0, 1, 2]:
                index.append(turn_ind)
                turn_pref['turn'] = index
                turn_pref['right'] = True
                return turn_pref
            else:
                return turn_pref
        else:
            return turn_pref
    else:
        turn_pref['exit'] = True
        return turn_pref


def win_check(game_field, turn_ind):
    winner = False
    for a in range(3):
        if game_field[a][0] == turn_ind and game_field[a][1] == turn_ind and game_field[a][2] == turn_ind:
            winner = True
        elif game_field[0][a] == turn_ind and game_field[1][a] == turn_ind and game_field[2][a] == turn_ind:
            winner = True
    if not winner:
        if game_field[0][0] == turn_ind and game_field[1][1] == turn_ind and game_field[2][2] == turn_ind:
            winner = True
        elif game_field[0][2] == turn_ind and game_field[1][1] == turn_ind and game_field[2][0] == turn_ind:
            winner = True
    return winner


def the_game():
    print_rules()
    players_info = create_players()
    game_field = field_edit(None)
    game_run = True
    turn_ind = 0
    turns_count = 0
    while game_run:
        turn_right = False
        while not turn_right:
            turn_pref = player_turn(turn_ind, players_info)
            if turn_pref['exit']:
                print('Игра окончена. Заходите ещё!')
                game_run = False
                break
            else:
                turn_right = turn_pref['right']
                if turn_right:
                    turn_field = field_edit(game_field, turn_pref['turn'])
                    if turn_field:
                        game_field = turn_field.copy()
                    else:
                        print('Это поле уже занято, выберете другое!')
                        turn_right = False
                else:
                    print('Не правильный ввод, по пробуйте снова!')
        turns_count += 1
        if turns_count >= 3:
            winner = win_check(game_field, turn_ind)
            if winner:
                players_info[turn_ind]['wins'] += 1
                print('\nИгрок ' + players_info[turn_ind]['name'] + ' победил!')
                print('Общий счёт:')
                print(players_info[0]['name'] + ' -  + %d' % players_info[0]['wins'])
                print(players_info[1]['name'] + ' -  + %d\n' % players_info[1]['wins'])
                next_round = input('Вы хотите начать новый раунд? Введите 1, если да, и 0 если игра окончена: ')
                if next_round == '1':
                    game_field = field_edit(None)
                    turn_ind = 0
                    turns_count = 0
                    print('Новый раунд!')
                else:
                    print('Игра окончена. Заходите ещё!')
                    game_run = False
            else:
                turn_ind = abs(turn_ind - 1)
        elif turns_count == 9:
            print('все поля заняты, игра окончена. Ничья!')
            next_round = input('Вы хотите начать новый раунд? Введите 1, если да, и 0 если игра окончена')
            if next_round == '1':
                game_field = field_edit(None)
                turn_ind = 0
                turns_count = 0
                print('Новый раунд!')
            else:
                print('Игра окончена. Заходите ещё!')
                game_run = False
        else:
            turn_ind = abs(turn_ind - 1)


the_game()

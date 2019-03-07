import sys


def read_input():
    with open(sys.argv[1], 'r') as f:
        contents = f.readlines()

    input_games = []
    i = contents.index('--- RH-input ---\n')
    for j in range(i + 1, contents.index('--- end RH-input ---\n')):
        input_games.append(contents[j].split('\n')[0])
    return input_games, sys.argv[2]


def convert_data(game_data):
    return [game_data[start:start+6] for start in range(0, len(game_data), 6)]


def convert_games(games_string_format):
    game_matrices = []
    for game in games_string_format:
        game_matrices.append(convert_data(game))
    return game_matrices


def print_game_comfortably(game):
    for line in game:
        print(" ".join(line))


def main():

    input_games, timer = read_input()
    converted_games = convert_games(input_games)
    print_game_comfortably(converted_games[0])


if __name__ == '__main__':
    main()
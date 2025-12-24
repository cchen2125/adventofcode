def read_data(puzzle_file):
    with open(puzzle_file, "r") as file:
        input_data = file.read().splitlines()
    
    wordsearch = [[c for c in row] for row in input_data]
    return wordsearch

def get_word_starts(word_start, wordsearch):
    word_starts = []

    for i in range(len(wordsearch)):
        for j in range(len(wordsearch)):
            if wordsearch[i][j] == word_start:
                word_starts.append((i,j))
    
    return word_starts

def find_word(word, wordsearch, x, y, direction):
    for i in range(1, len(word)):
        try:
            if x+i * direction[0] < 0 or y + i * direction[1] < 0:
                break
            if wordsearch[x+i * direction[0]][y+i * direction[1]] != word[i]:
                break
            if i == len(word) - 1:
                return 1
        except:
            break
    
    return 0

def get_word_count(word, wordsearch):
    word_count = 0
    word_starts = get_word_starts(word[0], wordsearch)

    directions = [(0,1), (0,-1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    for word_start in word_starts:
        x, y = word_start[0], word_start[1]

        for direction in directions:
            word_count += find_word(word, wordsearch, x, y, direction)
    
    return word_count

def count_x_mas(wordsearch):
    x_centers = get_word_starts('A', wordsearch)
    x_mas_count = 0

    for center in x_centers:
        x, y = center[0], center[1]
        if x > 0 and x < len(wordsearch[0]) - 1 and y > 0 and y < len(wordsearch[0]) - 1:
            if wordsearch[x-1][y-1] == 'M' and wordsearch[x+1][y-1] == 'M' and wordsearch[x-1][y+1] == 'S' and wordsearch[x+1][y+1] == 'S':
                x_mas_count += 1
            if wordsearch[x-1][y-1] == 'S' and wordsearch[x+1][y-1] == 'S' and wordsearch[x-1][y+1] == 'M' and wordsearch[x+1][y+1] == 'M':
                x_mas_count += 1
            if wordsearch[x-1][y-1] == 'M' and wordsearch[x+1][y-1] == 'S' and wordsearch[x-1][y+1] == 'M' and wordsearch[x+1][y+1] == 'S':
                x_mas_count += 1
            if wordsearch[x-1][y-1] == 'S' and wordsearch[x+1][y-1] == 'M' and wordsearch[x-1][y+1] == 'S' and wordsearch[x+1][y+1] == 'M':
                x_mas_count += 1

    return x_mas_count

def main():
    puzzle_file = 'puzzle4.txt'
    wordsearch = read_data(puzzle_file)
    word = 'XMAS'

    print("Part 1 answer:", get_word_count(word, wordsearch))
    print("Part 2 answer:", count_x_mas(wordsearch))

if __name__ == "__main__":
    main()

        
def word_search_puzzle(file_dir):
    with open(file_dir, 'r') as input_file:
        file_read = input_file.readlines()

        for row in file_read:
            print(row.strip())


if __name__ == '__main__':
    word_search_puzzle('sample.pzl')

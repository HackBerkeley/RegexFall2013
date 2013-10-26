import re

def to_mat(line, cols):
    lst_split = re.findall('.{{{cols}}}'.format(cols=cols), line)
    return "\n".join(lst_split)

def main():
    maze = open('maze.txt', 'r')

    first_line = maze.readline()[:-1]
    num_cols = len(first_line)

    rest = maze.read()
    rest = re.sub(r'\n', '', rest)
    maze.close()

    maze_line = first_line + rest

    """
    TODO: change maze_line so that you have a bunch of `x` for each blank
    that's in the path
    """
    print(to_mat(maze_line, num_cols))

if __name__ == '__main__':
    main()

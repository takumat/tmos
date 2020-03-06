import sys
import os

def get_char_dat():
    with open("hankaku.txt", "r") as f:
        with open("hankaku_dat.txt", "w") as w:
            line = f.readline()
            while line:
                line.strip()
                if len(line) == 0 or line[0] == os.linesep or line[0] == '\n':
                    pass
                elif "char" in line:
                    pass
                else:
                    w.write("0b")
                    for c in line:
                        if c == '.':
                            w.write("0")
                        elif c == '*':
                            w.write("1")
                    w.write(',\n')

                line = f.readline()

def main():
    get_char_dat()

if __name__ == '__main__':
    main()
            





import count_lines
import sys

def split_words(lines):
    for line in lines:
        for w in line.strip().split():
            yield w

def main():
    filenames = sys.argv[1:]
    lines = count_lines.read_files(filenames)       
    words = split_words(lines)
    wordcount = count_lines.count_iter (words)
    print wordcount

if __name__ == "__main__":
    main()

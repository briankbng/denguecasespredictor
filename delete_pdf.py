import os


def main():
    filepath = 'data/raw'
    for item in os.listdir(filepath):
        if 'swo' in item:
            path = os.path.join('data/raw', item)
            os.remove(path)
        else:
            continue


if __name__ == '__main__':
    main()

from converter import converter


if __name__ == '__main__':
    path = input('Enter a file path:')
    delimiter = input('Enter a delimiter:')
    converter(path, delimiter)

import hashlib


def main():
    digester = hashlib.md5()
    with open('requirements.txt', 'rb') as file_stream:
        # data = file_stream.read(1034)
        # while data:
        #     digester.update(data)
        #     data = file_stream.read(10 24)
        file_iter = iter(lambda: file_stream.read(1024), b'')
        for data in file_iter:
            digester.update(data)
        print(digester.hexdigest())


if __name__ == '__main__':
    main()

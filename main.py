from document import Document
from input_handler import InputHandler


def main():
    app = InputHandler(Document())
    app.start()


if __name__ == '__main__':
    main()

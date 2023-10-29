class Ttrf():
    pass


class Yomayo(Ttrf):
    def __init__(self, name):
        self.name = name
        self.__text = 'fsadasd'
    
    def get_text(self):
        print(f'{self.__text} - initial text')

    def set_text(self, newText):
        self.__text = newText
        print(f'{self.__text} - new text')

emae = Yomayo("Harry Johnson")
emae.get_text()
emae.set_text('Kenny Dewitt')


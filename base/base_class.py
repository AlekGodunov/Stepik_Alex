class Base():
    def __init__(self, driver):
        self.driver = driver

    def assert_word(self, word_position, result):
        value_position = word_position.text
        assert value_position == result
        print ('Проверено наименование товара')
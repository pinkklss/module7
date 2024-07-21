class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    file_name = 'test_file.txt'

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text: str = file.read().lower()

                for separator in [',', '.', '!', '?', ';', ':', '-']:
                    text = text.replace(separator, ' ')

                words = text.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        found_positions = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            if word in words:
                found_positions[file_name] = words.index(word)
            else:
                found_positions[file_name] = -1

        return found_positions

    def count(self, word):
        word_count = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            word_count[file_name] = words.count(word.lower())

        return word_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

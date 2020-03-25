from utils.helpers import validate


class Finder:
    def __init__(self, string_list):
        self.string_list = string_list

    def get_chars_repetition(self, word):
        word_analysis_dict = {}
        for char in word:
            word_analysis_dict[char] = word_analysis_dict.get(char, 0) + 1
        return word_analysis_dict

    def match(self, string):
        """

        :param string:
        :return: OperationResult contains "status, status_code and data"
        """
        result = validate(string_list=self.string_list)
        try:
            matches = list()
            if result.status:
                for str_ in self.string_list:
                    if self.get_chars_repetition(str_) == self.get_chars_repetition(string):
                        matches.append(str_)

            result.data = matches
        except Exception as e:
            print(e.__str__())
        return result

    def find(self, string):
        """

        :param string:
        :return: list of matches strings.
        """
        try:
            result = self.match(string=string)
            return result.data
        except KeyError:
            print('Word not in dictionary')
            return []

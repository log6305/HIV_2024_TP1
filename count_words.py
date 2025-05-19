class CountWords:
    def count(self, s:str) -> int:
        """       
        Args:
          s (str): The parameter `s` is a string that represents a sentence or a sequence of words.
        Returns:
          The function returns the number of words in the input string `s` that end with either "s"
        or "r".
        """
        words = 0
        last = ' '

        for char in s:
            if not char.isalpha() and (last == 's' or last == 'r'):
                words += 1
            last = char

        if last == 'r' or last == 's':
            words += 1

        return words
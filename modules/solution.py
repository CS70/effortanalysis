"""
Solution Module
---
Analyzes solutions

"""
from TexSoup import TexSoup

class SolutionModule(object):

    def __init__(self, filepath=None, filetype='tex', text=None,
        output='console', print_answers=False):
        """Initialize a solution module to begin processing

        :param str filepath: path to solution file
        :param str filetype: pdf or tex
        :param bool output: output destination
        :param list allowed_chars: list of allowed characters
        """
        assert text is not None or filepath is not None, 'SolutionModule takes either a body of text or a path to a file to analyze'
        self.filepath = filepath.strip()
        self.filetype = filetype
        self.text = text
        self.output = output
        self.print_answers = print_answers
        self.__answers = None

    @property
    def answers(self):
        """Returns answers, but runs extract if not already run"""
        if not self.__answers:
            self.extract()
        return self.__answers

    def extract(self):
        """Extracts answers from source, and stores results in answers"""
        if self.filetype == 'pdf':
            raise NotImplementedError()
        elif self.filetype == 'tex':
            if self.text:
                return self.extractFromTex(text)
            return self.extractFromTex(open(self.filepath).read())
        else:
            raise NotImplementedError()

    def extractFromTex(self, text):
        """Extract answers from the provided LaTeX source"""
        soup = TexSoup(text)
        self.__answers = list(soup.find_all('answer'))
        return self

    def __str__(self):
        """Print answers prettily"""
        num_answers = sum(len(a) for a in self.answers)
        answers = '\n'.join('='*10 + 'answer' + '='*10 + '\n' + a for a in self.answers)
        if self.print_answers:
            return 'Length: %d\n%s' % (num_answers, answers)
        return 'Length: %d' % num_answers

if __name__ == '__main__':
    solution = SolutionModule(input('Path to file:')).extract()
    print(solution)

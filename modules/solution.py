"""
Solution Module
---
Analyzes solutions

"""
class SolutionModule(object):

    def __init__(self, filepath=None, filetype='tex', text=None,
        output='console', print_answers=False,
        allowed_chars=(' ', '\n', '+', '-', '=', '(', ')', ',', ':')):
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
        self.allowed_chars = allowed_chars
        self.print_answers = print_answers
        self.__answers = None

    @property
    def answers(self):
        """Returns answers"""
        if not self.__answers:
            self.extract()
        return self.__answers


    def extract(self):
        """Extracts answers from source

        :return: list of answers
        """
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
        answers = []
        for answer in text.split('\\answer{'):
            depth, chars, removeit = 1, [], False
            for c in answer:

                # check depth
                if c == '{': depth += 1
                elif c == '}': depth -= 1
                if depth == 0: break

                # skip anything of the form \text
                if c == '\\': removeit = True
                if removeit and c in (' ', '\n'): removeit = False

                # add character only if allowed
                if (c.isalpha() or c.isnumeric() or c in self.allowed_chars) and not removeit:
                    chars.append(c)

            answers.append(''.join(chars).strip())
        self.__answers = answers[1:]
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

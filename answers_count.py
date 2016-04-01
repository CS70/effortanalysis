#############
# CONSTANTS #
#############

FILEPATH = 'mt1-body.tex'
PRINT_ANSWERS = False
PRINT_START = 0
PRINT_END = 10
ALLOWED_CHARS = {' ', '\n', '+', '-', '=', '(', ')', ',', ':'}

########
# CODE #
########

def extract_answers_from_file(path):
    """Extract answers from the provided file"""
    return extract_answers_from_text(open(path).read())

def extract_answers_from_text(text):
    """Extract answers from the provided text"""
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
            if (c.isalpha() or c.isnumeric() or c in ALLOWED_CHARS) and not removeit:
                chars.append(c)

        answers.append(''.join(chars).strip())
    return answers[1:]

def print_answers(answers):
    """Print answers prettily"""
    for i in range(PRINT_START, PRINT_END):
        print('='*10, 'answer', '='*10)
        print(answers[i])

if __name__ == '__main__':
    answers = extract_answers_from_file(FILEPATH)
    print('Length:', sum(len(a) for a in answers))
    if PRINT_ANSWERS:
        print_answers(answers)

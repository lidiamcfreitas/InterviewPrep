import json

formula_tree = json.load(open("/Users/Turing/Dropbox/Git/InterviewPrep/Train/Beekeeper/input.json", "r+"))


def evaluate(formula):
    if not isinstance(formula, dict):
        return formula
    else:
        for k, v in formula.items():
            if k == '+':
                return evaluate(v[0]) + evaluate(v[1])
            if k == '*':
                return evaluate(v[0]) * evaluate(v[1])


def f(k):
    if k == '+':
        return lambda x, y: x + y
    elif k == '*':
        return lambda x, y: x * y


def evaluate2(formula):
    if not isinstance(formula, dict):
        return formula
    else:
        for k, v in formula.items():
            return f(k)(evaluate2(v[0]), evaluate2(v[1]))


print(evaluate2(formula_tree))

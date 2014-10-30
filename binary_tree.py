from itertools import chain
from random import randint


def leaf(t):
    return isinstance(t, str)

def random(n):
    def extend(t):
        if leaf(t):
            return (t+'l', t+'r')
        else:
            l, r = t
            if randint(0, 1): return (l, extend(r))
            else: return (extend(l), r)
    t = ''
    for _ in range(n-1): t = extend(t)
    return t

def format(t):
    def pad(prefix, spaces, previous):
        return prefix + (' ' * spaces) + previous
    def merge(l, r):
        l_above, l_below, l_lines = l
        r_above, r_below, r_lines = r
        gap = r_below + l_above
        gap_above = l_above
        gap_below = gap - gap_above
        def lines():
            for (i, line) in enumerate(chain(r_lines, l_lines)):
                if i < r_above:
                    yield ' ' + line
                elif i - r_above < gap_above:
                    dash = '_' if i - r_above == gap_above - 1 else ' '
                    if i < r_above + r_below:
                        yield pad(dash + '/', 2 * (i - r_above), line)
                    else:
                        yield pad(dash + '/', 2 * gap_below - 1, line)
                elif i - r_above - gap_above < gap_below:
                    if i < r_above + r_below:
                        yield pad(' \\', 2 * gap_above - 1, line)
                    else:
                        spaces = 2 * (r_above + gap_above + gap_below - i - 1)
                        yield pad(' \\', spaces, line)
                else:
                    yield ' ' + line
        return (r_above + gap_above, gap_below + l_below, lines())
    def descend(left, t):
        if leaf(t):
            if left:
                return (1, 0, [t])
            else:
                return (0, 1, [t])
        else:
            l, r = t
            return merge(descend(True, l), descend(False, r))
    def flatten(t):
        above, below, lines = t
        for (i, line) in enumerate(lines):
            if i < above: yield (' ' * (above - i - 1)) + line
            else: yield (' ' * (i - above)) + line
    return '\n'.join(flatten(descend(True, t)))


if __name__ == '__main__':
    for n in range(1,20,3):
        tree = random(n)
        print(format(tree))

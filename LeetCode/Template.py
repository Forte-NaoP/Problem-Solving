from typing import *
import ast

"""
Solution class here
"""

if __name__ == '__main__':
    fs = open('./input.txt')
    instance = Solution()
    solution = getattr(instance, dir(instance)[-1])
    solution(*map(lambda x: ast.literal_eval(str.strip(x)), fs.readlines()))
    fs.close()

import sys
# from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
# import robot

@keyword(name="phep cong")
def add (a,b):
    return (int(a)+int(b))

# def call_keyword(keyword):
#     return BuiltIn().run_keyword(keyword)
def get_keyword_names(self):
    return [name for name in dir(self) if hasattr(getattr(self, name), 'robot_name')]

if __name__ == '__main__':
    actions = {'add': add, 'help': help}
    try:
        action = sys.argv[1]
    except IndexError:
        action = 'help'
    args = sys.argv[2:]
    try:
        actions[action](*args)
    except (KeyError, TypeError):
        help()
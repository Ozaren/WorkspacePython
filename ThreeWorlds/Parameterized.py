from functools import wraps

def parametrized(dec):
    def layer(*args, **kwargs):
        @wraps(dec)
        def repl(f):
            return dec(f, *args, **kwargs)
#         
#         if len(args) == 1 and len(kwargs) == 0 and args[0] == dec:
#             # actual decorated function
#             class IllegalParameterizedDecorator(Exception):
#                 
#                 def __init__(self):
#                     super(IllegalParameterizedDecorator, self).__init__('{} is illegally used, must have parameters'.format(dec))
#                 pass
#             
#             raise IllegalParameterizedDecorator()
#         else:
#             # decorator arguments
#             return repl(dec)
        return repl
    return layer

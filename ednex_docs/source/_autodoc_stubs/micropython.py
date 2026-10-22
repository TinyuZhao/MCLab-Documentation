"""Small host-side subset used while importing firmware modules for Sphinx."""


def const(value):
    return value


def schedule(function, argument):
    return function(argument)

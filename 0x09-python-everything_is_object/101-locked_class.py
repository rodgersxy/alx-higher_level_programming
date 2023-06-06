#!/usr/bin/python3
"""class LockedClass that only allows users to dynamically
create instance only if attr is 'first_name'"""


class LockedClass:
    __slots__ = ['first_name']

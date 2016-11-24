# coding: utf-8

from __future__ import unicode_literals
import hueobject


class Schedule(hueobject.HueLLDevice):
    def __init__(self, *args, **kwargs):
        super(Schedule, self).__init__('groups', *args, **kwargs)

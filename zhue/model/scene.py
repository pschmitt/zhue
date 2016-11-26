from __future__ import unicode_literals
import basemodel


class Scene(basemodel.BaseGroup):
    def __init__(self, *args, **kwargs):
        super(Scene, self).__init__('scenes', *args, **kwargs)

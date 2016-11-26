from __future__ import unicode_literals
import basemodel


class Scene(basemodel.BaseGroup):
    def __init__(self, *args, **kwargs):
        super(Scene, self).__init__('scenes', *args, **kwargs)

    @property
    def owner(self):
        return self._bridge.user(username=self._json['owner'])

    @property
    def version(self):
        return self._json['version']

    @property
    def picture(self):
        return self._json['picture']

    @property
    def locked(self):
        return self._json['locked']

    @property
    def last_updated(self):
        return self._json['last_updated']

    @property
    def appdata(self):
        return self._json['appdata']

    @property
    def recycle(self):
        return self._json['recycle']

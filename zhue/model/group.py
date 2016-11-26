from __future__ import unicode_literals
import basemodel


class Group(basemodel.BaseGroup):
    def __init__(self, *args, **kwargs):
        super(Group, self).__init__('groups', *args, **kwargs)

    @property
    def state(self):
        return GroupState(
            dict(self._json['state'].items() + self._json['action'].items())
        )

    @property
    def all_on(self):
        return self.state.all_on

    @property
    def any_on(self):
        return self.state.any_on

    def _set_state(self, data):
        # Groups have a different endpoint for the "state" (/action)
        url = '{}/action'.format(self.API)
        res = self._request(
            method='PUT',
            url=url,
            data=data
        )
        self.update()
        return res


class GroupState(basemodel.LightDeviceState):
    @property
    def all_on(self):
        return self._json['all_on']

    @property
    def any_on(self):
        return self._json['any_on']

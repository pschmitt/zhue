from __future__ import unicode_literals
import hueobject


class Light(hueobject.HueDevice):
    def __init__(self, *args, **kwargs):
        super(Light, self).__init__('lights', *args, **kwargs)

    def __on_off(self, state):
        assert state in ['on', 'off'], 'Unknown state: {}'.format(state)
        url = '{}/state'.format(self.API)
        data = {'on': state == 'on'}
        return self._bridge._request(
            method='PUT',
            url=url,
            data=data
        )

    def on(self):
        return self.__on_off('on')

    def off(self):
        return self.__on_off('off')

    def is_on(self):
        return self.state['on']

    def rename(self, new_name):
        url = '{}/lights/{}'.format(self._bridge.API, self.hue_id)
        data = {'name': new_name}
        res = self._bridge._request(
            method='PUT',
            url=url,
            data=data
        )
        if type(res) is list and len(res) > 0 and 'success' in res[0]:
            self._json['name'] = res[0]['success']['/lights/{}/name'.format(self.hue_id)]

    def delete(self):
        url = '{}/lights/{}'.format(self._bridge.API, self.hue_id)
        return self._bridge._request(
            method='DELETE',
            url=url
        )

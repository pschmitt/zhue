from __future__ import unicode_literals
import hueobject


class Light(hueobject.HueDevice):
    def __init__(self, *args, **kwargs):
        super(Light, self).__init__('lights', *args, **kwargs)

    def __on_off(self, state):
        assert state in ['on', 'off'], 'Unknown state: {}'.format(state)
        return self._set_state(data={'on': state == 'on'})

    def on(self):
        return self.__on_off('on')

    def off(self):
        return self.__on_off('off')

    def is_on(self):
        return self.state['on']

    def delete(self):
        return self._request(method='DELETE')

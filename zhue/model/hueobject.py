from __future__ import unicode_literals
from __future__ import print_function


class HueApiResponse(object):
    def __init__(self, json):
        self._json = json

    @staticmethod
    def factory(json):
        if type(json) is list and len(json) > 0:
            if 'error' in json[0]:
                return HueErrorResponse(json)
            elif 'success' in json[0]:
                return HueSuccessResponse(json)
        return HueApiResponse(json)


class HueErrorResponse(HueApiResponse):
    pass


class HueSuccessResponse(HueApiResponse):
    pass


class HueObject(object):
    def __init__(self, json):
        self._json = json


class HueDevice(HueObject):
    def __init__(self, api_endpoint, bridge, hue_id, *args, **kwargs):
        super(HueDevice, self).__init__(*args, **kwargs)
        self.hue_id = hue_id
        self._bridge = bridge
        self.API = '{}/{}/{}'.format(
            self._bridge.API,
            api_endpoint,
            self.hue_id
        )

    # Shortcut function
    def _request(self, *args, **kwargs):
        # TODO use self.API as URL
        return self._bridge._request(*args, **kwargs)

    @property
    def manufacturer(self):
        return self._json['manufacturername']

    @property
    def model(self):
        return self._json['modelid']

    @property
    def name(self):
        return self._json['name']

    @property
    def version(self):
        return self._json['swversion']

    @property
    def uuid(self):
        return self._json['uniqueid']

    @property
    def type(self):
        return self._json['type']

    @property
    def state(self):
        return self._json['state']

    @property
    def config(self):
        return self._json['config']

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '<{}: {}>'.format(type(self).__name__, self.name)

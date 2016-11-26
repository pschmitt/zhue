from __future__ import unicode_literals
import basemodel
import user


class BridgeConfig(basemodel.HueJsonObject):
    # Versions
    @property
    def api_version(self):
        return self._json['apiversion']

    @property
    def version(self):
        return self._json['swversion']

    @property
    def bridge_id(self):
        return self._json['bridgeid']

    # Network stuff
    @property
    def dhcp(self):
        return self._json['dhcp']

    @property
    def gateway(self):
        return self._json['gateway']

    @property
    def mac(self):
        return self._json['mac']

    @property
    def netmask(self):
        return self._json['netmask']

    @property
    def zigbeechannel(self):
        return self._json['zigbeechannel']

    @property
    def factorynew(self):
        return self._json['factorynew']

    @property
    def timezone(self):
        return self._json['timezone']

    @property
    def users(self):
        u = []
        for k, v in self._json['whitelist'].iteritems():
            u.append(user.User(username=k, json=v))
        return u

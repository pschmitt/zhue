# coding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals
from .basemodel import (HueLLDevice, HueJsonObject)
from .api_response import HueSuccessResponse
import re


class Schedule(HueLLDevice):
    def __init__(self, bridge, hue_id, json):
        super(Schedule, self).__init__(bridge, 'schedules', hue_id, json)

    @staticmethod
    def new(bridge, command, localtime, status='enabled', name='',
            description='', autodelete=True, recycle=True):
        if isinstance(command, ScheduledCommand):
            cmd = command._json
        else:
            cmd = command
        if isinstance(localtime, ScheduleTime):
            ltime = localtime.timestr
        else:
            ltime = localtime
        response = bridge._request(
            url='{}/schedules'.format(bridge.API),
            method='POST',
            data={
                'command': cmd,
                'name': name,
                'description': description,
                'status': status,
                'localtime': ltime,
                # 'autodelete': autodelete, # FIXME
                'recycle': recycle
            }
        )
        if type(response) is HueSuccessResponse:
            return bridge.schedule(hue_id=response._json['id'])
        return response

    @property
    def description(self):
        return self._json['description']

    @property
    def created(self):
        return self._json['created']

    @property
    def time(self):
        return ScheduleTime(self._json['time'])

    @property
    def localtime(self):
        return ScheduleTime(self._json['localtime'])

    @property
    def command(self):
        return ScheduledCommand(self._json['command'])

    @property
    def device(self):
        return self._bridge.from_address(self.command.address)

    @property
    def status(self):
        return self._json['status']

    @property
    def recycle(self):
        return self._json['recycle']


class ScheduleTime(object):
    def __init__(self, timestr):
        self.timestr = timestr

    @property
    def recurring(self):
        return re.match(
            r'W\d{3}/T\d{2}:\d{2}:\d{2}(A\d{2}:\d{2}\d{2})?',
            self.timestr
        ) is not None

    # @property
    # def randomized(self):
    #     return re.match(
    #         r'(W\d{3}/T)?\d{2}:\d{2}:\d{2}(A\d{2}:\d{2}\d{2})?',
    #         self.timestr
    #     ) is not None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '<ScheduleTime: {}>'.format(self.timestr)


class RecurringTime(ScheduleTime):
    pass


class ScheduledCommand(HueJsonObject):
    @property
    def method(self):
        return self._json['method']

    @property
    def body(self):
        return self._json['body']

    @property
    def address(self):
        '''
        Override the address property because if does not contain the
        bridge hostname
        '''
        return self._json['address']

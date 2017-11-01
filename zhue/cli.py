#!/usr/bin/env python

from __future__ import print_function
from __future__ import absolute_import
import argparse
import logging

from model.bridge import Bridge


def parse_args():
    ON_OFF_CHOICE = ['on', 'off']
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username',
                        help='Username', required=True)
    parser.add_argument('-b', '--bridge',
                        help='Hostname or IP of the Hue bridge',
                        default=None, required=False)
    subparsers = parser.add_subparsers(dest='action', help='Action')
    light_parser = subparsers.add_parser('light')
    light_parser.add_argument('NAME')
    light_parser.add_argument('STATE', choices=ON_OFF_CHOICE)
    sensors_parser = subparsers.add_parser('sensors')
    sensor_parser = subparsers.add_parser('sensor')
    sensor_parser.add_argument('NAME')
    sensor_parser.add_argument('STATE', choices=ON_OFF_CHOICE, nargs='?')
    return parser.parse_args()


def main():
    args = parse_args()
    if args.bridge:
        bridge = Bridge(args.bridge, username=args.username)
    else:
        bridge = Bridge.discover_nupnp(username=args.username)
        if bridge:
            bridge = bridge[0]
    if args.action == 'lights':
        print(bridge.lights)
    elif args.action == 'light':
        light = bridge.light(args.NAME)
        if args.STATE == 'on':
            light.on()
        else:
            light.off()
    elif args.action == 'sensor':
        sensor = bridge.sensor(args.NAME)
        print(vars(sensor.config))
        print(sensor._json)
        if args.STATE == 'on':
            print(sensor.enable())
        elif args.STATE == 'off':
            print(sensor.disable())
        else:
            print(sensor._json)
    elif args.action == 'sensors':
        print(bridge.sensors)


if __name__ == '__main__':
    main()

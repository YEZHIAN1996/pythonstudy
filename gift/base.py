# coding:utf-8

import os
import time
import json
from common import utils, error, consts
from common.consts import FIRSTLEVELS, SECONDLEVELS
class Base(object):
    def __init__(self, user_json, gift_json):
        self.user_json = user_json
        self.gift_json = gift_json

        self.__check_user_json()
        self.__check_gift_json()
        self.__read_gifts()

    def __check_user_json(self):
        utils.check_file(self.user_json)

    def __check_gift_json(self):
        utils.check_file(self.gift_json)

    def __read_users(self, time_to_str=False):
        with open(self.user_json, 'r') as f:
            data = json.loads(f.read())

        if time_to_str == True:
            for username, v in data.item():
                v['create_time'] = utils.timestamp_to_string(v['create_time'])
                v['update_time'] = utils.timestamp_to_string(v['update_time'])
                data[username] = v
        return data

    def __write_user(self, **user):
        if 'username' not in user:
            raise ValueError('missing username')
        if 'role' not in user:
            raise ValueError('missing role')

        user['active'] = True
        user['create_time'] = time.time()
        user['update_time'] = time.time()
        user['gifts'] = []

        users = self.__read_users()

        if user['username'] in users:
            raise error.UserExistsError('username %s had exists' % users['username'])

        users.update(
            {user['username']: user}
        )

        self.__save(users, self.user_json)

    def __change_role(self, username, role):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False
        if role not in consts.ROLES:
            raise error.RoleError('not use role %s' % role)

        user['role'] = role
        user['update_time'] = time.time()

        users[username] = user
        self.__save(users, self.user_json)
        return True

    def __change_active(self, username):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False

        user['active'] = not user['active']
        user['update_time'] = time.time()
        users[username] = user
        self.__save(users, self.user_json)

    def __delete_user(self, username):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False

        delete_user = users.pop(username)

        self.__save(users, self.gift_json)

    def __read_gifts(self):
        with open(self.gift_json) as f:
            data = json.loads(f.read())
        return data

    def __init_gifts(self):
        data = {
            'level1': {
                'level1': {},
                'level2': {},
                'level3': {}
            },
            'level2': {
                'level1': {},
                'level2': {},
                'level3': {}
            },
            'level3': {
                'level1': {},
                'level2': {},
                'level3': {}
            },
            'level4': {
                'level1': {},
                'level2': {},
                'level3': {}
            }
        }
        gifts = self.__read_gifts()
        if len(gifts) != 0:
            return
        self.__save(gifts, self.gift_json)

    def __write_gift(self, first_level, second_level, gift_name, gift_count):
        if first_level not in FIRSTLEVELS:
            raise error.levelError('first_level not exsist')
        if second_level not in SECONDLEVELS:
            raise error.levelError('second_level not exsist')

        gifts = self.__read_gifts()
        current_gift_pool = gifts[first_level]
        current_second_gift_pool = current_gift_pool[second_level]

        if gift_count <= 0:
            gift_count = 1
        if gift_name in current_second_gift_pool[gift_name]:
            current_second_gift_pool[gift_name]['count'] = current_second_gift_pool[gift_name]['count'] + gift_count
        else:
            current_second_gift_pool[gift_name] = {
                'name': gift_name,
                'count': gift_count
            }
        current_gift_pool[second_level] = current_second_gift_pool
        gifts[first_level] = current_gift_pool
        self.__save(gifts, self.gift_json)

    def __save(self, data, path):
        json_data = json.dumps(data)
        with open(path, 'w') as f:
            f.write(json_data)

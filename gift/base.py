# coding:utf-8

import os
import time
import json
from common import utils, error,consts

class Base(object):
    def __init__(self, user_json, gift_json):
        self.user_json = user_json
        self.gift_json = gift_json

        self.__check_user_json()
        self.__check_gift_json()

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

        json_users = json.dumps(users)
        with open(self.user_json, 'w') as f:
            f.write(json_users)

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
        json_data = json.dumps(users)
        with open(self.user_json, 'w') as f:
            f.write(json_data)
        return True


    def __change_active(self, username):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False

        user['active'] = not user['active']
        user['update_time'] = time.time()
        users[username] = user
        json_data = json.dumps(users)
        with open(self.user_json, 'w') as f:
            f.write(json_data)
        return True

    def __delete_user(self, username):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False

        delete_user = users.pop(username)

        json_data = json.dumps(users)
        with open(self.user_json, 'w') as f:
            f.write(json_data)
        return delete_user
print('########################################################')
print('# configpaser')
print('########################################################')

import configparser

config = configparser.ConfigParser()
# config['DEFAULT'] = {
#     'debug': True
# }
# config['web_server'] = {
#     'host': '127.0.0.1',
#     'port': 80
# }
# config['db_server'] = {
#     'host': '127.0.0.1',
#     'port': 3306
# }
# with open('config/config.ini', 'w') as config_file:
#     config.write(config_file)

config.read('config/config.ini')
print(config, type(config))
print(config['web_server'])
print(config['web_server']['host'])

print('########################################################')
print('# yaml')
print('########################################################')

import yaml

# with open('config/config.yaml', 'w') as yaml_file:
#     yaml.dump({
#         'web_server': {
#             'host': '127.0.0.1',
#             'port': 80
#         },
#         'db_server': {
#             'host': '127.0.0.1',
#             'port': 3306
#         }
#     }, yaml_file, default_flow_style=False)

with open('config/config.yaml', 'r') as yaml_file:
    data = yaml.load(yaml_file, Loader=yaml.Loader)
    print(data, type(data))
    print(data['web_server'])
    print(data['web_server']['host'])

print('########################################################')
print('# 로깅')
print('########################################################')

"""
python log level 순서
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""

import logging

# logging.basicConfig(filename='test.log', level=logging.INFO)
logging.basicConfig(level=logging.INFO)

# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')

logging.info('info {} {}'.format('test', "kk"))

print('########################################################')
print('# 로깅 포매터')
print('########################################################')

formatter = '%(asctime)s:%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

logging.info('info {} {}'.format('a', 'b'))

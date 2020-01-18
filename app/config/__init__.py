import os
import configparser

cfg_path = '/home/administrator/PycharmProjects/wallpager-download-tool/app/config/cfg.ini'

cfg = configparser.ConfigParser()
cfg.read(cfg_path)


def get(section, option):
    # 检查配置项是否存在，存在则返回配置值，否则返回空值
    if cfg.has_option(section, option):
        return cfg.get(section, option)
    else:
        return None


def write(section, option, value):
    # 检查配置组是否不存在，不存在则添加配置组
    if not cfg.has_section(section):
        cfg.add_section(section)
    cfg.set(section, option, value)
    cfg.write(open(cfg_path, 'w'))


def remove(section, option):
    # 检查配置组是否存在，存在则删除配置项，否则不操作
    if cfg.has_section(section):
        cfg.remove_option(section, option)
        cfg.write(open(cfg_path, 'w'))
    else:
        pass
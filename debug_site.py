# coding: utf-8

import os
import mkdocs.commands.serve


config_file_path = os.path.abspath(os.path.join(__file__, '../config.yml'))

mkdocs.commands.serve.serve(
    config_file = open(config_file_path, "rb"),
    dev_addr='127.0.0.1:80'
)


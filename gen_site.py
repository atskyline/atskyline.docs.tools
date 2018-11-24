# coding: utf-8
import os
import mkdocs.config
import mkdocs.commands.build

docs_dir = os.path.abspath(os.path.join(__file__, '../../atskyline.docs'))
site_dir = os.path.abspath(os.path.join(__file__, '../../atskyline.github.io'))
config_file_path = os.path.abspath(os.path.join(__file__, '../config.yml'))

config = mkdocs.config.load_config(
    config_file = open(config_file_path, "rb")
)

mkdocs.commands.build.build(config)

#create CNAME file
with open(os.path.join(site_dir, "CNAME"), "w") as f:
    f.write("www.atskyline.com")
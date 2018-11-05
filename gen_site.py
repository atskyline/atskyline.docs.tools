# coding: utf-8
import os
import mkdocs.config
import mkdocs.commands.build

docs_dir = os.path.abspath(os.path.join(__file__, '../../atskyline.docs'))
site_dir = os.path.abspath(os.path.join(__file__, '../../atskyline.github.io'))
nav_file_path = os.path.abspath(os.path.join(__file__, '../nav.yml'))
site_name = "朱易辰的个人网站"

print(docs_dir)
print(site_dir)

config = mkdocs.config.load_config(
    config_file = open(nav_file_path, "rb"),
    site_name = site_name,
    theme = 'mkdocs',
    site_url ='http://www.atskyline.com',
    repo_url = 'https://github.com/atskyline/atskyline.docs',
    repo_name = 'GitHub',
    docs_dir = docs_dir,
    site_dir = site_dir
)

mkdocs.commands.build.build(config)
#!/bin/env python

import os
import setuptools

if os.path.exists('./README.md'):
    with open('./README.md', 'r', encoding='utf=8') as fh:
        long_description = fh.read()

# There isn't a cleaner solution to get the latest package addition to requirements.txt
# We are using https://stackoverflow.com/a/14399775
# ^ solution also requires https://stackoverflow.com/questions/38533669/include-requirements-txt-file-in-python-wheel
if os.path.exists('./requirements.txt'):
    with open('./requirements.txt', 'r', encoding='utf-8') as rfh:
        packages_required = rfh.read().splitlines()

setuptools.setup(
        name = 'newsletter_automation',
        version = '0.0.3',
        author = 'Sravanti Tatiraju, Indira Nellutla, Preedhi Vivek, Rohan Dudam, Shivahari Pitchaikkannu',
        author_email = 'sravanti.tatiraju@qxf2.com, indira@qxf2.com, preedhi.vivek@qxf2.com, rohan@qxf2.com, shivahari@qxf2.com',
        description = 'A Qxf2 Newsletter automation app',
        long_description = long_description,
        long_description_content_type = 'text/markdown',
        url = 'https://github.com/qxf2/newsletter_app',
        classifiers = [
            'Programming Language :: Python :: 3',
            'License :: OSI :: MIT',
            'Operating System :: OS Independent'],
        packages = ['newsletter_automation'],
        zip_safe = False,
        include_package_data = True,
        install_requires = packages_required,
        python_requires = '>=3.8'
        )

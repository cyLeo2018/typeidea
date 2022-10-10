from setuptools import setup, find_packages


setup(
    name='typeidea',
    version='0.1',
    description='blog system base on django',
    author='leo',
    author_email='961363629@qq.com',
    url='https://www.classicog.com',
    license='MIT',

    packages=find_packages('typeidea'),
    package_dir={
        '': 'typeidea'
    },
    include_package_data=True,
    scripts=[
        'typeidea/manage.py',
        'typeidea/typeidea/wsgi.py',
    ],
    entry_points={
        'console_scripts': [
            'typeidea_manage = manage:main',
        ]
    },

)
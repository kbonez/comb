from setuptools import setup


setup(
    name='comb',
    version='0.9.2',
    packages=['comb', 'comb.mq', 'comb.demo'],
    install_requires=['cliez'],
    url='https://github.com/kbonez/comb',
    download_url='https://github.com/kbonez/comb/tarball/0.9.0',
    license='http://opensource.org/licenses/MIT',
    author='Breeze.Kay',
    author_email='wangwenpei@kbonez.com',
    description='A simply and high-performance framework for create concurrent program',
    keywords='comb,slot,thread,framework,hook',
    entry_points={
        'console_scripts': [
            'comb = comb.main:main'
        ]
    },


)

from distutils.core import setup

setup(
    name='mqtls',
    packages=['mqtls'],
    version='0.1',
    license='wtfpl',
    description='MqTLS client for python',
    author='Efrén Boyarizo',
    author_email='efren@boyarizo.es',
    url='https://github.com/user/reponame',
    download_url='https://github.com//reponame/archive/v_01.tar.gz',
    keywords=['MqTLS', 'gobroker', 'client'],
    install_requires=[
        'validators',
        'beautifulsoup4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Do What The F*ck You Want To Public License'
    ],
)

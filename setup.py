from setuptools import setup, find_packages

setup(
  name='Discord Webhooks',
  version='1.0.5',
  py_modules=['discord_webhooks'],
  url='https://github.com/DoggieLicc/discord-webhooks',
  author='Doggie Licc',
  author_email='doggietoe@gmail.com',
  description='Easy to use module for Python which allows for sending of webhooks to a Discord server.',
  license='MIT',
  install_requires=[
    'requests==2.24.0'
  ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Environment :: Other Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
  ],
)

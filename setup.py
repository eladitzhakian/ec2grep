try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='ec2grep',
    description='EC2 cli tool',
    author='Roey Berman',
    author_email='roey.berman@gmail.com',
    packages=['ec2grep'],
    version='0.2',
    keywords=['ec2', 'cli', 'aws', 'ssh'],
    install_requires=[
        'boto3',
        'futures',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'ec2 = ec2grep:cli'
        ]
    }
)

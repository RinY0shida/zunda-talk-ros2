from setuptools import find_packages, setup

package_name = 'zunda_talk'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rin',
    maintainer_email='tororo1219@gmail.com',
    description='This package allows Zundamon to read aloud the published string.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'zunda_talk = zunda_talk.zunda_talk_sub:main'
        ],
    },
)

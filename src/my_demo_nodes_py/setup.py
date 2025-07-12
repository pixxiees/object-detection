from setuptools import find_packages, setup

package_name = 'my_demo_nodes_py'

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
    maintainer='pixxelee',
    maintainer_email='lailyananda25@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_publisher = my_demo_nodes_py.simple_publisher:main',
            'simple_subscriber = my_demo_nodes_py.simple_subscriber:main',
        ],
    },
)

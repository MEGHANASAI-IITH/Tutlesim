from setuptools import find_packages, setup

package_name = 'turt_controller'

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
    maintainer='hp',
    maintainer_email='m.meghanasai@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = turt_controller.my_first_node:main",
            "draw_circle = turt_controller.draw_circle:main",
            "pose_subscriber = turt_controller.pose_subscriber:main",
            "turtle_controller = turt_controller.turtle_controller:main",
            "turtle_catcher = turt_controller.turtle_catcher:main"
        ],
    },
)

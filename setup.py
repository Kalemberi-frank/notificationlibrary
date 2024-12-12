from setuptools import setup, find_packages

setup(
    name='iot_notification_system',
    version='0.1',
    description='An IoT-based notification system for swine fever detection',
    author='Your Name',
    author_email='kalemberifrank@gmail.com.com',
    packages=find_packages(),
    install_requires=[
        'paho-mqtt==1.6.1',
        'Flask==2.3.2'
    ],
)

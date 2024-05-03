from setuptools import setup, find_packages

setup(
    name='analytics',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    author='rakhi',
    author_email='rakhi.pr@beinex.com',
    description='A Django app for analytics purposes',
    url='https://github.com/rakhi641557/django-analytics',
    license='MIT',
    install_requires=[
        'Django',
        
    ],
)
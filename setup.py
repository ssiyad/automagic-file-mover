from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='moover',
    version='1.1.2',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/ssiyad/automagic-file-mover',
    license='MIT',
    author='Sabu Siyad',
    author_email='sabu.siyad.p@gmail.com',
    description='Automagically Move Files',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "py-notifier==0.1.0",
        "watchdog==0.9.0"
    ],
    entry_points={
        "console_scripts": [
            "moover = moover.__main__:main",
        ]
    }
)

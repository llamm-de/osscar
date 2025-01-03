from setuptools import setup, find_packages

setup(
    name='osscar',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            # 'osscar_command=osscar.main:main'
        ],
    },
    install_requires=[
    ],
    author='Lukas Lamm',
    author_email='lamm.lukas@gmail.com',
    description='A brief description of your project',
    url='https://github.com/llamm-de/osscar',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
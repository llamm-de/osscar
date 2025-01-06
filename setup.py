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
        'iniconfig==2.0.0',
        'packaging==24.2',
        'pluggy==1.5.0',
        'pytest==8.3.4',
        'pytest-cov==6.0.0',
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
    python_requires='>=3.9',
)
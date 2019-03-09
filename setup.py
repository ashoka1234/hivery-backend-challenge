from setuptools import setup, find_packages

tests_require = [
    'pytest'
]

extras_require = {
    'test' : tests_require
}

setup(

    name='ashoka_challenge',

    version='0.1',

    python_requires='>=3.6',

    author='Ashoka Jayawardena',

    packages=find_packages(),

    install_requires=[
        'click',
        'flask',
        'pymongo'
    ],

    extras_require=extras_require,
    tests_require=tests_require,

    entry_points={
        'console_scripts': [
            'challenge-manage = manage:cli',
        ],
    }
)

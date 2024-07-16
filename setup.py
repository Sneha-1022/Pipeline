
### `setup.py`

Optionally, if you want to use a `setup.py` file to manage your Python package, you can include one:

```python
from setuptools import setup, find_packages

setup(
    name='lambda_function',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'requests'
    ],
)


from setuptools import setup, find_packages
setup(
    name = "codefile",
    version = "0.2",
    packages = find_packages()
    )

# import os
# print('pushing the build to repo')
# os.system('twine upload --repository-url https://console.cloud.google.com/artifacts/pypi/mytest-316909/asia-south1/unittest-repo/ dist/*')

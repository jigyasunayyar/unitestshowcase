import os
print('exporting the path to path variable')
os.system('export PATH=/builder/home/.local/bin:$PATH >> ~/.bashrc')

print('pushing the repo using twine')
os.system('twine upload --repository-url https://console.cloud.google.com/artifacts/pypi/mytest-316909/asia-south1/unittest-repo/ dist/*')
          

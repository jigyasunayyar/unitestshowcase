import os
# print('exporting the path to path variable')
# os.system('export PATH=/builder/home/.local/bin:$PATH >> ~/.bashrc')
# os.system('. ~/.bashrc')

# print('pushing the repo using twine')
# os.system('twine upload --repository-url https://console.cloud.google.com/artifacts/pypi/mytest-316909/asia-south1/unittest-repo/ dist/*')

print('copy the file to user home folder')
os.system('cp -f .pypirc ~/')

          

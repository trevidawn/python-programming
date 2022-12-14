print('########################################################')
print('# 파일의 작성')
print('########################################################')
f = open('file/test.txt', 'w')
f.write('Test\n')
print('I am print', file=f)
print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
f.close()

"""FILE OUTPUT
Test
I am print
My#name#is#Mike!
"""

print('########################################################')
print('# with 구문으로 파일을 open하기')
print('########################################################')

with open('file/test.txt', 'w') as f:
    f.write('file open with "with statement"\n')
    # f.close()

print('########################################################')
print('# 파일 읽어오기')
print('########################################################')

s = """\
AAA
BBB
CCC
DDD
"""

with open('file/test.txt', 'w') as f:
    f.write(s)

with open('file/test.txt', 'r') as f:
    print(f.read())
    """OUTPUT
    AAA
    BBB
    CCC
    DDD
    """

with open('file/test.txt', 'r') as f:
    while True:
        line = f.readline()
        print(line, end='')
        if not line:
            break
    """OUTPUT
    AAA
    BBB
    CCC
    DDD
    """

with open('file/test.txt', 'r') as f:
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break
    """OUTPUT
    AA
    A
    
    BB
    B
    
    CC
    C
    
    DD
    D
    
    """

print('########################################################')
print('# seek를 써서 이동하기')
print('########################################################')

with open('file/test.txt', 'r') as f:
    f.seek(5)
    print(f.tell(), ", ", f.read(1))
    f.seek(10)
    print(f.tell(), ", ", f.read(1))
    """OUTPUT
    5 ,  B
    10 ,  C
    """

print('########################################################')
print('# 쓰기와 읽어오기 모드')
print('########################################################')

"""
w+로 열어온 순간 파일이 공백 파일이 된다.
"""
with open('file/test.txt', 'w+') as f:
    f.write(s)
    f.seek(0)
    print(f.read())

"""
r+로 읽어올 파일이 없으면 에러
"""
with open('file/test.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)

print('########################################################')
print('# 템플릿')
print('########################################################')

import string

"""
with 구문 안에서 선언된 변수는 밖에서도 쓸 수 있다.
"""

with open('file/template1.txt') as f:
    t = string.Template(f.read())

contents = t.substitute(name="Mike", contents="How are you?")
print(contents)
"""OUTPUT
Hi Mike.

How are you?

Have a good day
"""

print('########################################################')
print('# CSV 파일에 쓰고 읽어오기')
print('########################################################')

import csv

with open('file/test.csv', 'w') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})
    """FILE OUTPUT
    Name,Count
    A,1
    B,2
    """

with open('file/test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])
    """OUTPUT
    A 1
    B 2
    """

print('########################################################')
print('# 파일 조작')
print('########################################################')

import os

print(os.path.exists('file/test.txt'))
print(os.path.isfile('file/test.txt'))
print(os.path.isdir('file'))

os.rename('file/test.txt', 'file/test.txt')
# os.symlink('test.txt', 'symlink_test.txt')
os.mkdir('file/test_dir')
# os.rmdir('test_dir')

import pathlib

pathlib.Path('file/empty.txt').touch()
os.remove('file/empty.txt')

import glob
import shutil
pathlib.Path('file/test_dir/empty.txt').touch()
shutil.copy('file/test_dir/empty.txt', 'file/test_dir/empty2.txt')
print(glob.glob('file/test_dir/*'))

shutil.rmtree('file/test_dir')
print(os.getcwd())

print('########################################################')
print('# tarfile의 압축 및 풀기')
print('########################################################')

import tarfile

with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('file/tar')

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(tr, path="test_tar")
    with tr.extractfile('file/tar/sub_dir/sub_dir_test.txt') as f:
        print(f.read())

print('########################################################')
print('# zipfile의 압축 및 풀기')
print('########################################################')

print('########################################################')
print('# tempfile')
print('########################################################')

print('########################################################')
print('# subprocess로 명령어 실행하기')
print('########################################################')

"""
터미널 커맨드 
os.system() 보다 subprocess가 더 낫다
"""
import subprocess

# subprocess.run(['ls', '-al'])
# subprocess.run('ls -al', shell=True) >> 보안이슈: shell injection :: | 파이프 쓰고 커맨드 더 쓸 수 있음
# r = subprocess.run('las', shell=True)
# print(r.returncode)

p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)


print('########################################################')
print('# datetime')
print('########################################################')

import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y-%H%M%S%f'))
print()

today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))
print()

t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print()

print(now)
d = datetime.timedelta(weeks=-1)
print(now + d)
print()

import time
time.sleep(1)
print(time.time())
print()

import os
import shutil

file_name = 'file/test.txt'

if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(
        file_name, now.strftime('%Y_%m_%d_%H_%M_%S')
    ))

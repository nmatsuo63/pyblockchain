import collections
import hashlib

block = {'b': 2, 'a': 1}
block2 = {'a': 1, 'b': 2}
print(hashlib.sha256('test'.encode()).hexdigest())
print(hashlib.sha256('test'.encode()).hexdigest())
print(hashlib.sha256('test2'.encode()).hexdigest())
print(hashlib.sha256(str(block).encode()).hexdigest())
print(hashlib.sha256(str(block2).encode()).hexdigest())
print(f'~' * 25)


block = collections.OrderedDict(sorted(block.items(), key=lambda d:d[0]))
block2 = collections.OrderedDict(sorted(block2.items(), key=lambda d:d[0]))
print(hashlib.sha256(str(block).encode()).hexdigest())
print(hashlib.sha256(str(block2).encode()).hexdigest())

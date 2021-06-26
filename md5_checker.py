# working of MD5 (byte - byte)

import os
import sys
import time
import string
import argparse
import itertools
import hashlib

class md5C():
    def __init__(self):
        self.md5List = open(input('Enter md5 list file:'),'r').readlines()
        try:
            self.dataList = open(input('Enter wordlist file:'),'rb').readlines()
            self.customList()
        except: self.selfList(int(input('min>')),int(input('max>')))
    
    @property
    def the_md5(self):
        return hashlib.md5(self.d).hexdigest()+'\n'

    def customList(self):
        for i in self.dataList:
            self.d = i
            sys.stdout.write('\r[+] testing on `%s`' % i.decode())
            if self.the_md5 in self.md5List:
                print("%s:%s"%(i.decode(),self.the_md5))

    def selfList(self, min_length, max_length,chrs='abcdefghijklmnopqestuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.'):
        for n in range(min_length, max_length + 1):
            for xs in itertools.product(chrs, repeat=n):
                chars = ''.join(xs)
                self.d = chars.encode()
                if self.the_md5 in self.md5List:
                    print("%s:%s"%(chars,self.the_md5))
                sys.stdout.write('\r[+] testing on `%s`' % chars)
                self.d = chars
                sys.stdout.flush()

md5C()


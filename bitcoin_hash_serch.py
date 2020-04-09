# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 21:09:11 2020

@author: tetsuya
"""
import urllib3
import certifi

if __name__ == '__main__':
    url='https://blockchain.info/rawblock/000000000000000000003b6e10bfe41a9065fac05b1e984f0c90b19035e012d6'
    
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED' , ca_certs=certifi.where())
    r = http.request('GET', url)
    print(r.data)

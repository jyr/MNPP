#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is part of the web2py Web Framework
Copyrighted by Massimo Di Pierro <mdipierro@cs.depaul.edu>
License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)

This file specifically includes utilities for security.
"""

import hashlib
import hmac
import uuid
import random
import thread
import time
import os

def md5_hash(text):
    """ Generate a md5 hash with the given text """
    return hashlib.md5(text).hexdigest()

def simple_hash(text, digest_alg = 'md5'):
    """
    Generates hash with the given text using the specified
    digest hashing algorithm
    """
    if not digest_alg:
        raise RuntimeError, "simple_hash with digest_alg=None"
    elif not isinstance(digest_alg,str):
        h = digest_alg(text)
    else:
        h = hashlib.new(digest_alg)
        h.update(text)
    return h.hexdigest()

def get_digest(value):
    """
    Returns a hashlib digest algorithm from a string
    """
    if not isinstance(value,str):
        return value
    value = value.lower()
    if value == "md5":
        return hashlib.md5
    elif value == "sha1":
        return hashlib.sha1
    elif value == "sha224":
        return hashlib.sha224
    elif value == "sha256":
        return hashlib.sha256
    elif value == "sha384":
        return hashlib.sha384
    elif value == "sha512":
        return hashlib.sha512
    else:
        raise ValueError("Invalid digest algorithm")

def hmac_hash(value, key, digest_alg='md5', salt=None):
    if ':' in key:
        digest_alg, key = key.split(':')
    digest_alg = get_digest(digest_alg)
    d = hmac.new(key,value,digest_alg)
    if salt:
        d.update(str(salt))
    return d.hexdigest()


### compute constent ctokens
def initialize_urandom():
    """
    This function and the web2py_uuid follow from the following discussion:
    http://groups.google.com/group/web2py-developers/browse_thread/thread/7fd5789a7da3f09

    At startup web2py compute a unique ID that identifies the machine by adding 
    uuid.getnode() + int(time.time() * 1e3)

    This is a 48bits number. It converts the number into 16x8bits tokens.
    It uses thie unique if to initilize the entropy source ('/dev/urandom') or to seed random.

    If os.random() is not supported, it falls back to using random and issues a warning.
    """
    node_id = uuid.getnode()
    milliseconds = int(time.time() * 1e3)
    ctokens = [((node_id + milliseconds) >> ((i%6)*8)) % 256 for i in range(16)]
    try:
        os.urandom(1)
        if os.path.exists('/dev/urandom'):
            open('/dev/urandom','wb').write(''.join(chr(t) for t in ctokens))
    except:
        random.seed(node_id + milliseconds)
        logging.warn(
"""Cryptographycally secure session management is not possible on your system because
your system does not provide a cryptographically secure entropy source.
This is not specific to web2py. Consider deploying on a different Operating System.""")
    return ctokens
ctokens = initialize_urandom()

def web2py_uuid():
    """
    This function follows from the following discussion:
    http://groups.google.com/group/web2py-developers/browse_thread/thread/7fd5789a7da3f09
    
    It works like uuid.uuid4 exxcept that tries to use os.urandom() if possible
    And it XORs the output with the tokens uniquely associated to this machine.
    """
    try:
        bytes = os.urandom(16) # use /dev/urandom if possible
    except NotImplementedError:
        bytes = [chr(random.randrange(256)) for i in range(16)]
    ## xor bytes with contant ctokens
    bytes = ''.join(chr(ord(c) ^ ctokens[i]) for i,c in enumerate(bytes))
    return str(uuid.UUID(bytes=bytes, version=4))

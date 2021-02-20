import hashlib
import json
import datetime
from typing import List


class Blockchain:

    def __init__(self):
        self.chain: List[Block] = []
        self.generate_genesis_block()

    @property
    def last_block(self):
        return self.chain[-1]

    @property
    def genesis_block(self):
        return self.chain[0]

    def add_block(self, block):
        if self.validate_block(block):
            self.chain.append(block)

    def validate_block(self, block):
        if block is None:
            raise Exception("Block is not valid")

        if self.last_block.timestamp == block.timestamp:
            block.timestamp = datetime.datetime.utcnow().timestamp()
            block.hash_block()

        return self.last_block.hash == block.previous_hash

    def generate_genesis_block(self):
        genesis_block = Block([], '').hash_block()
        self.chain.append(genesis_block)

    def print(self):
        for block in self.chain:
            print(block)


class Block:

    def __init__(self, data, previous_hash):
        self.validate_data(data)
        self.timestamp = datetime.datetime.utcnow().timestamp()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = ''

    def __str__(self):
        return self.serialize()

    def __repr__(self):
        return self.serialize()

    def serialize(self):
        return json.dumps(self.__dict__)

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.serialize().encode())
        return sha.hexdigest()

    def hash_block(self):
        self.hash = self.calc_hash()
        return self

    def validate_data(self, data):
        if data is None:
            raise Exception("Input params are not valid")


def test_block_chain():
    print("Test generated valid blockchain")
    chain = Blockchain()

    for i in range(10):
        block = Block([{"data": "some content"}], chain.last_block.hash).hash_block()
        chain.add_block(block)

    chain.print()


def test_add_not_valid_block():
    print("\nTest not valid block won't be added")
    chain = Blockchain()
    chain.add_block(Block([], ''))

    if len(chain.chain) != 1:
        raise Exception('Error while adding a new block')

    chain.print()


def test_previous_hash():
    print("\nTest previous hash")
    chain = Blockchain()

    block = Block([{"data": "some content"}], chain.last_block.hash).hash_block()
    chain.add_block(block)

    if chain.last_block.previous_hash != chain.genesis_block.hash:
        raise Exception('Hash is not valid')

    chain.print()


def test_not_valid_block():
    print("\nTest add not valid block")
    chain = Blockchain()

    try:
        chain.add_block(None)
    except Exception:
        print("passed")


def test_same_timestamp():
    print("\nTest same timestamps")
    chain = Blockchain()

    timestamp = datetime.datetime.utcnow().timestamp()
    block1 = Block([], chain.last_block.hash)
    block1.timestamp = timestamp
    block1.hash_block()
    chain.add_block(block1)

    block2 = Block([], chain.last_block.hash)
    block2.timestamp = timestamp
    block2.hash_block()
    chain.add_block(block2)

    if chain.chain[-1].timestamp == chain.chain[-2].timestamp:
        raise Exception("timestamps are same")
    else:
        print("passed")


test_block_chain()
test_add_not_valid_block()
test_previous_hash()
test_not_valid_block()
test_same_timestamp()

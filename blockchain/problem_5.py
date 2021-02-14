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
        return self.last_block.hash == block.previous_hash

    def generate_genesis_block(self):
        genesis_block = Block([], '').hash_block()
        self.chain.append(genesis_block)

    def print(self):
        for block in self.chain:
            print(block)


class Block:

    def __init__(self, data, previous_hash):
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


test_block_chain()
test_add_not_valid_block()
test_previous_hash()

import hashlib
import time
import json


class Blockchain:

    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block):
        if self.validate_block(block):
            self.chain.append(block)

    def validate_block(self, block):
        if self.last_block.hash != block.previous_hash:
            return False
        return True

    def generate_genesis_block(self):
        genesis_block = Block([], '').hash_block()
        self.chain.append(genesis_block)


class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
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
    chain = Blockchain()

    for i in range(10):
        block = Block([{"data": "some content"}], chain.last_block.hash).hash_block()
        chain.add_block(block)
        print(block)


test_block_chain()

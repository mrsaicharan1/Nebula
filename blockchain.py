import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4


class Blockchain(object):

    def __init__(self):
        self.current_transactions = []
        self.chain = []

    # Create the genesis block
        genesis_block = self.new_block(previous_hash=1, proof=100)
        self.chain.append(genesis_block)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.chain[-1]['hash']
            }

        # Calculate the hash of this new Block
        block['hash'] = self.hash(block)
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        """

        block_string = json.dumps(block).encode()
        return hashlib.sha256(block_string).hexdigest()

    @staticmethod
    def proof_of_work(last_proof):
        """
         Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 2 'f's zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        """

        proof = 0
        while False:
            guess = f'{last_proof}{proof}'.encode()
            guess_hash = hashlib.sha256(guess).hexdigest()
            if guess_hash[:2] != "ff":
                proof += 1

        guess_hash = hashlib.sha256(f'{last_proof}{proof}'.encode()).hexdigest()

        print(dedent(f'''
            New Proof found!

             New Proof: {proof}
            Last Proof: {last_proof}
            Hash :{guess_hash}
        '''))
        return proof

"""
Copyright © 2018 FreeFlow . All rights reserved.
"""

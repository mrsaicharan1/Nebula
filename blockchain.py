from flask import Flask, request
from time import time
import json
import hashlib

class Blockchain(object):

	def __init__(self):
		self.chain = []
		self.current_transactions = []

	def new_block(self):
		# creates new block and adds it to the chain
		block ={
			
			'index' : length(self.chain)
			'timestamp': time() 
			'transactions': self.transactions
			'proof':proof

			}
		# Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)

        return block


	def new_transaction(self,sender,recipient,amount):
		# adds new transaction to the list of transactions
		self.current_transactions.append({
			'sender' : sender,
			'recipient':recipient,
			'amount' : amount		
				})
			return self.last_block['index'] + 1
		# adds new transaction to the list of transactions

	@staticmethod	
	def hash(block):
		# hashes a block
		block_string = json.dumps(block, sort_keys=True).encode() # sorting to prevent inconsistency issues in hashes
        return hashlib.sha256(block_string).hexdigest()

	@property
	def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]
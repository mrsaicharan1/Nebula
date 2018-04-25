from flask import Flask, jsonify,
from textwrap import dedent
from uuid import uuid4
import blockchain

app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    # Calculate POW
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transaction(
            sender="0",
            recipient=node_identifier,
            amount=1,
            )
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
	values = request.get_json() # get the JSON which was posted earlier on the server

	# check for required fields
	required = ['sender','recipient','amount']
	if not(k in required for k in values):
		return 'Missing values',400

	block_index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
	response = {'message': f'Transaction will be added to Block {block_index}'}
	return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200 # posting the data onto the flask server

if __name__ == '__main__':
    app.run(debug=True)

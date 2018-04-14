from flask import Flask
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
    return "We'll mine a new Block"
  
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
	values = request.get_json()

	# check for required fields
	required = ['sender','recipient','amount']
	if not(k in required for k in values):
		return 'Missing values',400

	index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])	
	response = {'message': f'Transaction will be added to Block {index}'}
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

from flask import jsonify, request
from DTO.BlockDTO import BlockDTO
from utils.Blockchain import BlockChain
import requests
from uuid import uuid4
from urllib.parse import urlparse

def routes(app, blockchain:BlockChain):

    @app.route('/mine_block', methods = ['GET'])
    def mine_block():

        previous_block:BlockDTO
        previous_proof:int

        previous_block = blockchain.get_previous_block()
        previous_proof = previous_block.proof
        proof = blockchain.proof_of_work(previous_proof=previous_proof)
        previous_hash = blockchain.hash(block=previous_block)

        block:BlockDTO
        block = blockchain.create_block(proof=proof, previous_hash=previous_hash)

        response = {
            'message': 'You miner a block!',
            'index':block.index,
            'timestamp':block.timestamp,
            'proof': block.proof,
            'previous_hash': block.previous_hash
        }

        return jsonify(response), 200

    @app.route('/get_chain', methods = ['GET'])
    def get_chain():
        
        response = {
            'chain': blockchain.get_chain_dict(),
            'length': len(blockchain.chain)
        }

        return jsonify(response), 200
    
    @app.route('/is_valid', methods = ['GET'])
    def is_valid():
        is_valid = blockchain.is_chain_valid()
        if is_valid:
            response = {
                'msg': 'blockchain is valid'
            }
        else:
            response = {
                'msg': 'blockchain not is valid'
            }

        return jsonify(response), 200
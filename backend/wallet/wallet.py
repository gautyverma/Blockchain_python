    # def serialize_public_key(self):
    #     """
    #     Reset the Public key to its serialized version.
    #     """  
    #     self.public_key_bytes = self.public_key.public_bytes(
    #         encoding = serialization.Encoding.PEM,#----ASA----          #Privacy-Enhanced Mail (PEM) is a de facto file format for storing 
    #         format = serialization.PublicFormat.SubjectPublicKeyInfo    # and sending cryptographic keys, certificates, and other data, 
    #                                                                     #based on a set of 1993 IETF standards defining "privacy-enhanced mail." 
    #     )

    #     # print(f'\nself.public_key_bytes:{self.public_key_bytes}')

    #     decoded_public_key = self.public_key_bytes.decode('utf-8')
    #     # print(f'\ndecoded_public_key:{decoded_public_key}')
        
    #     self.public_key = decoded_public_key


    
import json
import uuid

from backend.config import STARTING_BALANCE
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import (
    encode_dss_signature,
    decode_dss_signature
)
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

# Elliptic-curve cryptography (ECC) is an approach to public-key cryptography 
# based on the algebraic structure of elliptic curves over finite fields. 
# ECC allows smaller keys compared to non-EC cryptography 
# (based on plain Galois fields) to provide equivalent security.

class Wallet:
    """
    An individual wallet for a miner.
    Keeps track of the miner's balance.
    Allows a miner to authorize transactions.
    """
    def __init__(self, blockchain=None):
        # address of wallet---unique string of 26 characters
        # use UUID: universal unique ID

        self.blockchain = blockchain
        self.address = str(uuid.uuid4())[0:8]
        self.private_key = ec.generate_private_key(
            ec.SECP256K1(),
            default_backend()
        )
        # secp256k1 refers to the parameters of the elliptic curve 
        # used in Bitcoin's public-key cryptography, 
        # and is defined in Standards for Efficient Cryptography (SEC) 
                
        self.public_key = self.private_key.public_key()
        self.serialize_public_key()

    @property
    def balance(self):
        # @property decorator allows us to define properties 
        # easily without calling the property() function manually.

        return Wallet.calculate_balance(self.blockchain, self.address)

    def sign(self, data):
        """
        Generate a signature based on the data using the local private key.
        """
        return decode_dss_signature(self.private_key.sign(
            json.dumps(data).encode('utf-8'),
            ec.ECDSA(hashes.SHA256())
        ))

    def serialize_public_key(self):
        """
        Reset the public key to its serialized version.
        """
        self.public_key = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

    @staticmethod
    def verify(public_key, data, signature):
        """
        Verify a signature based on the original public key and data.
        """
        deserialized_public_key = serialization.load_pem_public_key(
            public_key.encode('utf-8'),
            default_backend()
        )

        (r, s) = signature

        try:
            deserialized_public_key.verify(
                encode_dss_signature(r, s),
                json.dumps(data).encode('utf-8'),
                ec.ECDSA(hashes.SHA256())    
            )
            return True
        except InvalidSignature:
            return False

    @staticmethod
    def calculate_balance(blockchain, address):
        """
        Calculate the balance of the given address considering the transaction
        data within the blockchain.

        The balance is found by adding the output values that belong to the
        address since the most recent transaction by that address.
        """
        balance = STARTING_BALANCE

        if not blockchain:
            return balance

        for block in blockchain.chain:
            for transaction in block.data:
                if transaction['input']['address'] == address:
                    # Any time the address conducts a new transaction it resets
                    # its balance
                    balance = transaction['output'][address]
                elif address in transaction['output']:
                    balance += transaction['output'][address]

        return balance

def main():
    wallet = Wallet()
    print(f'wallet.__dict__: {wallet.__dict__}')

    data = { 'foo': 'bar' }
    signature = wallet.sign(data)
    print(f'signature: {signature}')

    should_be_valid = Wallet.verify(wallet.public_key, data, signature)
    print(f'should_be_valid: {should_be_valid}')

    should_be_invalid = Wallet.verify(Wallet().public_key, data, signature)
    print(f'should_be_invalid: {should_be_invalid}')

if __name__ == '__main__':
    main()

import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain=[]
        self.current_transactions=[]

        self.new_block(previous_hash=1, proof=100)
        
    def new_block(self, proof, previous_hash=None):
        """
        블록체인에 들어갈 새로운 블록을 만드는 코드이다.
        index는 블록의 번호, timestamp는 블록이 만들어진 시간이다.
        transaction은 블록에 포함될 거래이다.
        proof는 논스값이고, previous_hash는 이전 블록의 해시값이다.
        """
        block = {
        'index':len(self.chain)+1,
        'timestamp': time(),
        'transaction': self.current_transactions,
        'proof': proof,
        'previous_hash' : previous_hash or self.hash(self.chain[-1]),
        }
        
        # 거래의 리스트를 초기화한다.
        self.current_transactions = []
        
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        새로운 거래는 다음으로 채굴될 블록에 포함되게 된다. 거래는 3개의 인자로 구성되어 있다. 
        sender와 recipient는 string으로 각각 수신자와 송신자의 주소이다. 
        amount는 int로 전송되는 양을 의미한다. return은 해당 거래가 속해질 블록의 숫자를 의미한다.
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1
    
    @property
    def last_block(self):
        """
        체인의 가장 블록을 반환한다
        """
        return self.chain[-1]
    
    @staticmethod
    def hash(block):
        """블록을 해시값을 출력한다
        SHA-256을 이용하여 블록의 해시값을 구한다.
        해시값을 만드는데 block이 input 값으로 사용된다. 
        """

    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """
        작업증명에 대한 간단한 설명이다:
        - p는 이전 값, p'는 새롭게 찾아야 하는 값이다. 
        - hash(pp')의 결과값이 첫 4개의 0으로 이루어질 때까지 p'를 찾는 과정이 작업 증명과정이다. 
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        작업증명 결과값을 검증하는 코드이다. hash(p,p')값의 앞의 4자리가 0으로 이루어져 있는가를 확인한다.
        결과값은 boolean으로 조건을 만족하지 못하면 false가 반환된다.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"    
class Blockchain(object):
    def __init__(self):
        self.chain=[]
        self.current_transactions=[]
        
    def new_block(self):
        # 새로운 블록을 생성하고 체인에 넣는다
        pass
    
    @staticmethod
    def hash(block):
        # 블록을 해시값을 출력한다
        pass
    
    @property
    def last_block(self):
        # 체인의 가장 블록을 반환한다
        pass

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
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
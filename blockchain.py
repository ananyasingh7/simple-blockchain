import hashlib
import time

class Transaction:
    def __init__(self, sender, recipient, amount) -> None:
        self.sender = sender
        self.recipient = recipient;
        self.amount = amount
    
    def __str__(self):
        return f"{self.sender} -> {self.recipient}: {self.amount}"

class Block:
    def __init__(self, transactions, previous_hash) -> None:
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_contents = (
            str(self.timestamp) +
            str(self.transactions) + 
            str(self.previous_hash) +
            str(self.nonce)
        )
        return hashlib.sha256(block_contents.encode()).hexdigest()
    
    def mine_block(self, difficulty):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

    def __str__(self):
        transactions_str = "/n".join(str(tx) for tx in self.transactions)
        return f"""
Block:
Hash: {self.hash}
Previous Hash: {self.previous_hash}
Timestamp: {self.timestamp}
Transactions:
    {transactions_str}
Nonce: {self.nonce}
"""

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_transactions = []
        self.mining_reward = 10
    
    def create_genesis_block(self):
        return Block([], "0")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def mine_pending_transactions(self, miner_reward_address):
        block = Block(self.pending_transactions, self.get_latest_block().hash)
        

# Example usage
tx1 = Transaction("Alice", "Bob", 50)
tx2 = Transaction("Bob", "Charlie", 30)
tx3 = Transaction("Charlie", "David", 10)

block1 = Block([tx1, tx2], "0")
print(block1)

block2 = Block([tx3], block1.hash)
print(block2)

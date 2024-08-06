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
    def __init__(self, records, previous_hash) -> None:
        self.timestamp = time.time()
        self.records = records
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_contents = (
            str(self.timestamp) +
            str(self.records) + 
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
        print(f"Nonce: {self.nonce}")

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
        block.mine_block(self.difficulty)

        print("Block successfully mined!")
        self.chain.append(block)

        self.pending_transactions = [
            Transaction("System", miner_reward_address, self.mining_reward)
        ]

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def get_balance(self, address):
        balance = 0
        for block in self.chain:
            for record in block.records:
                if record.sender == address:
                    balance -= record.amount
                if record.recipient == address:
                    balance += record.amount
        return balance


# Example usage:
blockchain = Blockchain()

blockchain.chain = [
    Block([
        Transaction("System", "Alice", 50),  # Alice receives 50 coins
        Transaction("Alice", "Bob", 30),     # Alice sends 30 coins to Bob
    ], "0"),
    Block([
        Transaction("Bob", "Charlie", 10),   # Bob sends 10 coins to Charlie
        Transaction("System", "Alice", 5),   # Alice mines a block and receives 5 coins
    ], "previous_hash")
]

print(f"Alice's balance: {blockchain.get_balance('Alice')}")
print(f"Bob's balance: {blockchain.get_balance('Bob')}")
print(f"Charlie's balance: {blockchain.get_balance('Charlie')}")
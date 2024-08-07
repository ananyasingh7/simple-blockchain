# Simple Blockchain Implementation

## Overview

This project implements a basic blockchain system that simulates a simple cryptocurrency. It demonstrates core concepts of blockchain technology, including transactions, mining, and maintaining a decentralized ledger.

## Features

- Creation and management of a basic digital currency
- Decentralized ledger for recording transactions
- Proof of Work (PoW) consensus mechanism
- Peer-to-peer value transfer
- Currency minting through mining rewards

## Components

1. **Transaction**: Represents a transfer of currency between addresses.
2. **Block**: Contains a set of transactions and links to the previous block in the chain.
3. **Blockchain**: Manages the entire chain, including mining new blocks and validating the chain.

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/simple-blockchain.git
   cd simple-blockchain
   ```

2. No additional libraries are required as this implementation uses only Python standard libraries.

### Usage

To use the blockchain, you can run the following Python code:

```python
from blockchain import Blockchain, Transaction

# Initialize blockchain
blockchain = Blockchain()

# Add transactions
blockchain.add_transaction(Transaction("Alice", "Bob", 50))
blockchain.add_transaction(Transaction("Bob", "Charlie", 30))

# Mine a block
print("Mining first block...")
blockchain.mine_pending_transactions("Miner1")

# Add more transactions
blockchain.add_transaction(Transaction("Charlie", "Alice", 20))
blockchain.add_transaction(Transaction("Bob", "Alice", 10))

# Mine another block
print("Mining second block...")
blockchain.mine_pending_transactions("Miner2")

# Check balances
print(f"Balance of Alice: {blockchain.get_balance('Alice')}")
print(f"Balance of Bob: {blockchain.get_balance('Bob')}")
print(f"Balance of Charlie: {blockchain.get_balance('Charlie')}")
print(f"Balance of Miner1: {blockchain.get_balance('Miner1')}")
print(f"Balance of Miner2: {blockchain.get_balance('Miner2')}")

# Validate the blockchain
print(f"Blockchain valid: {blockchain.is_chain_valid()}")
```

## Key Concepts

- **Mining**: The process of adding new blocks to the chain by solving a computational puzzle.
- **Proof of Work**: A consensus mechanism that requires miners to perform computational work to add new blocks.
- **Transactions**: Represent the transfer of currency between addresses.
- **Blocks**: Contain a set of transactions and are linked together to form the blockchain.
- **Chain Validation**: Ensures the integrity of the entire blockchain.

## Limitations

This is a simplified implementation for educational purposes and lacks many features of real-world blockchain systems, including:

- Network distribution (multiple nodes)
- Advanced consensus mechanisms
- Smart contracts
- Privacy features
- Scalability solutions
- Governance mechanisms

## Contributing

Contributions to improve the implementation or add new features are welcome. Please feel free to submit a pull request or open an issue to discuss potential changes.

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This implementation is for educational purposes only and should not be used in production environments or for managing real assets.
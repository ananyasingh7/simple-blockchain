import hashlib

def simplified_mine(block_data, difficulty):
    nonce = 0
    target = "0" * difficulty

    while True:
        # Combine the block data with the nonce
        data_with_nonce = f"{block_data}{nonce}"
        
        # Calculate the hash
        hash_result = hashlib.sha256(data_with_nonce.encode()).hexdigest()
        
        # Check if the hash meets the difficulty requirement
        if hash_result.startswith(target):
            return nonce, hash_result
        
        # If not, increment the nonce and try again
        nonce += 1

# Example usage
block_data = "Transactions: Alice pays Bob 50 BTC"
difficulty = 5

found_nonce, valid_hash = simplified_mine(block_data, difficulty)

print(f"Found valid nonce: {found_nonce}")
print(f"Resulting hash: {valid_hash}")
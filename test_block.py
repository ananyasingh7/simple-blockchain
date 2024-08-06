from datetime import datetime, timedelta
import unittest

from blockchain import Block

class TestMineBlock(unittest.TestCase):
    def setUp(self):
        self.block = Block(["test transaction"], "previous_hash")

    def test_mine_block_difficulty_1(self):
        self.block.mine_block(1)
        self.assertTrue(self.block.hash.startswith("0"))

    def test_mine_block_difficulty_3(self):
        self.block.mine_block(3)
        self.assertTrue(self.block.hash.startswith("000"))

    def test_mine_block_nonce_incremented(self):
        initial_nonce = self.block.nonce
        self.block.mine_block(1)
        self.assertGreater(self.block.nonce, initial_nonce)

    def test_mine_block_hash_changed(self):
        initial_hash = self.block.hash
        self.block.mine_block(1)
        self.assertNotEqual(self.block.hash, initial_hash)

    def test_mine_block_performance(self):
        start_time = datetime.now()
        self.block.mine_block(4)
        end_time = datetime.now()
        mining_time = end_time - start_time
        self.assertLess(mining_time, timedelta(seconds=10), "Mining took too long")

if __name__ == '__main__':
    unittest.main()
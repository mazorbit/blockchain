from os import times
import time
from rich import print
from backend.util.crypto_hash import crypto_hash

class RrrBlock:
    """
    RrrBlock: Combination of information
    """

    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    def __repr__(self):
        return (
            '\nRrrBlock( '
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data} )'
        )

    @staticmethod
    def mine_block(last_block, data):
        """
        Mine a block based on given last_block and data.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        hash = crypto_hash(timestamp, last_hash)

        return RrrBlock(timestamp, last_hash, hash, data)

    @staticmethod
    def create_genesis_block():
        """
        Creating the genesis block.
        """
        return RrrBlock(time.time_ns(), "None", "genesis_hash", "This is all father of blocks")

def main():
    gen_block = RrrBlock.create_genesis_block()
    block2 = RrrBlock.mine_block(gen_block, '2nd block')
    block3 = RrrBlock.mine_block(block2, '3rd block')
    
    print(gen_block)
    print(block2)
    print(block3)

if __name__ == "__main__":
    main()
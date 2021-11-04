import time
from rich.console import Console
con = Console()

def mine_block(last_block, data):
    """
    Mine a block based on given last_block and data.
    """
    timestamp = time.time_ns()
    last_hash = last_block.hash
    hash = f"{timestamp}-{last_hash}"

    return Block(timestamp, last_hash, hash, data)

def genesis():
    """
    Generate the genesis block.
    """

    return Block(1, "gen_last_hash", "gen_hash", [])

class Block:
    """
    Block: Combination of information
    """

    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data})'
        )

def main():
    gen_block = genesis()
    block = mine_block(gen_block, 'foo')
    con.print(block)

if __name__ == "__main__":
    main()
from rich import print
from rrrblock import RrrBlock, mine_block, genesis

class RrrBlockchain:
    """
    RrrBlockchain: Distributed ledger of blocks.
    """

    def __init__(self):
        self.chain = [genesis()]

    def __repr__(self):
        return f"RrrBlockchain: {self.chain}"

    def add_block(self, data):
        self.chain.append(RrrBlock(data))

    def mine_block(last_block, data):
        """
        Mine a block based on given last_block and data.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        hash = f"{timestamp}-{last_hash}"

        return RrrBlock(timestamp, last_hash, hash, data)

    def genesis():
        """
        Generate the genesis block.
        """
        return RrrBlock(time.time_ns(), "None", "genesis_hash", "This is all father of blocks")


def main():
    bc = RrrBlockchain()

    # bc.add_block("one")
    # bc.add_block("two")

    print(bc)

    # print(f"bc.py.__name__: {__name__}")

if __name__ == "__main__":
    main()



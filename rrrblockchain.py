from rich import print
from rrrblock import RrrBlock

class RrrBlockchain:
    """
    RrrBlockchain: Distributed ledger of blocks.
    """

    def __init__(self):
        self.chain = [RrrBlock.create_genesis_block()]

    def __repr__(self):
        return f"RrrBlockchain: {self.chain}"

    def add_block(self, data):
        self.chain.append(RrrBlock.mine_block(self.chain[-1], data))

def main():
    bc = RrrBlockchain()

    bc.add_block("one")
    bc.add_block("two")

    print(bc)

    # print(f"bc.py.__name__: {__name__}")

if __name__ == "__main__":
    main()



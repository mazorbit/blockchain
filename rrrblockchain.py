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

def main():
    bc = RrrBlockchain()

    # bc.add_block("one")
    # bc.add_block("two")

    print(bc)

    # print(f"bc.py.__name__: {__name__}")

if __name__ == "__main__":
    main()



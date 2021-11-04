from rich.console import Console
from rrrblock import Block

class Blockchain:
    """
    Blockchain: Distributed ledger of blocks
    """

    def __init__(self):
        self.chain = []
        self.con = Console()

    def __repr__(self):
        return f"Blockchain: {self.chain}"

    def add_block(self, data):
        self.chain.append(Block(data))

def main():
    bc = Blockchain()

    bc.add_block("one")
    bc.add_block("two")

    bc.con.print(bc)

    print(f"bc.py.__name__: {__name__}")

if __name__ == "__main__":
    main()



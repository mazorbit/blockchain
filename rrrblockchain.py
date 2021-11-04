from rich.console import Console

class Block:
    """
    Block: Combination of information
    """

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Block - data: {self.data}"

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

bc = Blockchain()

bc.add_block("one")
bc.add_block("two")

bc.con.print(bc.chain)
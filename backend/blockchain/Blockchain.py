from rich.console import Console
con = Console()

def lightning_hash(data):
    return data + "*"

class Block:
    def __init__(self, data, hash, last_hash):
        self.data = data
        self.hash = hash
        self.last_hash = last_hash

class Blockchain:
    def __init__(self):
        genenis_block = Block("gen_data", "gen_hash", "gen_last_hash")
        self.chain = [genenis_block]

    def add_block(self, data):
        last_hash = self.chain[-1].hash
        this_hash = lightning_hash(data + "_" + last_hash) 
        new_block = Block(data, this_hash, last_hash)
        
        self.chain.append(new_block)

bc = Blockchain()
bc.add_block("one")
bc.add_block("two")

for block in bc.chain:
    con.print(block.__dict__)

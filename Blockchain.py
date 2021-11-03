class Block:
    def __init__(self, data, hash, last_hash):
        self.data = data
        self.hash = hash
        self.last_hash = last_hash

    def lightning_hash(data):
        return data + "_*"

# foo_block = Block('Hello', 'hash', 'last_hash')

# print(foo_block.data)
# print(foo_block.hash)
# print(foo_block.last_hash)

class Blockchain:
    def __init__(self):
        genenis_block = Block("gen_data", "gen_hash", "gen_last_hash")
        self.chain = [genenis_block]

bc = Blockchain()
print(bc.chain, type(bc.chain))




import hashlib
import json

def crypto_hash(*args):
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = ''.join(stringified_args)
    
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

if __name__ == "__main__":
    data = crypto_hash('dsadasdas', 0xf3dd, ('3'), ['4','5'], 14.5)
    print(data, len(data))
    
    data = crypto_hash(0xf3dd, 'dsadasdas', ('3'), 14.5, ['4','5'])
    print(data, len(data))
    

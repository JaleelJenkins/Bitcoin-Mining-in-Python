"""
Mining is the process of guessing a nonce that generates hash with first X number of zeros. 

Nonce is a for loop beginning at 1 going until it produces a hash where the first four digits are zero. The process of guessing a nonce is bitcoin mining.

Miners get a reward, every 4 years the reward gets halfed.

2009: 50 Bitcoins per block

2012: 25 BTC

2016: 12.5

2020: 6.25
"""

from hashlib import sha256
MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yay! Successfully mined bitcoins with nonce value: {nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")

if __name__ == '__main__':
    transactions='''
    Dhaval -> Bhavin -> 20, 
    Mando -> Cara -> 45
    '''

    difficulty=6 # increasing the difficulty will increase the script processing time. Current mining is at 20.
    import time
    start = time.time()
    print("start mining")
    new_hash = mine(5, transactions, '00000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    total_time = str((time.time() - start))
    print(f"end mining. Minig took: {total_time} seconds")
    print(new_hash)
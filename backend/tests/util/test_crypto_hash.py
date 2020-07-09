from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
    #It should return the same hash with arguments of different
    # data types in any order.
    
    #The assert keyword is used when debugging code.
    # The assert keyword lets you test if a condition in your code returns True, 
    # if not, the program will raise an AssertionError.   

    assert crypto_hash(1,[2],'three') == crypto_hash('three',1,[2])

    # assert crypto_hash('foo') == 'b2213295d564916f89a6a42455567c87c3f480fcd7a1c15e220f17d7169a790b'
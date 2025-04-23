#mini_aes.ppy
#Implementasi Mini-AES 16-bit (3 ronde)

# S-Box 4-Bit
SBOX = {
    0x0: 0x9, 0x1: 0x4, 0x2: 0xA, 0x3: 0xB,
    0x4: 0xD, 0x5: 0x1, 0x6: 0x8, 0x7: 0x5,
    0x8: 0x6, 0x9: 0x2, 0xA: 0x0, 0xB: 0x3,
    0xC: 0xC, 0xD: 0xE, 0xE: 0xF, 0xF: 0x7
}

#Fungsi SubNibbles
def sub_nibbles(state):
    return [SBOX[n] for n in state]

# Fungsi shiftRows (swap baris ke-2)
def shift_rows(state):
    return [state[0], state[1], state[3], state[2]]

# Fungsi perkalian di GF (2^4)
def gf_mult(a,b):
    p = 0
    for _ in range(4):
        if b & 1:
            p ^= a
            hi_bit_set = a & 0x8
            a <<= 1
            if hi_bit_set:
                a ^= 0x13  # irreducible polynomial x^4 + x + 1
            b >>= 1
    return p & 0xF

# Fungsi MixColumns untuk 2x2 matrix
# |1 4|   [s0 s1]
# |4 1|   [s2 s3]
def mix_columns(state):
    s0 = state[0]
    s1 = state[1]
    s2 = state[2]
    s3 = state[3]
    return [
        gf_mult(1, s0) ^ gf_mult(4, s2),
        gf_mult(1, s1) ^ gf_mult(4, s3),
        gf_mult(4, s0) ^ gf_mult(1, s2),
        gf_mult(4, s1) ^ gf_mult(1, s3),
    ]

# Fungsi AddRoundKey
# XOR antara state dan key
def add_round_key(state, key):
    return [s ^ k for s, k in zip(state, key)]

# Fungsi Enkripsi Mini-AES (3 ronde)
def encrypt(plaintext, round_keys):
    state = add_round_key(plaintext, round_keys[0])

    # Dua ronde utama
    for i in range(1, 3):
        state = sub_nibbles(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[i])

    # Ronde terakhir (tanpa MixColumns)
    state = sub_nibbles(state)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[3])

    return state

# Contoh Penggunaan
if __name__ == "__main__":
    # Plaintext dan round keys (4 nibble = 16-bit)
    plaintext = [0x1, 0x2, 0x3, 0x4]  # contoh input
    round_keys = [
        [0x0, 0x0, 0x0, 0x0],  # k0
        [0x1, 0x1, 0x1, 0x1],  # k1
        [0x2, 0x2, 0x2, 0x2],  # k2
        [0x3, 0x3, 0x3, 0x3]   # k3
    ]

    # Lakukan enkripsi
    cipher = encrypt(plaintext, round_keys)
    print("Ciphertext:", [hex(c) for c in cipher]) # Tampilkan hasil enkripsi dalam format heksadesimal

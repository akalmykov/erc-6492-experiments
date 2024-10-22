from erc6492_signature_verifier import SignatureVerifier

# Initialize the verifier with your Web3 provider URL
verifier = SignatureVerifier("https://mainnet.base.org")

# Example data
signature = "0x000000000000000000000000ca11bde05977b3631167028862be2a173976ca110000000000000000000000000000000000000000000000000000000000000060000000000000000000000000000000000000000000000000000000000000028000000000000000000000000000000000000000000000000000000000000001e482ad56cb0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000200000000000000000000000000ba5ed0c6aa8c49038f819e587e2633c4a9f428a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000e43ffba36f00000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000040e583905e0537a80abc6ad1597aeb1dfa88f8e445632d2c5e25ca7b136a902fbacd82c4c14859af59c5eef6b85d52f8b5838d96adb6ee0ed8b06ea5f963c658ea000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002800000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000120000000000000000000000000000000000000000000000000000000000000001700000000000000000000000000000000000000000000000000000000000000012608a5323e8090e779f78171adf4603f799ec3e9d5c1cfe087b64896dcd80964562fde345d8278c0b2baad7731ba2b84cbec1a52c650b817b15b9bc4e7abe1280000000000000000000000000000000000000000000000000000000000000025f198086b2db17256731bc456673b96bcef23f51d1fbacdd7c4379ef65465572f1d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000008a7b2274797065223a22776562617574686e2e676574222c226368616c6c656e6765223a2248454b577932616a6d36564348304572467876416f645265335a67596d65453243777a3255436e72484a30222c226f726967696e223a2268747470733a2f2f6b6579732e636f696e626173652e636f6d222c2263726f73734f726967696e223a66616c73657d000000000000000000000000000000000000000000006492649264926492649264926492649264926492649264926492649264926492"  # Replace with the actual signature
message = """localhost:5173 wants you to sign in with your Ethereum account:\n0x26692e752267b18e96f6386e4bE2ca58993148Fa\n\nSmart Wallet SIWE Example\n\nURI: http://localhost:5173\nVersion: 1\nChain ID: 84532\nNonce: 12345678\nIssued At: 2024-10-22T22:00:28.890Z"""

signer = "0x26692e752267b18e96f6386e4bE2ca58993148Fa"  # Replace with the actual signer's Ethereum address

# Verify the signature
is_valid = verifier.verify_signature(signature, message, signer)
print(f"Signature valid: {is_valid}")

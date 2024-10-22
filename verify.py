from siwe import SiweMessage


eip_4361_string = """localhost:5173 wants you to sign in with your Ethereum account:
0x26692e752267b18e96f6386e4bE2ca58993148Fa

Smart Wallet SIWE Example

URI: http://localhost:5173
Version: 1
Chain ID: 84532
Nonce: 12345678
Issued At: 2024-10-22T21:35:08.548Z"""

message = SiweMessage(
    domain="login.xyz",
    address="0x9D85ca56217D2bb651b00f15e694EB7E713637D4",
    chain_id=1,
    uri="https://login.xyz",
    version="1",
    statement="Sign-In With Ethereum Example Statement",
    nonce="bTyXgcQxn2htgkjJn",
    issued_at="2022-01-27T17:09:38.578Z",
    expiration_time="2100-01-07T14:31:43.952Z",
)
try:
    message.verify(
        signature="0xdc35c7f8ba2720df052e0092556456127f00f7707eaa8e3bbff7e56774e7f2e05a093cfc9e02964c33d86e8e066e221b7d153d27e5a2e97ccd5ca7d3f2ce06cb1b"
    )
    print("Valid")
except Exception as e:
    print("Invalid", e)

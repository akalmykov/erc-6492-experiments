import React, { useCallback, useEffect, useMemo, useState } from "react";
import { useAccount, usePublicClient, useSignMessage } from "wagmi";
import { SiweMessage } from "siwe";
import type { Hex } from "viem";

export function SignInWithEthereum() {
  const [signature, setSignature] = useState<Hex | undefined>(undefined);
  const { signMessage } = useSignMessage({
    mutation: { onSuccess: (sig) => setSignature(sig) },
  });
  const account = useAccount();
  const [valid, setValid] = useState<boolean | undefined>(undefined);
  const client = usePublicClient();

  const siweMessage = useMemo(() => {
    // return new SiweMessage("Hello, world!");
    const siweMsg = new SiweMessage({
      domain: document.location.host,
      address: account.address,
      chainId: account.chainId,
      uri: document.location.origin,
      version: "1",
      statement: "Smart Wallet SIWE Example",
      nonce: "12345678", // replace with nonce generated by your backend
    });
    console.log("domain", siweMsg.domain);
    console.log("address", siweMsg.address);
    console.log("chainId", siweMsg.chainId);
    console.log("uri", siweMsg.uri);
    console.log("version", siweMsg.version);
    console.log("statement", siweMsg.statement);
    console.log("nonce", siweMsg.nonce);
    console.log("siweMsg.toMessage", siweMsg.toMessage());
    console.log("siweMsg.prepareMessage", siweMsg.prepareMessage());
    return siweMsg;
  }, []);

  const promptToSign = () => {
    signMessage({ message: siweMessage.prepareMessage() });
  };

  const checkValid = useCallback(async () => {
    if (!signature || !account.address || !client) return;
    const isValid = await client.verifyMessage({
      address: account.address,
      message: siweMessage.prepareMessage(),
      signature,
    });
    setValid(isValid);
  }, [signature, account]);

  useEffect(() => {
    checkValid();
  }, [signature, account]);

  return (
    <div>
      <h2>SIWE Example</h2>
      <button onClick={promptToSign}>Sign In with Ethereum</button>
      {signature && <p>Signature: {signature}</p>}
      {valid !== undefined && <p>Is valid: {valid.toString()}</p>}
    </div>
  );
}

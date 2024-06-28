## Cryptex for Navi!
### Installation:  
1. Launch Navi `navi`
2. Search Cryptex `chips search cryptex`
3. Install Cryptex `chips install navi-cryptex`
As of this point Navi should reload with the new chip installed.
### Using Cryptex in Navi  
**Listing availible ciphers**
- Run the command `cryptex` to bring up the list of encryptions
  
**Getting Help**
- `cryptex <short code>` or for example `cryptex hex`
    
> It should be noted that different ciphers will offer different arguments to be used. Be sure to pay attention to this.
 
**Encrypting with Navi**
- `cryptex hex -e -t "Hello world!"` Will give you the following hex encoding 2248656c6c6f20776f726c642122.
    
**Decrypting with Navi**  
- `cryptex hex -d -t "2248656c6c6f20776f726c642122"` Will decode the hex back into: Hello World!

![image](https://github.com/SaintsSec/navi-cryptex/assets/89718570/76e1dc24-6125-434f-925d-af3c9d509cbe)


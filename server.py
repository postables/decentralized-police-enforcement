from web3 import Web3, HTTPProvider, IPCProvider
import web3
import ipfsapi
import hashlib

ipfs = ipfsapi.connect('127.0.0.1', 5001)

# connect to local node
w3 = Web3(HTTPProvider('http://localhost:8545'))

w3_contract = web3.contract.Contract('address of contract')

# uploads hash
w3_contract.transact().addEntry('someaddr', 'somehash', 'somechecksum')


class Web3():

    def __init__(tokenContractAddress):
        self.w3 = Web3(HTTPProvider('http://localhost:8545'))
        self.tokenContractAddress = tokenContractAddress
        self.w3_contract = web3.Contract(tokenContractAddress)
        # create hashlib handler for sha256
        self.hasher = hashlib.blake2b()
        # to use this we would do something like so:
        # self.hasher.update(b'ipfs hash')
        # to return: self.hasher.hexdigest()

    

    def addChecksum(recorder, ipfshash):
        checksum = self.hasher.update(b'%s' % ipfshash)
        self.w3_contract.transact().addEntry(str(recorder), str(ipfshash), str(checksum))


class Ipfs():

    def __init__(ip, port):
        self.ipfs_api = ipfsapi.connect(ip, port)

    
    def uploadFile(objectID):
        response = self.ipfs_api.add(objectID)
        ipfshash = self.ipfs_api.cat(response['Hash']).strip('\n')
        return ipfshash





def init():
    webb3 = Web3('someaddr')
    ipfss = Ipfs('ip', 'port')


def storeToIpfsAndSaveChecksum(recorder, ipfshash):
    ipfshash = ipfss.uploadFile('some id')
    webb3.addChecksum(recorder, ipfshash)
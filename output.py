def genesis_block_generation():
    print("\nGenesis Block is generated. The Blockchain system is up...!")
    print("Miners will now collect transactions from memPool and start building blocks...\n\n")


def block_info(block, consensus_algorithm):
    print("The following block has been proposed by " + block['generator_id'] +
          " and is generated into the Blockchain network")
    print("**************************")
    print("transactions:")
    print(block['transactions'])
    print("hash:")
    print(block['hash'])
    print("timestamp:")
    print(block['timestamp'])
    if consensus_algorithm == 1:
        print("nonce:")
        print(block['nonce'])
    print("previous_hash:")
    print(block['previous_hash'])
    print("**************************")


def block_success_addition(self_address, generator_id):
    print("*******************************************")
    print("the block is now added to the local chain of " + self_address)
    if generator_id != self_address:
        print("this block was received from " + generator_id)
        print("##############################\n")


def mempool_info(mempool):
    print('mempool contains the following TXs:')
    txs = []
    for i in range(mempool.qsize()):
        txs.append(mempool.get())
    for tx in txs:
        print(tx)
        mempool.put(tx)


def authorization_trigger(blockchain_placement, no_fogs, no_miners):
    print("please input the address of authorized:")
    if blockchain_placement == 1:
        print("Fog Nodes")
    else:
        print("End-users")
    print("to generate new blocks in the exact following format:")
    print(">>>> 1 OR 3 OR 50 ... (up to: ")
    if blockchain_placement == 1:
        print(str(no_fogs) + " fog nodes available")
    else:
        print(str(no_miners) + " miners available in the EU layer")
    print("Once done, kindly input: done")


def choose_functionality():
    print("Please choose the function of the Blockchain network:\n"
          "(1) Data Management\n"
          "(2) Computational services\n"
          "(3) Payment\n"
          "(4) Identity Management\n")


def choose_placement():
    print("Please choose the placement of the Blockchain network:\n"
          "(1) Fog Layer\n"
          "(2) End-User layer\n")


def choose_consensus():
    print("Please choose the Consensus algorithm to be used in the simulation:\n"
          "(1) Proof of Work: PoW\n"
          "(2) Proof of Stake: PoS\n"
          "(3) Proof of Authority: PoA\n")


def txs_success(txs_per_user, parent_add, self_add):
    print(str(txs_per_user) + " data records had been generated by End-User no. " + str(parent_add) + "." + str(self_add))


def GDPR_warning():
    print("###########################################"
          "\nWARNING: Each end-user's address and the address of the fog component it is connected with,\n "
          "will be immutably saved on the chain. This is not a GDPR-compliant practice.\n"
          "if you need to have your application GDPR-compliant, you need to change the configuration,\n"
          " so that other types of identities be saved on the immutable chain, and re-run the simulation."
          "\n###########################################\n")


def miners_are_up():
    print("*****************\nMiner nodes are up and waiting for the genesis block...!\n")


def illegal_tx(tx, wallet_content):
    print("the following transaction is illegal:")
    print(tx)
    print("the end_user_wallet contains only " + str(wallet_content) + " digital coins..!")
    print("the transaction is withdrawn from the block")


def illegal_block():
    print("The proposed block is not valid."
          "\nTransactions will be sent back to the mempool and mined again..!")


def unauthorized_miner_msg(miner_address):
    print("Miner: " + miner_address + " is not authorized to generate a new block..!")


def block_discarded():
    print("The received block was ignored because it is already in the local chain")


def local_chain_is_updated(miner_address, length_of_local_chain):
    print("Using the Gossip protocol of FoBSim, the local chain of the following miner was updated:")
    print("Miner: " + str(miner_address))
    print("The length of the new local chain: " + str(length_of_local_chain))


def mempool_is_empty():
    print("mempool is empty")


def finish():
    print("simulation is done.")
    print("To check/analyze the experiment, please refer to the temporary folder.")
    print("There, you can find:")
    print("- miners' local chains")
    print("- miners' local records of users' wallets")
    print("- log of blocks confirmed by the majority of miners")
    print("- log of final amounts in miners' wallets (initial values - staked values + awards)")
    print("- log of values which were staked by miners")
    print("thank YOU..!")

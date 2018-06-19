def test_minter(chain):
    coin, _ = chain.provider.get_or_deploy_contract('Coin')
    assert "0x82A978B3f5962A5b0957d9ee9eEf472EE55B42F1" == coin.call().minter()


def test_mint(chain, accounts):
    coin, _ = chain.provider.get_or_deploy_contract('Coin')
    account = accounts[1]
    assert coin.call().minter() != account
    txn_hash = coin.transact().mint(account, 21)
    chain.wait.for_receipt(txn_hash)
    assert 21 == coin.call().balances(account)

    txn_hash = coin.transact().mint(account, 30)
    chain.wait.for_receipt(txn_hash)
    assert 51 == coin.call().balances(account)


def test_mint_from_another_account(chain, accounts):
    coin, _ = chain.provider.get_or_deploy_contract('Coin')
    account = accounts[1]
    assert coin.call().minter() != account
    transaction = {"from": account}
    txn_hash = coin.transact(transaction).mint(accounts[2], 30)
    chain.wait.for_receipt(txn_hash)
    assert 0 == coin.call().balances(accounts[2])


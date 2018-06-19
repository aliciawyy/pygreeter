def test_minter(chain):
    coin, _ = chain.provider.get_or_deploy_contract('Coin')
    assert "0x82A978B3f5962A5b0957d9ee9eEf472EE55B42F1" == coin.call().minter()


def test_mint(chain):
    pass
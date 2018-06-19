def test_greeting(chain):
    greeter, _ = chain.provider.get_or_deploy_contract('Greeter')

    greeting = greeter.call().greeting()
    assert greeting == 'Hello'


def test_custom_greeting(chain):
    greeter, _ = chain.provider.get_or_deploy_contract('Greeter')

    set_txn_hash = greeter.transact().setGreeting('Guten Tag')
    chain.wait.for_receipt(set_txn_hash)

    greeting = greeter.call().greeting()
    assert greeting == 'Guten Tag'


def test_named_greeting(chain):
    greeter, _ = chain.provider.get_or_deploy_contract("Greeter")
    assert "Hello Kitty" == greeter.call().greeting("Kitty")

pragma solidity ^0.4.22;

contract Greeter {
    string public greeting;

    function Greeter() public {
        greeting = 'Hello';
    }

    function setGreeting(string _greeting) public {
        greeting = _greeting;
    }

    function greeting(bytes name) public constant returns (bytes) {
        bytes memory b_greeting = bytes(greeting);
        bytes memory named_greeting = new bytes(
            b_greeting.length + 1 + name.length
        );
        uint i;

        for (i = 0; i < b_greeting.length; i++) {
            named_greeting[i] = b_greeting[i];
        }

        named_greeting[b_greeting.length] = ' ';

        for (i = 0; i < name.length; i++) {
            named_greeting[b_greeting.length + 1 + i] = name[i];
        }

        return named_greeting;
    }
}

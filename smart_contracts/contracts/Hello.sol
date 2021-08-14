// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Hello {
    string name;

    constructor(string memory _name) {
        name = _name;
    }

    function callName() public view returns (string memory) {
        return name;
    }
}

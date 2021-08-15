// SDPX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "OpenZeppelin/openzeppelin-contracts@4.0.0/contracts/token/ERC20/ERC20.sol";


contract ZeppelinERC20 is ERC20 {
    constructor(uint256 initialSupply) ERC20("Hung Token ERC20", "HUNGERC20") {
        _mint(msg.sender, initialSupply);
    }
}
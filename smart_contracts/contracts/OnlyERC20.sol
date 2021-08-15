// SDPX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract OnlyERC20 {

    function name() public view returns (string memory) {
        return 'Hung Only ERC20 Token';
    }

    function symbol() public view returns (string memory) {
        return 'HUNG_ONLY_ERC20';
    }

    function decimals() public view returns (uint8) {
        return 18;
    }

    function totalSupply() public view returns (uint256) {
        return 1e21;
    }

    function balanceOf(address _owner) public view returns (uint256 balance) {
        return 8888888;
    }

    function transfer(address _to, uint256 _value) public returns (bool success) {
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        return true;
    }

    function approve(address _spender, uint256 _value) public returns (bool success) {
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    function allowance(address _owner, address _spender) public view returns (uint256 remaining) {
        return 123456;
    }

    event Transfer(address indexed _from, address indexed _to, uint256 _value);
    event Approval(address indexed _owner, address indexed _spender, uint256 _value);

}

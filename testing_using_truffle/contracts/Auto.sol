// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

contract Purchase {
    address[20] public buyers;

    // buying a car
    function buy(uint256 carId) public returns (uint256) {
        require(carId >= 0 && carId <= 19);

        buyers[carId] = msg.sender;

        return carId;
    }

    // get all buyers
    function getBuyers() public view returns (address[20] memory) {
        return buyers;
    }
}

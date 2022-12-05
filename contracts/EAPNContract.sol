// contracts/GameItem.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract EzAsPyNews is ERC721URIStorage {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    uint256 public mintRate= 1.00 ether;

    constructor() ERC721("EzAsPyNews", "EAPN") {}

    function awardItem(address to, string memory tokenURI)
        public payable returns (uint256)
    {
        require(msg.value >= mintRate, "Please make sure you are entering a value of one ether.");
        uint256 newItemId = _tokenIds.current();
        _mint(to, newItemId);
        _setTokenURI(newItemId, tokenURI);

        _tokenIds.increment();
        return newItemId;
    }

    function getRecentTokenURI() public view returns (string memory)
    {
        uint256 currentTokenID = _tokenIds.current() - 1;
        return tokenURI(currentTokenID);
    }
}
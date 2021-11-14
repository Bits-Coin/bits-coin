What is Bits-Coin?
----------------

Bits-Coin (BITS) is a rapidly growing decentralized, global blockchain that was founded in late 2021 with a focus on cyber security, payments & secure communications technologies.

For more information, as well as an immediately useable, binary version of the Bits-Coin Core software, refer below links

Official mining Pool : https://urpool.io   
Official Wallet:  https://webwallet.Bits-coin.io  
Official Explorer:  https://explorer.Bits-coin.io
Official Web site: https://Bits-coin.io (under consruction)
Official General crypto-currency info : www.Electro-bits.com 



Bits-Coin FAQ
-------------
Launch Date: October 15th, 2021 Hard fork blockchain from Digibyte core v7.17.2 released under the terms of the MIT Open Source License Agreement

Blockchain Type: Public, Decentralized, UTXO based, Multi-Algorithm

Ticker Symbol: BITS

Genesis Block Hash: "The Evolution of Technology opens doors to a new decentralized financial freedom era "

Max Total Supply: 21 Billion Bits-Coins in 39 Years (2059)

Current Supply: 108,499,970 BITS (Oct 2021)

Block Reward Reduction: Reward Halving - 50% (Every 5 Years/10512000 Blocks)

Current Block Reward: 1000 BITS (Oct 2021)

Mining Algorithms: Five individual: SHA256, Scrypt, Groestl, Skein & Qubit

Block Interval: 15 Second Blocks (75 seconds per algo)

Algo Block Share: 20% Block Share Per Algo (5)

Difficulty Retarget: Every 1 Block, 5 Separate Difficulties, independent difficulty for each Mining Algo

SegWit Support: No. 





You can mine Bits-Coin on one of five separate mining algorithms. Each algo averages out to mine 20% of new blocks. This allows for much greater decentralization than other blockchains. An attacker with 99% of of any individual algorithm would still be unable to hardfork the blockchain, making Bits-Coin much more secure against PoW attacks than other blockchains.


Bits-Coin vs Bitcoin
-------------------

Security: 5 Bits-Coin mining algorithms vs. 1 Bitcoin mining algorithm.
Bits-Coin mining is much more decentralized.
Bits-Coin mining algorithms can be changed out in the future to prevent centralization.

Speed: Bits-Coin transactions occur much faster than Bitcoin transactions.
1-2 second transaction notifications.
15 second Bits-Coin blocks vs. 10 minute Bitcoin blocks.
Bits-Coin has 6x block confirmations 1.5 minutes vs. 1 hour with Bitcoin.

Transaction Volume: Bits-Coin can handle many more transactions per second.
Bitcoin can only handle 3-4 transactions per second.
Bits-Coin currently can handle 560+ transactions per second.


Total Supply: More Bits-Coin, lower price, more micro transactions, better price stability.
21 billion Bits-Coin will be created over 39 years.
Only 21 million Bitcoin will be created over 140 years.


Flexibility: Ability to quickly add new features.
Bits-Coin can add new features & upgrades much quicker than Bitcoin.
Future Bits-Coin upgrades will push transaction limit to several hundred thousand per second.

Marketability & Usability: Bits-Coin is an easy brand to market to consumers.
Bits-Coins are much cheaper to acquire.

License
-------

Bits-Coin Core is released under the terms of the MIT license. See [COPYING](COPYING) for more
information or see https://opensource.org/licenses/MIT.

Development Process
-------------------

The `master` branch is regularly built and tested, but is not guaranteed to be
completely stable. [Tags](https://github.com/Bits-Coin/bits-coin/) are created
regularly to indicate new official, stable release versions of BitsCoin Core.

The contribution workflow is described in [CONTRIBUTING.md](CONTRIBUTING.md).

Testing
-------

### Automated Testing

Developers are strongly encouraged to write [unit tests](src/test/README.md) for new code, and to
submit new unit tests for old code. Unit tests can be compiled and run
(assuming they weren't disabled in configure) with: `make check`. Further details on running
and extending unit tests can be found in [/src/test/README.md](/src/test/README.md).

There are also [regression and integration tests](/test), written
in Python, that are run automatically on the build server.
These tests can be run (if the [test dependencies](/test) are installed) with: `test/functional/test_runner.py`

The Travis CI system makes sure that every pull request is built for Windows, Linux, and macOS, and that unit/sanity tests are run automatically.

### Manual Quality Assurance (QA) Testing

Changes should be tested by somebody other than the developer who wrote the
code. This is especially important for large or high-risk changes. It is useful
to add a test plan to the pull request description if testing the changes is
not straightforward.


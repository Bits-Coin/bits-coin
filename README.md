What is BitsCoin?
----------------

BitsCoin (DGB) is a rapidly growing decentralized, global blockchain that was founded in early 2014 with a focus on cyber security, payments & secure communications technologies.

For more information, as well as an immediately useable, binary version of the BitsCoin Core software, see https://bitscoin.io

BitsCoin FAQ
-------------
Launch Date: January 10th, 2014

Blockchain Type: Public, Decentralized, UTXO based, Multi-Algorithm

Ticker Symbol: DGB

Genesis Block Hash: "USA Today: 10/Jan/2014, Target: Data stolen from up to 110M customers"

Max Total Supply: 21 Billion BitsCoins in 21 Years (2035)

Current Supply: 11,692,747,373 DGB (April 2019)

Block Reward Reduction: 1% Monthly

Current Block Reward: 688 DGB (April 2019)

Mining Algorithms: Five individual: SHA256, Scrypt, Groestl, Skein & Qubit

Block Interval: 15 Second Blocks (75 seconds per algo)

Algo Block Share: 20% Block Share Per Algo (5)

Difficulty Retarget: Every 1 Block, 5 Separate Difficulties, independent difficulty for each Mining Algo

SegWit Support: Yes. First major altcoin to successfully activate Segwit. (April 2017)

Hardforks: 4. DigiShield, MultiAlgo, MultiShield, DigiSpeed

Softforks: 3. SegWit, CSV, NVersionBits

You can mine BitsCoin on one of five separate mining algorithms. Each algo averages out to mine 20% of new blocks. This allows for much greater decentralization than other blockchains. An attacker with 99% of of any individual algorithm would still be unable to hardfork the blockchain, making BitsCoin much more secure against PoW attacks than other blockchains.

DigiShield Hardfork: Block 67,200, Feb. 28th, 2014

MultiAlgo Hardfork: Block 145k, Sep. 1st 2014

MultiShield Hardfork: Block 400k, Dec. 10th 2014

DigiSpeed Hardfork: Block 1,430,000 Dec. 4th 2015

BitsCoin vs Bitcoin
-------------------

Security: 5 BitsCoin mining algorithms vs. 1 Bitcoin mining algorithm.
BitsCoin mining is much more decentralized.
BitsCoin mining algorithms can be changed out in the future to prevent centralization.

Speed: BitsCoin transactions occur much faster than Bitcoin transactions.
1-2 second transaction notifications.
15 second BitsCoin blocks vs. 10 minute Bitcoin blocks.
BitsCoin has 6x block confirmations 1.5 minutes vs. 1 hour with Bitcoin.

Transaction Volume: BitsCoin can handle many more transactions per second.
Bitcoin can only handle 3-4 transactions per second.
BitsCoin currently can handle 560+ transactions per second.
The 2015 DigiSpeed hardfork introduced changes that double the capacity of the network every two years.

Total Supply: More BitsCoins, lower price, more micro transactions, better price stability.
21 billion BitsCoins will be created over 21 years.
Only 21 million Bitcoin will be created over 140 years.
1:1000 ratio. 1 BitsCoin for every 1000 Bitcoin.

Flexibility: Ability to quickly add new features.
BitsCoin can add new features & upgrades much quicker than Bitcoin.
Future BitsCoin upgrades will push transaction limit to several hundred thousand per second.

Marketability & Usability: BitsCoin is an easy brand to market to consumers.
BitsCoins are much cheaper to acquire.

License
-------

BitsCoin Core is released under the terms of the MIT license. See [COPYING](COPYING) for more
information or see https://opensource.org/licenses/MIT.

Development Process
-------------------

The `master` branch is regularly built and tested, but is not guaranteed to be
completely stable. [Tags](https://github.com/bitscoin/bitscoin/tags) are created
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


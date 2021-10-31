
Setup
---------------------
BitsCoin Core is the original BitsCoin client and it builds the backbone of the network. However, it downloads and stores the entire history of BitsCoin transactions (which is currently several GBs); depending on the speed of your computer and network connection, the synchronization process can take anywhere from a few hours to a day or more.
BitsCoin Core
=============

Setup
---------------------
BitsCoin Core is the original BitsCoin client and it builds the backbone of the network. It downloads and, by default, stores the entire history of BitsCoin transactions (which is currently more than 100 GBs); depending on the speed of your computer and network connection, the synchronization process can take anywhere from a few hours to a day or more.

To download BitsCoin Core, visit [bitscoincore.org](https://bitscoincore.org/en/releases/).

Running
---------------------
The following are some helpful notes on how to run BitsCoin Core on your native platform.

### Unix

Unpack the files into a directory and run:

- `bin/bitscoin-qt` (GUI) or
- `bin/bitscoind` (headless)

### Windows

Unpack the files into a directory, and then run bitscoin-qt.exe.

### macOS

Drag BitsCoin Core to your applications folder, and then run BitsCoin Core.

### Need Help?

* See the documentation at the [BitsCoin Wiki](https://en.bitscoin.it/wiki/Main_Page)
for help and more information.
* Ask for help on [#bitscoin](http://webchat.freenode.net?channels=bitscoin) on Freenode. If you don't have an IRC client use [webchat here](http://webchat.freenode.net?channels=bitscoin).
* Ask for help on the [BitsCoinTalk](https://bitscointalk.org/) forums, in the [Technical Support board](https://bitscointalk.org/index.php?board=4.0).

Building
---------------------
The following are developer notes on how to build BitsCoin Core on your native platform. They are not complete guides, but include notes on the necessary libraries, compile flags, etc.

- [Dependencies](dependencies.md)
- [macOS Build Notes](build-osx.md)
- [Unix Build Notes](build-unix.md)
- [Windows Build Notes](build-windows.md)
- [OpenBSD Build Notes](build-openbsd.md)
- [NetBSD Build Notes](build-netbsd.md)
- [Gitian Building Guide](gitian-building.md)

Development
---------------------
The BitsCoin repo's [root README](/README.md) contains relevant information on the development process and automated testing.

- [Developer Notes](developer-notes.md)
- [Release Notes](release-notes.md)
- [Release Process](release-process.md)
- [Source Code Documentation (External Link)](https://dev.visucore.com/bitscoin/doxygen/)
- [Translation Process](translation_process.md)
- [Translation Strings Policy](translation_strings_policy.md)
- [Travis CI](travis-ci.md)
- [Unauthenticated REST Interface](REST-interface.md)
- [Shared Libraries](shared-libraries.md)
- [BIPS](bips.md)
- [Dnsseed Policy](dnsseed-policy.md)
- [Benchmarking](benchmarking.md)

### Resources
* Discuss on the [BitsCoinTalk](https://bitscointalk.org/) forums, in the [Development & Technical Discussion board](https://bitscointalk.org/index.php?board=6.0).
* Discuss project-specific development on #bitscoin-core-dev on Freenode. If you don't have an IRC client use [webchat here](http://webchat.freenode.net/?channels=bitscoin-core-dev).
* Discuss general BitsCoin development on #bitscoin-dev on Freenode. If you don't have an IRC client use [webchat here](http://webchat.freenode.net/?channels=bitscoin-dev).

### Miscellaneous
- [Assets Attribution](assets-attribution.md)
- [Files](files.md)
- [Fuzz-testing](fuzzing.md)
- [Reduce Traffic](reduce-traffic.md)
- [Tor Support](tor.md)
- [Init Scripts (systemd/upstart/openrc)](init.md)
- [ZMQ](zmq.md)

License
---------------------
Distributed under the [MIT software license](/COPYING).
This product includes software developed by the OpenSSL Project for use in the [OpenSSL Toolkit](https://www.openssl.org/). This product includes
cryptographic software written by Eric Young ([eay@cryptsoft.com](mailto:eay@cryptsoft.com)), and UPnP software written by Thomas Bernard.

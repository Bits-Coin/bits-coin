// Copyright (c) 2011-2014 The BitsCoin Core developers
// Distributed under the MIT software license, see the accompanying
// file COPYING or http://www.opensource.org/licenses/mit-license.php.

#ifndef DIGIBYTE_QT_DIGIBYTEADDRESSVALIDATOR_H
#define DIGIBYTE_QT_DIGIBYTEADDRESSVALIDATOR_H

#include <QValidator>

/** Base58 entry widget validator, checks for valid characters and
 * removes some whitespace.
 */
class BitsCoinAddressEntryValidator : public QValidator
{
    Q_OBJECT

public:
    explicit BitsCoinAddressEntryValidator(QObject *parent);

    State validate(QString &input, int &pos) const;
};

/** BitsCoin address widget validator, checks for a valid bitscoin address.
 */
class BitsCoinAddressCheckValidator : public QValidator
{
    Q_OBJECT

public:
    explicit BitsCoinAddressCheckValidator(QObject *parent);

    State validate(QString &input, int &pos) const;
};

#endif // DIGIBYTE_QT_DIGIBYTEADDRESSVALIDATOR_H

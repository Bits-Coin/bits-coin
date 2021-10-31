// Copyright (c) 2009-2019 The Bitcoin Core developers
// Copyright (c) 2014-2019 The BitsCoin Core developers
// Distributed under the MIT software license, see the accompanying
// file COPYING or http://www.opensource.org/licenses/mit-license.php.

#ifndef DIGIBYTE_QT_WALLETMODELTRANSACTION_H
#define DIGIBYTE_QT_WALLETMODELTRANSACTION_H

#include <qt/walletmodel.h>

#include <memory>

#include <QObject>

class SendCoinsRecipient;

namespace interfaces {
class Node;
class PendingWalletTx;
}

/** Data model for a walletmodel transaction. */
class WalletModelTransaction
{
public:
    explicit WalletModelTransaction(const QList<SendCoinsRecipient> &recipients);

    QList<SendCoinsRecipient> getRecipients() const;

    std::unique_ptr<interfaces::PendingWalletTx>& getWtx();
    unsigned int getTransactionSize();

    void setTransactionFee(const CAmount& newFee);
    CAmount getTransactionFee() const;

    CAmount getTotalTransactionAmount() const;

    void reassignAmounts(int nChangePosRet); // needed for the subtract-fee-from-amount feature

private:
    QList<SendCoinsRecipient> recipients;
    std::unique_ptr<interfaces::PendingWalletTx> wtx;
    CAmount fee;
};

#endif // DIGIBYTE_QT_WALLETMODELTRANSACTION_H

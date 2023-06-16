import time


class Bank:
    def __init__(self):
        self.clients = []
        self.transaction = []
        self.bills = []

    def create_client(self, new_client):
        self.clients.append(new_client)

    def create_bill(self, client, account_number, balance):
        client_account = next((b for b in self.bills if b['client'] == client), None)
        if client_account:
           print("У клиента уже есть счет")
        else:
            self.bills.append({
                'client': client,
                'account_number': account_number,
                'balance': balance
            })

    def check_balance_enough(self, bill_number, summ):
        bill = next((b for b in self.bills if b["account_number"] == bill_number), None)
        if bill['balance'] >= summ:
            return True
        else:
            return False

    def transfer(self, client, transfer_from, transfer_to, summ):
        client = filter(client, self.clients)
        bill_from = next(b for b in self.bills if b["account_number"] == transfer_from)
        bill_to = next(b for b in self.bills if b["account_number"] == transfer_to)

        if self.check_balance_enough(bill_from['account_number'], summ):
            bill_from['balance'] -= summ
            bill_to['balance'] += summ

            self.transaction.append({
                'client': client,
                'transfer_from': transfer_from,
                'transfer_to': transfer_to,
                'time': time.time(),
                'summ': summ
            })
        else:
            print('Ошибка при осущевлении операции перевода')


bank = Bank()
bank.create_client('Mikhail')
bank.create_bill('Mikhail', '58585858585', 10000)

bank.create_client('Alena')
bank.create_bill('Alena', '59595959595', 5000)

bank.transfer('Mikhail', '58585858585', '59595959595', 10000000)
bank.transfer('Mikhail', '58585858585', '59595959595', 1000)

print(bank.bills[0])

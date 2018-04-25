import gdax
import time
import setup as stp
import login as lgn

auth_client = gdax.AuthenticatedClient(lgn.key, lgn.b64secret, lgn.passphrase)
btc = 'BTC-EUR' #for dollars chanige EUR to USD
eth = 'ETH-EUR' #for dollars chanige EUR to USD
ltc = 'LTC-EUR' #for dollars chanige EUR to USD

##########buy##########
def buy(prijs, hoeveelhijd):
    auth_client.buy(price=prijs,  # EUR
                    size=hoeveelhijd,  # BTC
                    product_id=curency())

##########sell##########
def sell(prijs, hoeveelhijd):
    auth_client.sell(price=prijs,  # EUR
                     size=hoeveelhijd,  # BTC
                     product_id=curency())


def main():
    print stp.test



##########_wtf_##########
if __name__ == "__main__":
    main()
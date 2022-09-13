btc = input('What is Bitcoin price today?\n')
dollar = input('How much $ do you have?\n')
total = (float(dollar) / float(btc))
print('You can buy:' + str(total) + 'BTC')

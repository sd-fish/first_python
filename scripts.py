prices = {
    "banana" :4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3,
}
stock = {
    "banana" :6,
    "apple" : 0,
    "orange" : 32,
    "pear" : 15,
}

for key in prices:
    print key
    print "prices: %d" % prices[key]
    print "stock: %d" % stock[key]

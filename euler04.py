prodlist = []
for i in range (999, 900, -1):
    for j in range (999, 900, -1):
        product = i * j
        product1 = str(product)
        product2 = product1[::-1]
        if product1 == product2:
            int(product2)
            prodlist.append(product2)
for x in prodlist:
    print x




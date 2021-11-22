#elements [0] della linea date
#elements[1] della linea sales

#apro e leggo il file
def somma_valori(input_file):
    total = 0
    values = []
    my_file = open (input_file, 'r')
    for line in my_file :
        elements = line.split (',')
        if elements [0] != 'Date':
            date = elements[0]
            value = elements[1]
            values.append(float(value))
      # value = float(line)
            total += float(elements[1])
   
    my_file.close()
    print('My sales: {}', total)
    return total

somma_valori("sales.txt")
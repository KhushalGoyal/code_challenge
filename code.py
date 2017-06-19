products = {}

def add(text):
    """Add items in the cart"""
    if text in products:
        for key in products.keys():
            val = products[key]
            if key == text:
                products[key] = val + 1
    else:
        products[text] = 0
    return products

def find(text):
    """Find the item matching the string pattern inputed by the user"""
    count = 0
    for y in products.keys():
        if text == y[0:len(text)]:
            count+=1
    return count


def list_items():
    """Prints all the items in the cart
    :return:
    """
    items = products.keys()
    return items


if __name__ == '__main__':
    import sys
    list1 = [i for i, x in enumerate(sys.argv) if x == "add"]
    for function in sys.argv:
        if function=="add":
            for x in list1:
                add(sys.argv[x+1])
        elif function=="find":
            val = sys.argv.index(function)+1
            value = sys.argv[val]
            print find(value)
        elif function=="list":
            items_list = list_items()
            for x in items_list[::-1]:
                print x
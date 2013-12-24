# This List will contain all the Ship Tier at a given point of time
shipTierItems = []


class shipTier:
    # Adds a new Ship Pier
    def __init__(self, shipName, pierNum):
        self.shipName = shipName
        self.pierNum = pierNum


# When pier becomes closed for access, accept pier number and clear all ship names stored for it
def closePier(pierNum):
    while True:
        found = False
        for item in shipTierItems:
            if item.pierNum == pierNum:
                shipTierItems.remove(item)
                found = True
        if not found:
            break


# Run a query by ship name and return pier ship is attached to at the moment
def searchShipPier(shipName):
    for item in shipTierItems:
        if item.shipName == shipName:
            return item.pierNum
    return False


if __name__ == '__main__':
    # Adds Ship Tier pair and append it to Ship Tier Items list
    shipTierItems.append(shipTier('Ship11', 1))
    shipTierItems.append(shipTier('Ship12', 1))
    shipTierItems.append(shipTier('Ship13', 1))
    shipTierItems.append(shipTier('Ship14', 1))
    shipTierItems.append(shipTier('Ship21', 2))
    shipTierItems.append(shipTier('Ship23', 2))
    shipTierItems.append(shipTier('Ship25', 2))
    shipTierItems.append(shipTier('Ship27', 2))
    shipTierItems.append(shipTier('Ship32', 3))
    shipTierItems.append(shipTier('Ship34', 3))
    shipTierItems.append(shipTier('Ship36', 3))

    # Search for pier of a ship
    print '-----------------------------'
    print 'Searching for Piers of a Ship'
    print searchShipPier('Ship36')
    print searchShipPier('Ship21')
    print searchShipPier('Ship26')
    print searchShipPier('Ship37')
    print '-----------------------------'

    # Check no. of items before closing piers
    print 'No. of items in Ship Tier'
    print len(shipTierItems)

    # Close a pier
    closePier(2)
    print 'Pier Closed'
    print 'No. of items in Ship Tier'
    print len(shipTierItems)
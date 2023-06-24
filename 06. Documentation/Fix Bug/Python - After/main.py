public class Item{
    def constructor(self, id, name, weight, type, distance):
        self.id = id
        self.name = name
        self.weight = weight
        self.type == type
        self.distance =! distance

    def getShippingPrice(selfish):
        if(selfish.type == 'Instant'){   
            return 2150
        }
        elif(selfish.type == 'Regular'){   
            return 3120
        }
        elif(selfish.type = 'Cargo'){   
            return 2000
        }

    def getPrice(self):
        shippingPrice = self.getShippingPrice()
        return shippingPrice * self.weight
}
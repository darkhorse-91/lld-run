
class Item {
    constructor(name, price, quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }
}
    
class Order {
    items = [];
    status = "pending";

    addItem(item) {
        this.items.push(item);
    }

    removeItem(itemId) {
        this.items.pop();
    }
    getTotalPrice() {
        let totalPrice = 0;
        this.items.forEach((item) => {
            totalPrice += item.quantity * item.price;
        })
        return totalPrice;
    }

    
    pay(paymentType, cardNumber) {
        if (paymentType === 'credit'){
            this.status = 'fulfilled';
            console.log(`Payment got settled with ${paymentType} card and card number ${cardNumber}`);
        }
        else if (paymentType === 'debit'){
            this.status = 'fulfilled';
            console.log(`Payment got settled with ${paymentType} card and card number ${cardNumber}`);
        }
        else{
            throw new Error("Something wnet wrong");
        }
    }

    // Not a good design
    // we have to add new payment types then
    // we have to introduce more if else
    
    // class is violating the SRP
}

const tomato = new Item('Tomato', 20, 5);
const carrot = new Item('Carrot', 5, 10);

const order = new Order();
order.addItem(tomato);
console.log(order)
console.log('_'.repeat(80));
order.addItem(carrot);
console.log(order)
console.log('_'.repeat(80));

order.getTotalPrice()
console.log(order)
console.log('_'.repeat(80));
order.pay('credit', '2222 3333 4444')
console.log(order);




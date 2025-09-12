import { PayMentMethod } from "./PayMentMethod.js";

export class PaypalPayMent extends PayMentMethod {
    pay(amount){
        console.log("Pago procesado con PayPal" + amount);
    }
}
import { PayMentMethod } from "./PayMentMethod.js";

export class CreditCardPayMent extends PayMentMethod {
    pay(amount) {
        console.log("Pago procesado con tarjeta de credito " + amount);
    }

}
import { PayMentMethod } from "./PayMentMethod.js";

export class BitcoinPayMent {
    pay(amount){
        console.log("Pago efectuado por Bitcoin $ " + amount);
    }
}
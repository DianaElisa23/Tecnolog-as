import { PayMentServices } from "./services/PayMentServices";
import { CreditCardPayMent } from "./models/CreditCardPayMent";
import { PaypalPayMent } from "./models/PayPalPayMent";
import { BitcoinPayMent } from "./models/BitcoinPayMent";

const services = new PayMentServices();
const creditCard = new CreditCardPayMent();
const paypal = new PaypalPayMent();
const bitcoin = new BitcoinPayMent();

services.serviceProcess(creditCard, 200);
services.serviceProcess(paypal, 500);
services.serviceProcess(bitcoin, 1000);  
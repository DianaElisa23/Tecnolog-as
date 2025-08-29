import {Animal} from "./Animal";

export class Gato extends Animal {
    constructor(name: String) {
        super(name);
    }

    makeSound(): void {
        console.log("Miau Miau");
    }
}
import Animal from "./Animal";

export class Volar extends Animal {
    constructor(name: String) {
        super(name);
    }

    makeSound(): void {
        console.log("Flap Flap");
    }
}
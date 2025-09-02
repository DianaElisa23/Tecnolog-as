class animal = object
  method eat = print_endline "comiendo"
end;;

class mamifero = object
  inherit animal
  method feed_offspring = print_endline "alimentando a la cría"
end;;

class perro = object
  inherit mamifero
  method bark = print_endline "woof"
end;;

let maka = new perro;;

maka#eat;;
maka#feed_offspring;;
maka#bark;;
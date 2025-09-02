class worker (name : string) (income: float) = object
  val mutable name = name
  val mutable income = income
end;;

class chief (name : string) (income: float) = object
  inherit worker name income
  method manage_team = print_endline "dirigiendo equipo"
end;;

class programmer (name : string) (income: float) = object
  inherit worker name income
  method code = print_endline "programando"
end;;

class occountant (name : string) (income: float) = object
  inherit worker name income
  method manage_accounts = print_endline "contando"
end;;

let jesica = new chief "Jesica" 100.5;;
let fernando = new programmer "Fernando" 50.5;;
let jairo = new occountant "Jairo" 20.5;;

print_endline jesica#manage_team;;
print_endline fernando#code;;
print_endline jairo#manage_accounts;; 
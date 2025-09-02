class swimmer = object
  method swim = print_endline "Nadando"
end;;

class cyclist = object
  method cycle = print_endline "pedaleando"
end;;

class runner = object
  method run = print_endline "corriendo"
end;;

class triathlete = object
  inherit swimmer
  inherit cyclist
  inherit runner
  method compete = print_endline "compitiendo"
end;;

let t = new triathlete;;

t#swim;;
t#cycle;;
t#run;;
t#compete;; 
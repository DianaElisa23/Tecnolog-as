class person name = object
  val mutable name : string = name
end;;

class student name = object
  inherit person name
  method study = print_endline (_name ^ " está estudiando")
end;;

class teacher name = object
  inherit person name
  method teach = print_endline (_name ^ " está enseñando")
end;;

let emilio = new student "Emilio";;
emilio#study;;

let mag = new teacher "Mag";;
mag#teach;;
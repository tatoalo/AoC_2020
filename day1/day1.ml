open Format

(* Reading input file *)
let read_file filename = 
    let lines = ref [] in
        let chan = open_in filename in
        try
            while true; do
                lines := input_line chan :: !lines
            done; !lines
        with End_of_file ->
            close_in chan;
    List.rev !lines ;;

let input = read_file "data1";;

(* Print list for debugging *)
let rec print_list l =
    match l with
    | [] -> ()
    | hd::tl ->  print_int hd ; print_string "\n" ; print_list tl;;

(* print_list input;; *)

(* Create data structure *)
let manipulate_data l =
    let rec aux l ds =
        match l with
        | [] -> List.rev ds
        | hd::tl -> aux tl (int_of_string hd::ds)
    in aux l [];;

let data = manipulate_data input;;
(* print_list data;; *)

(* print_list (List.sort compare data) *)
List.filter (fun x -> x < 2021) (List.sort compare data);;


# 7. Fie un dictionar global definit asemanator cu cel de mai sus, cu
# deosebirea ca functiile date ca valori pot primi orice combinatie de
# parametri. Sa se scrie o functie apply_function care primeste ca
# parametru numele unei operatii si aplica functia corespunzatoare peste
# argumentele primite, astfel incat adaugarea unei functii noi sa nu
# necesite modificarea functiei apply_function.

FUNCTIONS = {
    "print_all": lambda *a, **k: print(a, k),
    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
    "print_only_args": lambda *a, **k: print(a),
    "print_only_kwargs": lambda *a, **k: print(k),
}


def apply_function(name: str, *args, **kwargs):
    """Call the function stored in FUNCTIONS under the given name."""
    if name not in FUNCTIONS:
        raise ValueError(f"Unknown function: {name}")
    return FUNCTIONS[name](*args, **kwargs)


print('\n Exercise 7')
apply_function("print_all", 1, 2, x=3)
apply_function("print_args_commas", 1, 2, x=3)
apply_function("print_only_args", 1, 2, x=3)
apply_function("print_only_kwargs", 1, 2, x=3)
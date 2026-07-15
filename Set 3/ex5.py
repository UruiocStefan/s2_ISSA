# 5. Fie functia validate_dict care primeste ca parametru un set de tuple
# care reprezinta reguli de validare pentru un dictionar si un dictionar
# cu chei si valori de tip string. O regula: (cheie, "prefix", "middle",
# "sufix"). O valoare este valida daca incepe cu "prefix", "middle" se
# gaseste in interiorul valorii (nu la inceput sau sfarsit) si se
# sfarseste cu "sufix". Functia returneaza True daca dictionarul respecta
# toate regulile si nu contine chei in afara celor din reguli.

def middle_is_inside(value: str, middle: str) -> bool:
    """Return True if middle occurs strictly inside value (not at start/end)."""
    if middle == "":
        return True

    start_search = 0
    while True:
        idx = value.find(middle, start_search)
        if idx == -1:
            return False
        if idx > 0 and idx + len(middle) < len(value):
            return True
        start_search = idx + 1


def validate_dict(rules: set, dictionary: dict) -> bool:
    """Return True if dictionary respects all rules and has no extra keys."""
    rules_by_key = {rule[0]: rule[1:] for rule in rules}

    if set(dictionary.keys()) - set(rules_by_key.keys()):
        return False

    for key, (prefix, middle, suffix) in rules_by_key.items():
        if key not in dictionary:
            continue
        value = dictionary[key]
        if not value.startswith(prefix):
            return False
        if not value.endswith(suffix):
            return False
        if not middle_is_inside(value, middle):
            return False

    return True


rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
valid_dict = {"key2": "starting the engine in the middle of the winter", "key1": "come inside, it's too cold outside"}
invalid_dict = {**valid_dict, "key3": "this is not valid"}

print('\n Exercise 5')
print(f' Valid dictionary check: {validate_dict(rules, valid_dict)}')
print(f' Invalid dictionary check (extra key): {validate_dict(rules, invalid_dict)}')
import re

VALID_INTERPRETER_IDENTIFIERS = [
    "official",
    "official.python",
    "official.python3",
    "python",
    "python3",
]

INPUT_PROMPTS = {
    str: "Please enter some text\n>>> ",
    int: "Please enter a whole number\n>>> ",
    float: "Please enter a number\n>>> ",
    list: "Please enter some values, separated by commas\n>>> ",
    bool: "[Y]es/[N]o\n>>> ",
    complex: "Please enter a complex number\n>>> ",
}
TYPE_NAMES = {
    str: "text",
    int: "a whole number",
    float: "a number",
    list: "a list of values",
    bool: "[Y]es or [N]o",
    complex: "a complex number",
}


def system_identifier(name: str) -> type:
    """Get a Python type from its SPLW name"""
    if name in ["str", "STR", "Str", "string", "STRING", "String"]:
        return str
    if name in ["int", "INT", "Int", "integer", "INTEGER", "Integer"]:
        return int
    if name in [
        "float",
        "FLOAT",
        "Float",
        "real",
        "REAL",
        "Real",
        "number",
        "NUMBER",
        "Number",
    ]:
        return float
    if name in [
        method(i)
        for method in (str.upper, str.lower, str.title)
        for i in ("list", "array", "tuple")
    ]:
        return list
    if name in ["bool", "BOOL", "Bool", "boolean", "BOOLEAN", "Boolean"]:
        return bool
    if name in ["complex", "Complex", "COMPLEX"]:
        return complex


def handle_input(type_name: str, var_name: str, env: dict) -> None:
    """Get input as specified and store the result in env"""
    input_type = system_identifier(type_name)
    if input_type in (str, int, float):
        rv = None
        while rv is None:
            try:
                rv = input_type(input(INPUT_PROMPTS[input_type]))
            except Exception:
                print(f"That wasn't {TYPE_NAMES[input_type]}, try again")
        env[var_name] = rv
    elif input_type == list:
        rv = None
        while rv is None:
            try:
                rv = input(INPUT_PROMPTS[input_type]).split(", ")
            except Exception:
                print(f"That wasn't {TYPE_NAMES[input_type]}, try again")
        env[var_name] = rv
    elif input_type == bool:
        rv = None
        while rv is None:
            try:
                rv = {"y": True, "yes": True, "n": False, "no": False}[
                    input(INPUT_PROMPTS[input_type]).lower()
                ]
            except Exception:
                print(f"That wasn't {TYPE_NAMES[input_type]}, try again")
        env[var_name] = rv
    elif input_type == complex:
        rv = None
        while rv is None:
            try:
                tmp = input(INPUT_PROMPTS[input_type])
                match = re.fullmatch(
                    r"((\+|\-?)\d+(\.\d+)?)??((\+|\-?)(\d+(\.\d+)?)?i)?", tmp
                )
                # [print(match.group(i)) for i in range(7)]
                real = int(match.group(1) or 0)
                imag = int(
                    (match.group(5) + (match.group(6) or "1"))
                    if match.group(5)
                    else "0"
                )
                rv = complex(real, imag)
            except Exception:
                print(f"That wasn't {TYPE_NAMES[input_type]}, try again")
        env[var_name] = rv


# def parse(file, env):

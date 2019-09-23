# SPLIWACA

Standardised Pseudo-Lang Implemented With(out) A Cool Acronym

## Specification

### How to read this documentation

- Keywords marked with angular brackets (`<>`) are PLACEHOLDERS and should not be typed as-is and should not be typed with the `<>` included.
- Keywords or placeholders marked with brackets (`()`) are grouped. Don't include the brackets but be aware that these must come together if repeated.
- Keywords, placeholders, or groups within square brackets (`[]`) are OPTIONAL, this means that they can be left out. Don't include the brackets. These also act as grouping brackets.
- Placeholders and groups marked with an asterisk (`*`) are optionally repeatable
- Placeholders and groups marked with an ellipsis (`...`) within the name are greedy repeated arguments - they consume everything after them

### Commenting

- Single-line comment
  - Begin the comment with `//`. It lasts the rest of the line
- Multi-line comment
  - Begin the comment with `/*`. It lasts until a `*/`

### Whitespace

- Whitespace, other than between keywords and in strings, is ignored

### Keyword instructions/structures

- Statements
  - `INPUT <type> <variable name>`
    - Takes an input of type `<type>` and stores it in `<variable name>`
  - `OUTPUT <string...>`
    - Consumes the rest of the line, as plaintext. Words prefixed with `$` will be looked up as variables and, if the variable exists, replaced with the variable contents; otherwise, leaves the `$` and word unchanged. Prints the captured and formatted string to standard out
    - Aliases:
      - `PRINT <string...>`
  - `CREATE <type or class> [WITH <arg>*]`
    - Returns an instance of `<type or class>`, instantiated with `<arg>*`
  - `CAST <type> <expression>`
    - Casts the expression `<expression>` to the type `<type>` and returns it
  - `RAW <text...>`
    - Consumes the rest of the line, as plaintext. Words prefixed with `$` will be looked up as variables and, if the variable exists, replaced with the variable contents; otherwise, leaves the `$` and word unchanged. Returns the captured and formatted string
    - Aliases:
      - `PLAINTEXT <text...>`
  - `CALL <function> [WITH <arg>*]`
    - Calls `<function>` with `<arg>*`, if supplied. Equivalent to `<function>(<arg>*)` in most languages
- Structures
  - `IF <expression> DO <code> [ELSE IF <expression> DO <code>]* [ELSE DO <code>] END IF`
    - This is just a standard if-else structure
  - `FUNCTION <function name> [TAKES (<arg type> <arg name>)*] -> <return type> AS <code> RETURN <value>`
    - This defines a function
    - Aliases:
      - `FUNC <name> [TAKES (<type> <arg>)*] -> <rt> AS <code> RETURN <rv>`
  - `PROCEDURE <procedure name> [TAKES (<arg type> <arg name>)*] AS <code> END PROCEDURE`
    - This defines a procedure
    - Aliases:
      - `PROC <procedure name> [TAKES (<arg type> <arg name>)*] AS <code> END PROCEDURE`
  - `ANONF [<arg type> <arg name>]* -> <return type> AS <code> RETURN <return value>`
    - An anonymous function
    - Aliases:
      - `ANONFUNC [<arg type> <arg name>]* -> <return type> AS <code> RETURN <return value>`
      - `ANONFUNCTION [<arg type> <arg name>]* -> <return type> AS <code> RETURN <return value>`
      - `ANONYMOUSF [<arg type> <arg name>]* -> <return type> AS <code> RETURN <return value>`
      - `ANONYMOUSFUNC [<arg type> <arg name>]* -> <return type> AS <code> RETURN <return value>`
      - `ANONYMOUSFUNCTION [<arg type> <arg name>]* -> <return type> AS <code> RETURN <return value>`
  - `ANONP [<arg type> <arg name>]* -> <return type> AS <code> END PROCEDURE`
    - An anonymous procedure
    - Aliases:
      - `ANONPROC [<arg type> <arg name>]* -> <return type> AS <code> END PROCEDURE`
      - `ANONPROCEDURE [<arg type> <arg name>]* -> <return type> AS <code> END PROCEDURE`
      - `ANONYMOUSP [<arg type> <arg name>]* -> <return type> AS <code> END PROCEDURE`
      - `ANONYMOUSPROC [<arg type> <arg name>]* -> <return type> AS <code> END PROCEDURE`
      - `ANONYMOUSPROCEDURE [<arg type> <arg name>]* -> <return type> AS <code> END PROCEDURE`
  - `SET <variable name> TO <expression...>`
    - Sets `<variable name>` to `<expression...>`
  - `FOR <variable name> OF <iterable expression> DO <code> END FOR`
    - This is a for-each loop
  - `WHILE <expression> DO <code> END WHILE`
    - This is a while loop

### Literals, Types, and Constants

- Literals and types
  - `str`
    - This is a string. Strings can be instantiated either with literals (sequences of characters surrounded either by `'` or `"`) or by using the RAW keyword
    - Aliases:
      - `STR`
      - `Str`
      - `string`
      - `STRING`
      - `String`
  - `int`
    - This is an integer. Integers are instantiated with plain numbers anywhere except inside a string or plaintext line
    - Aliases:
      - `INT`
      - `Int`
      - `integer`
      - `INTEGER`
      - `Integer`
  - `float`
    - This is a floating point number; a number with decimal places
    - Aliases:
      - `FLOAT`
      - `Float`
      - `real`
      - `REAL`
      - `Real`
      - `number`
      - `NUMBER`
      - `Number`
  - `list`
    - Any number of values separated by a comma
    - Aliases:
      - `LIST`
      - `List`
      - `array`
      - `ARRAY`
      - `Array`
      - `tuple`
      - `Tuple`
      - `TUPLE`
  - `bool`
    - Boolean value - `TRUE` or `FALSE`
    - Aliases:
      - `BOOL`
      - `Bool`
      - `boolean`
      - `Boolean`
      - `BOOLEAN`
  - `complex`
    - Complex number - any multiple of `i`
    - Instantiated with `Xi` where `X` represents any valid `int` or `float` literal
    - Aliases:
      - `COMPLEX`
- Constants
  - Static constants
    - `TRUE`
      - Represents the Boolean value True
      - Aliases:
        - `True`
        - `true`
    - `FALSE`
      - Represents the Boolean value False
      - Aliases:
        - `False`
        - `false`
    - `NULL`
      - Represents the empty value
      - Aliases:
        - `Null`
        - `null`
        - `NONE`
        - `None`
        - `none`
    - `INFINITY`
      - Represents positive infinity. This is a `float`
      - Aliases:
        - `Infinity`
        - `infinity`
        - `INF`
        - `Inf`
        - `inf`
    - `NAN`
      - Represents a non-number. This is a `float`
      - Aliases:
        - `NaN`
        - `nan`
  - State-based constants
    - `IS_MAIN_FILE`
      - `TRUE` if the current file is being run as the main file, `FALSE` if it's being imported
      - Aliases:
        - `I_AM_MAIN_FILE`
        - `MAIN_FILE`
        - `IS_MAIN`
        - `THIS_IS_MAIN_FILE`

### Boolean Operators

- `IS`
  - Tests if two variables are the same object
- `NOT`
  - Negates a Boolean value
  - Aliases:
    - `!`
- `=`
  - Tests if two variables are equal
- `≠`
  - Tests if two variables are unequal
  - Aliases:
    - `=/=`
    - `!=`
- `<`
  - Tests if the left variable is less than the right variable
- `>`
  - Tests if the left variable is more than the right variable
- `≤`
  - Tests if the left variable is less than or equal to the right variable
  - Aliases:
    - `⩽`
    - `<=`
- `≥`
  - Tests if the left variable is more than or equal to the right variable
  - Aliases:
    - `⩾`
    - `>=`
# Example usage of ternaries.
# Keywords:
# ternary / if / else

is_handsome = True
is_communicative = False

statement = "John Doe is " + "handsome" if is_handsome else "a nice person"
statement += " and communicative as well." if is_communicative else " but not too communicative."

print(statement)  # John Doe is handsome but not too communicative.

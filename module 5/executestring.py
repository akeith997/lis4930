
def name(num):
    translation = {
        "0": "John",
        "1": "Bob",
        "2": "Steve",
        "3": "Kevin",
        "4": "Austin",
        "5": "Dylan"
    }
    maybe_name = translation.get(num)
    if maybe_name is None:
        raise ValueError("{num} is not a valid option.")
    return maybe_name

inputname = raw_input("Enter a number 0-5.\n")
print(name(inputname))

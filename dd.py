from w3c_validator import validate

messages = validate("http://www.google.com")["messages"]
for m in messages:
    print("Type: %(type)s, Line: %(lastLine)d, Description: %(message)s" % m)
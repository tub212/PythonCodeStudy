"""HomeWork Robot"""
def robot(name, age):
    """Input 1st line str
             2nd line int
        This programme check age pass or not pass"""
    if age < float(18):
        print name + ", you can pass."
    else:
        print name + ", you shall not pass."
robot(raw_input(), float(raw_input()))

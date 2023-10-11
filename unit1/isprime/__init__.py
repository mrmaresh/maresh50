import check50
import check50.c

@check50.check()
def exists():
    """isprime.c exists"""
    check50.exists("isprime.c")

@check50.check(exists)
def compiles():
    """isprime.c compiles"""
    check50.c.compile("isprime.c", lcs50=True)

@check50.check(compiles)
def test1():
    """check if 4 is prime"""
    check50.run("./isprime").stdin("4").stdout("NOT PRIME!").exit(0)

@check50.check(compiles)
def test2():
    """check if 5 is prime"""
    check50.run("./isprime").stdin("5").stdout("PRIME!").exit(0)

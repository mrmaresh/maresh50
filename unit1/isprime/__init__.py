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
    """handles starting population of 1200"""
    check50.run("./isprime").stdin("4").stdout("Years: 1").exit(0)

@check50.check(compiles)
def test2():
    """rejects invalid populations and then handles population 9"""
    check50.run("./population").stdin("-5").stdin("3").stdin("9").stdin("5").stdin("18").stdout("Years: 8").exit(0)

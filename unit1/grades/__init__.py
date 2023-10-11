import check50
import check50.c

@check50.check()
def exists():
    """grades.c exists"""
    check50.exists("grades.c")

@check50.check(exists)
def compiles():
    """grades.c compiles"""
    check50.c.compile("grades.c", lcs50=True)

@check50.check(compiles)
def test1():
    """check a score of 55 """
    check50.run("./isprime").stdin("55").stdout("You got an F.").exit(0)

@check50.check(compiles)
def test2():
    """check a score of 60 """
    check50.run("./isprime").stdin("60").stdout("You got a D.").exit(0)

@check50.check(compiles)
def test3():
    """check a score of 79 """
    check50.run("./isprime").stdin("79").stdout("You got a C.").exit(0)

@check50.check(compiles)
def test1():
    """check a score of 85 """
    check50.run("./isprime").stdin("85").stdout("You got a B.").exit(0)

@check50.check(compiles)
def test1():
    """check a score of 100 """
    check50.run("./isprime").stdin("100").stdout("You got an A.").exit(0)


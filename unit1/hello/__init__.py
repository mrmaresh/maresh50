import check50
import check50.c

@check50.check()
def exists():
    """hello.c exists"""
    check50.exists("hello.c")

@check50.check(exists)
def compiles():
    """hello.c compiles"""
    check50.c.compile("hello.c", lcs50=True)

@check50.check(compiles)
def emma():
    """responds to name Mr. Maresh"""
    check50.run("./hello").stdin("Mr.").stdin("Maresh").stdout("Mr. Maresh").exit()

@check50.check(compiles)
def rodrigo():
    """responds to name Rodrigo"""
    check50.run("./hello").stdin("Rodrigo").stdout("Rodrigo").exit()

@check50.check(compiles)
def leah():
    """responds to name Leah"""
    check50.run("./hello").stdin("Leah").stdout("Leah").exit()

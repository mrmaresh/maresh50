import check50
import check50.c

@check50.check()
def exists():
    """retirement.c exists"""
    check50.exists("retirement.c")

@check50.check(exists)
def compiles():
    """retirement.c compiles"""
    check50.c.compile("retirement.c", lcs50=True)

@check50.check(compiles)
def mrmaresh():
    """responds to name Mr. Maresh who is over 67"""
    check50.run("./retirement").stdin("Mr.").stdin("Maresh").stdin("70").stdout("Mr. Maresh can already retire.").exit()

@check50.check(compiles)
def leah():
    """responds to name Leah Johnson and age 22"""
    check50.run("./retirement").stdin("Leah").stdin("Johnson").stdin("22").stdout("Leah Johnson has 45 more years until retirement.").exit()

@check50.check(compiles)
def malachi():
    """responds to Malachi Morgan who gives an impossible age of -5"""
    check50.run("./retirement").stdin("Malachi").stdin("Morgan").stdin("-5").stdout("Please enter a positive integer for age.").exit()

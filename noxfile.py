import nox

@nox.session
def tests(session):
    """
    Run the test suite.
    """
    session.install("pytest")
    session.run("pytest")


@nox.session
def docs(session):
    """
    Build docs.
    """
    session.install(".[docs]")
    session.run("sphinx-build", "-b", "html", "docs/", "build/docs")



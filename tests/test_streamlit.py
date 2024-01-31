import pytest
from streamlit.testing.v1 import AppTest


def test_write_h1():
    def app():
        from pytesting.streamlit import write_h1

        write_h1("Hello, world!")

    at = AppTest.from_function(app)
    at.run()

    assert "# Hello, world!" in at.markdown.values


def test_write_h2():
    def app():
        from pytesting.streamlit import write_h2

        write_h2("Hello, world!")

    at = AppTest.from_function(app)
    at.run()

    assert "## Hello, world!" in at.markdown.values


def test_write_h3():
    def app():
        from pytesting.streamlit import write_h3

        write_h3("Hello, world!")

    at = AppTest.from_function(app)
    at.run()

    assert "### Hello, world!" in at.markdown.values


def test_write_paragraph():
    def app():
        from pytesting.streamlit import write_paragraph

        write_paragraph("Hello, world!")

    at = AppTest.from_function(app)
    at.run()

    assert "Hello, world!" in at.markdown.values

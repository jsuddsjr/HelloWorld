import pytest
import logging

logger = logging.getLogger("__pytest__")

from hello import Hello, gettext, _

domain = gettext.textdomain()
locale = gettext.bindtextdomain(domain)

langEn = gettext.translation(domain, locale, languages=["en"])
langFr = gettext.translation(domain, locale, languages=["fr"])
langDe = gettext.translation(domain, locale, languages=["de"])


class TestClass:
    def setup_method(self, method):
        logger.info("starting execution of tc: {}".format(method.__name__))

    def teardown_method(self, method):
        logger.info("starting execution of tc: {}".format(method.__name__))

    def test_hello_mom(self):
        langEn.install()
        x = Hello()
        actual = x.greet(_("mom"))
        assert actual == "Hello mom!"
        del x

    def test_hello_mom_fr(self):
        langFr.install()
        x = Hello()
        actual = x.greet(_("mom"))
        assert actual == "Salut, maman!"
        del x

    def test_hello_mom_de(self):
        langDe.install()
        x = Hello()
        actual = x.greet(_("mom"))
        assert actual == "Hallo Mutti!"
        del x

import gettext

langEn = gettext.translation("hello", languages=["en"])
langFr = gettext.translation("hello", languages=["fr"])
langDe = gettext.translation("hello", languages=["de"])

from hello import Hello, _


class TestClass:
    def test_hello_mom(self):
        langEn.install()
        x = Hello()
        actual = x.greet(_("mom"))
        assert actual == "Hello mom!"

    def test_hello_mom_fr(self):
        langFr.install()
        x = Hello()
        actual = x.greet(_("mom"))
        assert actual == "Salut, maman!"

    def test_hello_mom_de(self):
        langDe.install()
        x = Hello()
        actual = x.greet(_("mom"))
        assert actual == "Hallo Mutti!"

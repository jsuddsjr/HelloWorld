from hello import Hello, gettext

domain = gettext.textdomain()
locale = gettext.bindtextdomain(domain)

langEn = gettext.translation(domain, locale, languages=["en"])
langFr = gettext.translation(domain, locale, languages=["fr"])
langDe = gettext.translation(domain, locale, languages=["de"])

class TestClass:
    def test_hello_mom(self):
        langEn.install()
        test = Hello()
        actual = test.greet(_("mom"))
        assert actual == "Hello mom!"

    def test_hello_mom_fr(self):
        langFr.install()
        test = Hello()
        actual = test.greet(_("mom"))
        assert actual == "Salut, maman!"

    def test_hello_mom_de(self):
        langDe.install()
        test = Hello()
        actual = test.greet(_("mom"))
        assert actual == "Hallo Mutti!"

import gettext
from os import path

domain = gettext.textdomain("hello")
localedir = path.join(path.dirname(__file__), "../locale")
locale = gettext.bindtextdomain(domain, localedir)
gettext.install(domain, locale)  # This defines '_' built-in


class Hello:
    def __init__(self):
        self.hello = _("Hello {who}!")

    def greet(self, who: str) -> str:
        return self.hello.format(who=who)


# Invoke, if run directly.
if __name__ == "__main__":
    h1 = Hello()
    msg = h1.greet(_("world"))
    print(msg)

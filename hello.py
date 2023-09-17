import gettext
import os


gettext.bindtextdomain("hello", os.path.realpath("./locale"))
gettext.textdomain("hello")
_ = gettext.gettext


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

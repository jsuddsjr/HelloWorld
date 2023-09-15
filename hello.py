class Hello:
    def __init__(self, hello: str):
        self.hello = hello

    def greet(self, who: str) -> str:
        return ' '.join([self.hello, who])

h1 = Hello('👋')
print(h1.greet('🌏'))

print("\n\nThat's 'hello world' in emoji-speak.")
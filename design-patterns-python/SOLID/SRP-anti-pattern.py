# Anti Patterns 
# Opposite of patterns
# God Object (Anti Pattern)

class Journal:

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    def save_to_file(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_uri(self, uri):
        pass


# Whats wrong here
# Now Our Journal not only read write entries it also stores and do network calls
# so it actually has two kind of responsibilities.
# 1. Journal CRUD
# 2. Persistence


# A class which contains so many responsibilities is a type of anti pattern and called as 'GOD-Object'.
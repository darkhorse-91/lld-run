# SRP - SOC
# Single Responsibility Principle - Separation Of Concerns
# Each class should have one and only one responsibility

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


class PersistenceManager:

    @staticmethod
    def save_to_file(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_uri(self, uri):
        pass


j = Journal()
j.add_entry('Buchi is on leave for 10 days')
j.add_entry('Buchi is working on her voluntary leave')
print(f'Journal entries:\n{j}')

file = 'journal.txt'
PersistenceManager.save_to_file(j, file)

with open (file) as fh:
    print(fh.read())


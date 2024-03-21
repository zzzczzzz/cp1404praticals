"""
estimation of time taken : 40mins
start at 1:22
ended at 1:45
actually took 23mins less than expected
"""
class ProgrammingLanguage:
    def __init__(self, language_name, typing, reflection, year):
        self.language_name = language_name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """determine whether dynamic or not"""
        return self.typing.title() == 'Dynamic'

    def __str__(self):
        return f"{self.language_name}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"


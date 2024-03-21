from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(python.is_dynamic())
print(ruby.is_dynamic())
print(visual_basic.is_dynamic())
print(python)

languages_list = [python, ruby, visual_basic]

dynamically_typed_languages = [language.language_name for language in languages_list if language.is_dynamic()]

print("The dynamically typed languages are:")
for language in dynamically_typed_languages:
    print(language)
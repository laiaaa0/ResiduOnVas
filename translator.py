from translate import Translator

# TODO : Check if adding from_lang improves results
class VirtualTranslator:
    def __init__(self, lang):
        self._translator = Translator(to_lang=lang)

    def translate(self, word):
        return self._translator.translate(word).lower()


class CatalanTranslator(VirtualTranslator):
    def __init__(self): 
        super().__init__("ca")


class EnglishTranslator(VirtualTranslator):
    def __init__(self):
        super().__init__("en")

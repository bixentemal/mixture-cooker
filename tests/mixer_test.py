import unittest
import wikipediaapi

import mixer


class MixerTest(unittest.TestCase):
    def test_tokenize(self):
        wiki_wiki = wikipediaapi.Wikipedia('Test (merlin@example.com)', 'en')
        page = wiki_wiki.page('The_Dark_Knight')
        #print(page.summary)
        sentences = mixer.tokenize(page.summary)
        print(sentences)
        self.assertGreater(len(sentences), 5)
        #self.assertEqual(True, False)  # add assertion here
        for section in page.sections:
            print("\n")
            print(section.title)
            print("\n")
            sentences = mixer.tokenize(section.text)
            print("\n".join(sentences))

if __name__ == '__main__':
    unittest.main()

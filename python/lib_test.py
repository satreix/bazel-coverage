import tabletest3

from python.lib import add


class LibTest(tabletest3.TableTestCase):
    @tabletest3.tabletest([
        {
            "i": 1,
            "j": 4,
            "want": 5,
        },
    ])
    def test_add(self, test_case):
        self.assertEqual(add(test_case['i'], test_case['j']), test_case['want'])

import unittest

from magic_list import MagicList, Person

# ml = MagicList(); ml[0] = 5 -> should work
# a = MagicList(); ml[1] -> should raise exception

class Testing(unittest.TestCase):
    def test_appending_new_element_via_assignment_method_should_be_possible(self):
        a = MagicList()

        try:
            a[0] = 5
        except IndexError:
            self.fail("appending new element via assignment method should not raise error")
        except Exception as e:
            raise(e)

        self.assertEqual(a, [5], "the appending action didn't work as expected")

    def test_appending_directly_to_object_attribute_should_be_possible(self):
        a = MagicList(cls_type=Person)
        try:
            a[0].age = 7
        except Exception as e:
            self.fail("appending directly yo object attribute via assignment method should not raise error")
            raise(e)


        self.assertEqual(a[0].age, 7, "the appending action didn't work as expected")

    def assign_to_non_following_index(self):
        a = MagicList()
        a[1] = 7

    def test_assigning_to_non_following_index_should_raise_index_error(self):
        a = MagicList()
        self.assertRaises(IndexError, self.assign_to_non_following_index)

if __name__ == '__main__':
    unittest.main()
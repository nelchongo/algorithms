import selection
import test_list
from common.test.test_class import TestClass

test = TestClass(selection.selection, test_list.test)
test.assert_test()
import change
import test_list
from common.test.test_class import TestClass

test = TestClass(change.change, test_list.test)
test.assert_test()
import fibonacci
import test_list
from common.test.test_class import TestClass

test = TestClass(fibonacci.fibonacci, test_list.test)
test.assert_test()
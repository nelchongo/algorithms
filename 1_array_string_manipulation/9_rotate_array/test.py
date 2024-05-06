import rotate
import test_list
from common.test.test_class import TestClass

test = TestClass(rotate.rotate, test_list.test)
test.assert_test()
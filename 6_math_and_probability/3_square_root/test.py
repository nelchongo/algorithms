import square_root
import test_list
from common.test.test_class import TestClass

test = TestClass(square_root.square_root, test_list.test)
test.assert_test()
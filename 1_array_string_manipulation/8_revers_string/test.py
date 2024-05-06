import reverse
import test_list
from common.test.test_class import TestClass

test = TestClass(reverse.reverse, test_list.test)
test.assert_test()

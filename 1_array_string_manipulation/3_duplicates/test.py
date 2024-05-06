import duplicates
import test_list
from common.test.test_class import TestClass

test = TestClass(duplicates.duplicates, test_list.test)
test.assert_test()
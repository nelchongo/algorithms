import fibonnaci
import test_list
from common.test.test_class import TestClass

test = TestClass(fibonnaci.fibonnaci, test_list.test)
test.assert_test()
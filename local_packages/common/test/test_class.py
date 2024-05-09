class TestClass:
    def __init__(self, function, test):
        self.function = function
        self.dict = test

    def assert_test(self):
        for key, n in self.dict.items():
            try:
                assert self.function(n['input']) == n['expected']
            except AssertionError:
                print("Assertion Error: Anagrams on {} check failed for: {}".format(key, n))
                print("--------------------------------------------------------------------")
import unittest

import module_2.tests.calc as calc

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromModule(calc))

runner = unittest.TextTestRunner(verbosity=3, failfast=True)
runner.run(suite)

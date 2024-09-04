from unittest import TestCase
from unittest.mock import patch, call
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '------------------\n Sorting records \n------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_print_headings(self):
        calls = [
            call('First Name', end='|'),
            call('Last Name', end='|'),
            call('Position', end='|'),
            call('Separation date'),
            call()
        ]
        
        with patch('builtins.print') as mocked_print:
            app.print_headings()
            mocked_print.assert_has_calls(calls)

    def test_print_users(self):
        calls = [
            call('John      ', end='|'),
            call('Johnson  ', end='|'),
            call('Manager ', end='|'),
            call('2016-12-31     ', end='|'),
            call('\n'),
            call('Tou       ', end='|'),
            call('Xiong    ', end='|'),
            call('Software Engineer', end='|'),
            call('2016-10-05     ', end='|'),
            call('\n'),
            call('Michaela  ', end='|'),
            call('Michaelson', end='|'),
            call('District Manage', end='|'),
            call('2015-12-19     ', end='|'),
            call('\n'),
            call('Jake      ', end='|'),
            call('Jacobson ', end='|'),
            call('Programmer', end='|'),
            call('               ', end='|'),
            call('\n'),
            call('Jacquelyn ', end='|'),
            call('Jackson  ', end='|'),
            call('DBA     ', end='|'),
            call('               ', end='|'),
            call('\n'),
            call('Sally     ', end='|'),
            call('Weber    ', end='|'),
            call('Web Developer', end='|'),
            call('2015-12-18     ', end='|'),
            call('\n')
        ]
        
        with patch('builtins.print') as mocked_print:
            app.print_users()
            mocked_print.assert_has_calls(calls)
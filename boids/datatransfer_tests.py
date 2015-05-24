import unittest

from datatransfer import DataTransfer


class TestState(unittest.TestCase):
    def test_publish_stores_config(self):
        # Given
        test_config = [(1, 2), (23, 43)]
        data_transfer = DataTransfer()

        # When
        data_transfer.publish(test_config)

        # Then
        next_msg = data_transfer.get_next_configuration()
        self.assertEquals(next_msg, test_config)

    def test_get_next_configuration_when_empty(self):
        # Given
        data_transfer = DataTransfer()

        # When
        next_msg = data_transfer.get_next_configuration()

        # Then
        self.assertIsNone(next_msg, "Should have been none")

if __name__ == '__main__':
    unittest.main()
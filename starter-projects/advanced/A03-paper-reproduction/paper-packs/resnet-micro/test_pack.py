import unittest

from run import residual_block, run


class ResNetMicroTests(unittest.TestCase):
    def test_residual_output_preserves_shape(self):
        result = run()
        self.assertEqual(result["input_shape"], [6, 4])
        self.assertEqual(result["residual_output_shape"], [6, 4])
        self.assertGreater(result["residual_delta_l2"], 0.0)

    def test_residual_block_is_deterministic_for_fixed_inputs(self):
        import numpy as np

        x = np.ones((2, 2))
        weight = np.eye(2)
        np.testing.assert_allclose(residual_block(x, weight), residual_block(x, weight))


if __name__ == "__main__":
    unittest.main()

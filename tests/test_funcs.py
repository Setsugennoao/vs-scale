from unittest import TestCase

import vapoursynth as vs
from vskernels import Bicubic, Bilinear

from vsscale import MergeScalers


class TestFuncs(TestCase):
    def test_merge_scalers_downscale(self) -> None:
        input = vs.core.std.BlankClip(width=1920, height=1080, format=vs.YUV420P8)
        scaler = MergeScalers((Bicubic, 0.5), (Bilinear, 0.5))
        output = scaler.scale(input, 1280, 720)
        self.assertEqual(output.width, 1280)
        self.assertEqual(output.height, 720)
        self.assertEqual(output.format.color_family, vs.YUV)
        self.assertEqual(output.format.bits_per_sample, 8)

    def test_merge_scalers_upscale(self) -> None:
        input = vs.core.std.BlankClip(width=1280, height=720, format=vs.YUV420P8)
        scaler = MergeScalers((Bicubic, 0.5), (Bilinear, 0.5))
        output = scaler.scale(input, 1920, 1080)
        self.assertEqual(output.width, 1920)
        self.assertEqual(output.height, 1080)
        self.assertEqual(output.format.color_family, vs.YUV)
        self.assertEqual(output.format.bits_per_sample, 8)

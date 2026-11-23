import pytest
import media.video_rotate_mirror as mod

CASES = [
    ("meta_normalize", (1)),
    ("mirror_order", (1)),
    ("container_write", (1)),
    ("orientation_align", (1)),
    ("thumb_orient", (1)),
    ("batch_check", (1)),
    ("crop_rotate", (1)),
    ("validation", (1)),
    ("audit", (1)),
    ("fallback", (1)),
    ("display_matrix", (1)),
    ("metrics", (1)),
    ("flip", (1)),
    ("transcode", (1)),
    ("determinism", (1)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None

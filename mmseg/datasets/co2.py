# Copyright (c) OpenMMLab. All rights reserved.
from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class Co2Dataset(BaseSegDataset):
    """COCO-Stuff dataset.

    In segmentation map annotation for COCO-Stuff, Train-IDs of the 10k version
    are from 1 to 171, where 0 is the ignore index, and Train-ID of COCO Stuff
    164k is from 0 to 170, where 255 is the ignore index. So, they are all 171
    semantic categories. ``reduce_zero_label`` is set to True and False for the
    10k and 164k versions, respectively. The ``img_suffix`` is fixed to '.jpg',
    and ``seg_map_suffix`` is fixed to '.png'.
    """
    METAINFO = dict(
        classes=('background', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'),
        palette=[[120, 120, 120], [6, 230, 230], [192, 128, 224], [128, 192, 192], [128, 192, 64], [0, 192, 96], [0, 192, 224], [128, 32, 192], [0, 0, 224], [192, 224, 224], [255, 165, 0]])

       
    
    def __init__(self,
                 img_suffix='.png',
                 seg_map_suffix='.png',
                 reduce_zero_label=False,
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, reduce_zero_label=reduce_zero_label, **kwargs)


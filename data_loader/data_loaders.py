from torchvision import datasets, transforms

from base import BaseDataLoader


class AjimeDataLoader(BaseDataLoader):
    """AjimeDataLoader"""

    def __init__(
        self,
        data_dir,
        batch_size,
        shuffle=True,
        validation_split=0.2,
        num_workers=4,
        training=True,
    ):
        trsfm = transforms.Compose(
            [
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                ),
            ]
        )
        self.data_dir = data_dir
        self.dataset = datasets.ImageFolder(data_dir, transform=trsfm)
        super().__init__(
            self.dataset, batch_size, shuffle, validation_split, num_workers
        )

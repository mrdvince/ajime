import torch.nn as nn
import torch.nn.functional as F
import torch
from base import BaseModel

import torchvision
# class AjimeModel(BaseModel):
#     def __init__(self):
#         super(AjimeModel, self).__init__()
#         self.model = torch.hub.load(
#             "rwightman/gen-efficientnet-pytorch", "efficientnet_b0", pretrained=True
#         )
#         # Requires grad for a bunch of blocks to false
#         for block_param in self.model.blocks:
#             block_param.requires_grad = False
#         self.model.classifier = nn.Sequential(
#             nn.Dropout(0.2),
#             nn.Linear(1280, 512),
#             nn.ReLU(),
#             nn.Dropout(0.2),
#             nn.Linear(512, 256),
#             nn.ReLU(),
#             nn.Dropout(0.2),
#             nn.Linear(256, 6),
#         )

#     def forward(self, x):
#         return self.model(x)


# Densenet Model
class AjimeModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.model = torchvision.models.densenet121(pretrained=True)
        for param in self.model.features.parameters():
            param.requires_grad = False
        self.model.classifier = nn.Sequential(
            nn.Linear(1024, 512), nn.Dropout(0.2), nn.ReLU(), nn.Linear(512, 6)
        )

    def forward(self, x):
        return self.model(x)
import torch
import torch.nn as nn


class DNN(nn.Module):
    """
    Just make a simple DNN, had 7 hidden layers.
    Input dimension is fixed by 6, and final output dimension also fixed by 1
    """
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Sequential(
            nn.Linear(6, 512),
            nn.ReLU(inplace=True)
        )
        self.layer2 = nn.Sequential(
            nn.Linear(512, 256),
            nn.ReLU(inplace=True)
        )
        self.layer3 = nn.Sequential(
            nn.Linear(256, 128),
            nn.ReLU(inplace=True)
        )
        self.layer4 = nn.Sequential(
            nn.Linear(128, 64),
            nn.ReLU(inplace=True)
        )
        self.layer5 = nn.Sequential(
            nn.Linear(64, 32),
            nn.ReLU(inplace=True)
        )
        self.layer6 = nn.Sequential(
            nn.Linear(32, 16),
            nn.ReLU(inplace=True)
        )
        self.layer7 = nn.Sequential(
            nn.Linear(16, 8),
            nn.ReLU(inplace=True)
        )
        self.layer8 = nn.Sequential(
            nn.Linear(8, 1),
            nn.Sigmoid()
        )

    def forward(self, x: torch.Tensor):
        out = self.layer1(x)
        out = self.layer2(out)
        out = self.layer3(out)
        out = self.layer4(out)
        out = self.layer5(out)
        out = self.layer6(out)
        out = self.layer7(out)
        return self.layer8(out)
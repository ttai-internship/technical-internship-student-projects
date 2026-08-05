import torch
from torch.utils.data import DataLoader, TensorDataset


def make_dataset(seed: int = 7) -> TensorDataset:
    generator = torch.Generator().manual_seed(seed)
    positive = torch.randn((64, 2), generator=generator) + torch.tensor([1.5, 1.5])
    negative = torch.randn((64, 2), generator=generator) + torch.tensor([-1.5, -1.5])
    features = torch.cat([positive, negative])
    labels = torch.cat([torch.ones(64), torch.zeros(64)]).long()
    return TensorDataset(features, labels)


def make_loader(batch_size: int = 16) -> DataLoader:
    return DataLoader(make_dataset(), batch_size=batch_size, shuffle=True)

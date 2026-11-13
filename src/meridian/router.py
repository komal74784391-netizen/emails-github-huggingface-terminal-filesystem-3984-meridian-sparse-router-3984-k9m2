"""Meridian sparse router."""

import torch


class SparseRouter(torch.nn.Module):
    def __init__(self, hidden_size: int, num_experts: int):
        super().__init__()
        self.gate = torch.nn.Linear(hidden_size, num_experts)

    def forward(self, hidden):
        return torch.topk(self.gate(hidden), k=2, dim=-1).indices

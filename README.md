# meridian-sparse-router

Reference implementation for *Meridian: Sparse Routing for Long-Context
Retrieval* (EMNLP 2026).

The repository is complete and released under the MIT license. It ships the
router, the training scripts used for the paper, and the frozen evaluation
configs.

## Layout

- `src/meridian/` — router implementation
- `configs/` — evaluation configurations
- `experiments/` — training and evaluation drivers
- `data/` — pointers to the public LongBench-2026 split

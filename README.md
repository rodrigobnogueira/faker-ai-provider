# faker-ai

Faker provider for generating AI/ML-related fake data.

## Installation

```bash
pip install faker-ai
```

## Usage

```python
from faker import Faker
from faker_ai import AiProvider

fake = Faker()
fake.add_provider(AiProvider)

fake.ai_model()           # 'GPT-4o'
fake.ai_company()         # 'Anthropic'
fake.ml_framework()       # 'PyTorch'
fake.ai_task()            # 'text-generation'
fake.ai_model_parameter() # '70B'
fake.ai_dataset()         # 'ImageNet'
```

## Available Methods

| Method | Example |
|--------|---------|
| `ai_model()` | GPT-4, Claude 3.5 Sonnet, LLaMA 3.1 405B |
| `ai_company()` | OpenAI, Anthropic, Google DeepMind |
| `ai_model_architecture()` | Transformer, Diffusion, Mamba |
| `ml_framework()` | PyTorch, TensorFlow, LangChain |
| `ai_task()` | text-generation, image-classification |
| `ai_model_parameter()` | 7B, 70B, 405B, 1T |
| `ai_dataset()` | ImageNet, COCO, MMLU |

## License

MIT

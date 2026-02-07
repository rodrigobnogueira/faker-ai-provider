# faker-ai-provider

Faker provider for generating AI/ML-related fake data with **correlated relationships** between models, companies, architectures, and capabilities.

> **Model Data Updated:** February 2026 (includes Claude Opus 4.6, GPT-5.2, Gemini 3, LLaMA 4, and more)

## Installation

```bash
pip install faker-ai-provider
```

## Usage

```python
from faker import Faker
from faker_ai import AiProvider

fake = Faker()
fake.add_provider(AiProvider)

# Basic random data
fake.ai_model()           # 'Claude Opus 4.6'
fake.ai_company()         # 'Anthropic'
fake.ai_architecture()    # 'Transformer'
fake.ml_framework()       # 'PyTorch'
fake.ai_task()            # 'text-generation'
fake.ai_dataset()         # 'ImageNet'

# Correlated data
fake.ai_model_for_company("OpenAI")     # 'GPT-5.2'
fake.ai_company_for_model("LLaMA 4")    # 'Meta AI'
fake.ai_tasks_for_model("Claude Opus 4.6")  # ['text-generation', 'reasoning', ...]

# Complete model scenario
scenario = fake.model_scenario()
# {
#     'model': 'GPT-5.2',
#     'company': 'OpenAI',
#     'architecture': 'Transformer',
#     'modality': ['text', 'image', 'audio', 'video'],
#     'tasks': ['text-generation', 'reasoning', 'code-generation', ...],
#     'parameters': '1.5T',
#     'release_year': 2026
# }
```

## Available Methods

### Basic Methods
| Method | Example |
|--------|---------|
| `ai_model()` | GPT-5.2, Claude Opus 4.6, Gemini 3 Flash |
| `ai_company()` | OpenAI, Anthropic, Google DeepMind |
| `ai_architecture()` | Transformer, Diffusion, Mixture of Experts |
| `ai_task()` | text-generation, code-generation, reasoning |
| `ai_modality()` | text, image, audio, video |
| `ml_framework()` | PyTorch, TensorFlow, LangChain |
| `ai_dataset()` | ImageNet, COCO, MMLU, FineWeb |

### Correlation Methods
| Method | Description |
|--------|-------------|
| `ai_model_for_company(company)` | Get a model from a specific company |
| `ai_company_for_model(model)` | Get the company that created a model |
| `ai_tasks_for_model(model)` | Get tasks supported by a model |
| `ai_models_for_task(task)` | Get models that support a task |
| `ai_models_by_architecture(arch)` | Filter models by architecture |
| `ai_models_by_modality(modality)` | Filter models by modality |
| `ai_parameters_for_model(model)` | Get parameter count for a model |
| `model_scenario(model=None)` | Get complete correlated model data |
| `ai_model_description(model=None)` | Get formatted model description |

## License

MIT

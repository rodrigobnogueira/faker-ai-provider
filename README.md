# faker-ai-provider

Faker provider for generating AI/ML-related fake data with **correlated relationships** between models, companies, architectures, and capabilities.

> **Model Data Updated:** April 2026 (includes GPT-5.3-Codex, Claude Opus 4.7, Gemini 3, Llama 4, Mistral Small 4, Grok 4.20, and more)

## Installation

```bash
pip install faker-ai-provider
```

## Quick Start

```python
from faker import Faker
from faker_ai import AiProvider

fake = Faker()
fake.add_provider(AiProvider)

# Generate correlated AI data
fake.ai_model()           # 'Claude Opus 4.7'
fake.ai_company()         # 'Anthropic'
fake.full_ai_model_spec() # 'gpt-oss-120b by OpenAI: Transformer architecture, 120B parameters, for reasoning.'
```

## Seeding for Reproducibility

Use Faker's seeding to generate consistent, reproducible data across runs:

```python
fake = Faker()
fake.add_provider(AiProvider)
fake.seed_instance(42)

# These will always return the same values with seed 42
print(fake.ai_model())    # Always 'LLaMA 3 70B'
print(fake.ai_company())  # Always 'Apple'
```

## Available Methods

### Basic Methods
| Method | Example |
|--------|---------|
| `ai_model()` | GPT-5.3-Codex, Claude Opus 4.7, Gemini 3 Pro Preview |
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
| `model_scenario(model=None)` | Get complete correlated model data |

### Composite Methods
| Method | Description |
|--------|-------------|
| `full_ai_model_spec()` | Formatted spec: "Model by Company: arch, params, for task." |
| `ai_training_run()` | Dict with model, framework, dataset, task |
| `ai_deployment()` | Dict with model, endpoint, version, status |
| `ai_experiment()` | Dict with experiment_id, accuracy, loss, epochs |

## Advanced Usage

### Populate a Database with AI Records

```python
from faker import Faker
from faker_ai import AiProvider

fake = Faker()
fake.add_provider(AiProvider)

# Generate 100 AI deployment records
deployments = [fake.ai_deployment() for _ in range(100)]

# Generate experiment tracking data
experiments = [fake.ai_experiment() for _ in range(50)]
```

### Generate ML Pipeline Configuration

```python
fake.seed_instance(42)  # Reproducible pipeline

pipeline = {
    "name": f"pipeline-{fake.random_int(1000, 9999)}",
    "training": fake.ai_training_run(),
    "deployment": fake.ai_deployment(),
    "experiment": fake.ai_experiment(),
}
```

### Filter Models by Capability

```python
# Get all models that support code generation
code_models = fake.ai_models_for_task("code-generation")

# Get all diffusion models
diffusion_models = fake.ai_models_by_architecture("Diffusion")

# Get all multimodal models
video_models = fake.ai_models_by_modality("video")
```

## Model Scenario

Get complete, correlated model information:

```python
scenario = fake.model_scenario()
# {
#     'model': 'GPT-5.2',
#     'company': 'OpenAI',
#     'architecture': 'Transformer',
#     'modality': ['text', 'image', 'audio', 'video'],
#     'tasks': ['text-generation', 'reasoning', 'code-generation', ...],
#     'parameters': 'undisclosed',
#     'release_year': 2026
# }
```

## License

MIT

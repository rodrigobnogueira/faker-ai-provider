from typing import TypedDict

from faker.providers import BaseProvider, ElementsType

from .types import ModelData


class ModelScenario(TypedDict):
    model: str
    company: str
    architecture: str
    modality: list[str]
    tasks: list[str]
    parameters: str
    release_year: int


class AiProvider(BaseProvider):
    """Faker provider for generating AI/ML-related fake data with correlations."""

    _model_correlations: dict[str, ModelData] | None = None

    @property
    def model_correlations(self) -> dict[str, ModelData]:
        if self._model_correlations is None:
            from .model_correlations import MODEL_CORRELATIONS
            self._model_correlations = MODEL_CORRELATIONS
        return self._model_correlations

    @property
    def ai_models(self) -> tuple[str, ...]:
        return tuple(self.model_correlations.keys())

    @property
    def ai_companies(self) -> tuple[str, ...]:
        companies = {data["company"] for data in self.model_correlations.values()}
        return tuple(sorted(companies))

    @property
    def ai_architectures(self) -> tuple[str, ...]:
        archs = {data["architecture"] for data in self.model_correlations.values()}
        return tuple(sorted(archs))

    @property
    def ai_tasks_list(self) -> tuple[str, ...]:
        all_tasks: set[str] = set()
        for data in self.model_correlations.values():
            all_tasks.update(data["tasks"])
        return tuple(sorted(all_tasks))

    @property
    def ai_modalities(self) -> tuple[str, ...]:
        all_mods: set[str] = set()
        for data in self.model_correlations.values():
            all_mods.update(data["modality"])
        return tuple(sorted(all_mods))

    ml_frameworks: ElementsType[str] = (
        "PyTorch",
        "TensorFlow",
        "JAX",
        "Keras",
        "Hugging Face Transformers",
        "scikit-learn",
        "XGBoost",
        "LightGBM",
        "ONNX",
        "MLflow",
        "Weights & Biases",
        "Ray",
        "Dask",
        "Apache Spark MLlib",
        "Fast.ai",
        "Lightning",
        "LangChain",
        "LlamaIndex",
        "vLLM",
        "DeepSpeed",
        "TensorFlow Lite",
        "OpenCV",
        "Caffe",
    )

    ai_datasets: ElementsType[str] = (
        "ImageNet",
        "COCO",
        "Common Crawl",
        "The Pile",
        "C4",
        "RedPajama",
        "LAION-5B",
        "Wikipedia",
        "BookCorpus",
        "OpenWebText",
        "Stack Overflow",
        "GitHub Code",
        "MNIST",
        "CIFAR-10",
        "CIFAR-100",
        "LibriSpeech",
        "SQuAD",
        "GLUE",
        "SuperGLUE",
        "MMLU",
        "HumanEval",
        "GSM8K",
        "HellaSwag",
        "TruthfulQA",
        "Dolma",
        "RefinedWeb",
        "FineWeb",
        "Proof-Pile",
        "FineWeb-Edu",
        "SlimPajama",
        "WebText",
        "Anthropic HH-RLHF",
    )

    def ai_model(self) -> str:
        return self.random_element(self.ai_models)

    def ai_company(self) -> str:
        return self.random_element(self.ai_companies)

    def ai_architecture(self) -> str:
        return self.random_element(self.ai_architectures)

    def ai_task(self) -> str:
        return self.random_element(self.ai_tasks_list)

    def ai_modality(self) -> str:
        return self.random_element(self.ai_modalities)

    def ml_framework(self) -> str:
        return self.random_element(self.ml_frameworks)

    def ai_dataset(self) -> str:
        return self.random_element(self.ai_datasets)

    def ai_model_for_company(self, company: str) -> str:
        models = [m for m, d in self.model_correlations.items() if d["company"] == company]
        if not models:
            raise ValueError(f"No models found for company '{company}'")
        return self.random_element(models)

    def ai_company_for_model(self, model: str) -> str:
        if model not in self.model_correlations:
            raise ValueError(f"Model '{model}' not found")
        return self.model_correlations[model]["company"]

    def ai_tasks_for_model(self, model: str) -> list[str]:
        if model not in self.model_correlations:
            raise ValueError(f"Model '{model}' not found")
        return list(self.model_correlations[model]["tasks"])

    def ai_models_for_task(self, task: str) -> list[str]:
        return [m for m, d in self.model_correlations.items() if task in d["tasks"]]

    def ai_models_by_architecture(self, architecture: str) -> list[str]:
        return [m for m, d in self.model_correlations.items() if d["architecture"] == architecture]

    def ai_models_by_modality(self, modality: str) -> list[str]:
        return [m for m, d in self.model_correlations.items() if modality in d["modality"]]

    def ai_parameters_for_model(self, model: str) -> str:
        if model not in self.model_correlations:
            raise ValueError(f"Model '{model}' not found")
        return self.model_correlations[model]["parameters"]

    def model_scenario(self, model: str | None = None) -> ModelScenario:
        if model is None:
            model = self.ai_model()
        elif model not in self.model_correlations:
            raise ValueError(f"Model '{model}' not found")

        data = self.model_correlations[model]
        return {
            "model": model,
            "company": data["company"],
            "architecture": data["architecture"],
            "modality": list(data["modality"]),
            "tasks": list(data["tasks"]),
            "parameters": data["parameters"],
            "release_year": data["release_year"],
        }

    def ai_model_description(self, model: str | None = None) -> str:
        scenario = self.model_scenario(model)
        return (
            f"{scenario['model']} by {scenario['company']} "
            f"({scenario['parameters']}, {scenario['architecture']})"
        )

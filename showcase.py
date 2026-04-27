"""
Showcase for faker-ai-provider library.

This script demonstrates the capabilities of the AI Provider 
for generating realistic AI/ML-related test data with correlations.
"""

from faker import Faker

from faker_ai import AiProvider


fake = Faker()
fake.add_provider(AiProvider)


def print_header(title: str) -> None:
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}")


def print_subheader(title: str) -> None:
    print(f"\n{title}")
    print("-" * 70)


def showcase_basic_data() -> None:
    print_header("Basic AI/ML Data")

    print_subheader("AI Models")
    for _ in range(5):
        print(f"  • {fake.ai_model()}")

    print_subheader("AI Companies")
    for _ in range(5):
        print(f"  • {fake.ai_company()}")

    print_subheader("Model Architectures")
    for _ in range(5):
        print(f"  • {fake.ai_architecture()}")

    print_subheader("ML Frameworks")
    for _ in range(5):
        print(f"  • {fake.ml_framework()}")


def showcase_tasks_and_modalities() -> None:
    print_header("Tasks & Modalities")

    print_subheader("AI Tasks")
    for _ in range(5):
        print(f"  • {fake.ai_task()}")

    print_subheader("Modalities")
    for modality in ("text", "image", "audio", "video"):
        print(f"  • {modality}")

    print_subheader("Datasets")
    for _ in range(5):
        print(f"  • {fake.ai_dataset()}")


def showcase_correlated_data() -> None:
    print_header("Correlated Data")

    print_subheader("Models by Company")
    companies = ["OpenAI", "Anthropic", "Google DeepMind", "Meta AI"]
    for company in companies:
        model = fake.ai_model_for_company(company)
        print(f"  • {company:<20} → {model}")

    print_subheader("Company for Model")
    models = ["GPT-5.3-Codex", "Claude Opus 4.7", "Gemini 3 Pro Preview", "Llama 4 Maverick"]
    for model in models:
        company = fake.ai_company_for_model(model)
        print(f"  • {model:<20} → {company}")

    print_subheader("Tasks for Model")
    model = "Claude Opus 4.7"
    print(f"\n  Model: {model}")
    tasks = fake.ai_tasks_for_model(model)
    for task in tasks:
        print(f"    → {task}")


def showcase_filtering() -> None:
    print_header("Filtering by Attributes")

    print_subheader("Models by Architecture: Diffusion")
    models = fake.ai_models_by_architecture("Diffusion")[:5]
    for model in models:
        print(f"  • {model}")

    print_subheader("Models by Modality: video")
    models = fake.ai_models_by_modality("video")[:5]
    for model in models:
        print(f"  • {model}")

    print_subheader("Models for Task: code-generation")
    models = fake.ai_models_for_task("code-generation")[:5]
    for model in models:
        print(f"  • {model}")


def showcase_model_scenarios() -> None:
    print_header("Complete Model Scenarios")

    for i in range(3):
        print_subheader(f"Scenario #{i + 1}")
        scenario = fake.model_scenario()

        print(f"\n  Model:        {scenario['model']}")
        print(f"  Company:      {scenario['company']}")
        print(f"  Architecture: {scenario['architecture']}")
        print(f"  Parameters:   {scenario['parameters']}")
        print(f"  Released:     {scenario['release_year']}")

        print("\n  Modalities:")
        for mod in scenario["modality"]:
            print(f"    • {mod}")

        print("\n  Supported Tasks:")
        for task in scenario["tasks"]:
            print(f"    • {task}")


def showcase_descriptions() -> None:
    print_header("Model Descriptions")

    print_subheader("Formatted Model Descriptions")
    for _ in range(5):
        print(f"  • {fake.ai_model_description()}")


def main() -> None:
    print("\n" + "=" * 70)
    print("  FAKER AI PROVIDER - CAPABILITIES SHOWCASE")
    print("=" * 70)
    print("\n🤖 Generating realistic AI/ML test data with correlations...")
    print("📅 Model data updated: April 2026\n")

    showcase_basic_data()
    showcase_tasks_and_modalities()
    showcase_correlated_data()
    showcase_filtering()
    showcase_model_scenarios()
    showcase_descriptions()

    print("\n" + "=" * 70)
    print("  End of Showcase")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()

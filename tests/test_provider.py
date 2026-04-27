import pytest
from faker import Faker
from faker_ai import AiProvider


@pytest.fixture
def faker():
    fake = Faker()
    fake.add_provider(AiProvider)
    return fake


class TestBasicMethods:
    def test_ai_model(self, faker):
        from faker_ai.model_correlations import MODEL_CORRELATIONS
        for _ in range(50):
            result = faker.ai_model()
            assert isinstance(result, str)
            assert result in MODEL_CORRELATIONS

    def test_ai_company(self, faker):
        for _ in range(50):
            result = faker.ai_company()
            assert isinstance(result, str)
            assert len(result) > 0

    def test_ai_architecture(self, faker):
        for _ in range(50):
            result = faker.ai_architecture()
            assert isinstance(result, str)
            assert len(result) > 0

    def test_ml_framework(self, faker):
        for _ in range(50):
            result = faker.ml_framework()
            assert isinstance(result, str)
            assert result in AiProvider.ml_frameworks

    def test_ai_task(self, faker):
        for _ in range(50):
            result = faker.ai_task()
            assert isinstance(result, str)
            assert len(result) > 0

    def test_ai_modality(self, faker):
        for _ in range(50):
            result = faker.ai_modality()
            assert isinstance(result, str)
            assert result in ("text", "image", "audio", "video")

    def test_ai_dataset(self, faker):
        for _ in range(50):
            result = faker.ai_dataset()
            assert isinstance(result, str)
            assert result in AiProvider.ai_datasets


class TestCorrelationMethods:
    def test_ai_model_for_company(self, faker):
        model = faker.ai_model_for_company("OpenAI")
        assert faker.ai_company_for_model(model) == "OpenAI"

    def test_ai_model_for_company_invalid(self, faker):
        with pytest.raises(ValueError, match="No models found"):
            faker.ai_model_for_company("NonExistentCompany")

    def test_ai_company_for_model(self, faker):
        company = faker.ai_company_for_model("GPT-5.2")
        assert company == "OpenAI"

    def test_ai_company_for_model_invalid(self, faker):
        with pytest.raises(ValueError, match="not found"):
            faker.ai_company_for_model("NonExistentModel")

    def test_ai_tasks_for_model(self, faker):
        tasks = faker.ai_tasks_for_model("Claude Opus 4.7")
        assert isinstance(tasks, list)
        assert "reasoning" in tasks

    def test_ai_models_for_task(self, faker):
        models = faker.ai_models_for_task("text-generation")
        assert isinstance(models, list)
        assert len(models) > 0

    def test_ai_models_by_architecture(self, faker):
        models = faker.ai_models_by_architecture("Diffusion")
        assert isinstance(models, list)
        assert len(models) > 0

    def test_ai_models_by_modality(self, faker):
        models = faker.ai_models_by_modality("video")
        assert isinstance(models, list)
        assert len(models) > 0

    def test_ai_parameters_for_model(self, faker):
        params = faker.ai_parameters_for_model("gpt-oss-120b")
        assert params == "120B"

    def test_catalog_includes_recent_models(self, faker):
        from faker_ai.model_correlations import MODEL_CORRELATIONS

        expected_models = {
            "GPT-5.2",
            "GPT-5.2 pro",
            "GPT-5.3-Codex",
            "GPT-5.3-Codex-Spark",
            "Claude Opus 4.7",
            "Gemini 3 Pro Preview",
            "Llama 4 Maverick",
            "Mistral Small 4",
            "Grok 4.20",
            "DeepSeek-V3.2",
            "Cohere Transcribe",
        }
        assert expected_models.issubset(MODEL_CORRELATIONS)

    def test_catalog_keeps_verified_legacy_models(self, faker):
        from faker_ai.model_correlations import MODEL_CORRELATIONS

        expected_models = {
            "GPT-4o",
            "GPT-4",
            "DALL-E 3",
            "Claude Opus 4.6",
            "Claude Sonnet 4.5",
            "Claude 3 Opus",
            "Gemini 1.5 Pro",
            "Gemma 2 27B",
            "Imagen 4",
            "Veo 2",
            "Mixtral 8x22B",
            "DeepSeek-V3",
            "Qwen2.5",
            "Qwen-VL-Max",
            "Command R+",
            "Stable Diffusion XL",
            "Recraft V3",
            "Ideogram 3.0",
            "Phi-3",
            "Falcon 180B",
        }
        assert expected_models.issubset(MODEL_CORRELATIONS)

    def test_catalog_omits_unverified_future_models(self, faker):
        from faker_ai.model_correlations import MODEL_CORRELATIONS

        unverified_models = {
            "Claude 5",
            "DALL-E 4",
            "DeepSeek-V4",
            "Grok-5",
            "LLaMA 4.1",
            "Stable Diffusion 4",
        }
        assert MODEL_CORRELATIONS.keys().isdisjoint(unverified_models)


class TestModelScenario:
    def test_model_scenario_random(self, faker):
        scenario = faker.model_scenario()
        assert "model" in scenario
        assert "company" in scenario
        assert "architecture" in scenario
        assert "modality" in scenario
        assert "tasks" in scenario
        assert "parameters" in scenario
        assert "release_year" in scenario

    def test_model_scenario_specific(self, faker):
        scenario = faker.model_scenario("Claude Opus 4.7")
        assert scenario["model"] == "Claude Opus 4.7"
        assert scenario["company"] == "Anthropic"
        assert isinstance(scenario["tasks"], list)

    def test_model_scenario_invalid(self, faker):
        with pytest.raises(ValueError, match="not found"):
            faker.model_scenario("InvalidModel")

    def test_model_scenario_correlation(self, faker):
        for _ in range(20):
            scenario = faker.model_scenario()
            company = faker.ai_company_for_model(scenario["model"])
            assert company == scenario["company"]


class TestAiModelDescription:
    def test_ai_model_description(self, faker):
        desc = faker.ai_model_description("gpt-oss-120b")
        assert "gpt-oss-120b" in desc
        assert "OpenAI" in desc
        assert "120B" in desc

    def test_ai_model_description_random(self, faker):
        for _ in range(10):
            desc = faker.ai_model_description()
            assert isinstance(desc, str)
            assert " by " in desc


class TestCompositeMethods:
    def test_full_ai_model_spec(self, faker):
        spec = faker.full_ai_model_spec("Claude Opus 4.7")
        assert "Claude Opus 4.7" in spec
        assert "Anthropic" in spec
        assert "Transformer" in spec
        assert "undisclosed parameters" in spec

    def test_full_ai_model_spec_random(self, faker):
        for _ in range(10):
            spec = faker.full_ai_model_spec()
            assert isinstance(spec, str)
            assert " by " in spec
            assert "parameters" in spec

    def test_ai_training_run(self, faker):
        run = faker.ai_training_run()
        assert "model" in run
        assert "framework" in run
        assert "dataset" in run
        assert "task" in run

    def test_ai_deployment(self, faker):
        deployment = faker.ai_deployment()
        assert "model" in deployment
        assert "endpoint" in deployment
        assert "status" in deployment
        assert deployment["status"] in ("active", "deployed", "staging", "beta")

    def test_ai_experiment(self, faker):
        experiment = faker.ai_experiment()
        assert "experiment_id" in experiment
        assert "accuracy" in experiment
        assert "loss" in experiment
        assert experiment["experiment_id"].startswith("exp-")


class TestSeeding:
    def test_seeding_reproducibility(self):
        from faker import Faker
        from faker_ai import AiProvider

        fake1 = Faker()
        fake1.add_provider(AiProvider)
        fake1.seed_instance(42)

        fake2 = Faker()
        fake2.add_provider(AiProvider)
        fake2.seed_instance(42)

        assert fake1.ai_model() == fake2.ai_model()
        assert fake1.ai_company() == fake2.ai_company()
        assert fake1.full_ai_model_spec() == fake2.full_ai_model_spec()

    def test_different_seeds_different_results(self):
        from faker import Faker
        from faker_ai import AiProvider

        fake1 = Faker()
        fake1.add_provider(AiProvider)
        fake1.seed_instance(42)

        fake2 = Faker()
        fake2.add_provider(AiProvider)
        fake2.seed_instance(123)

        results1 = [fake1.ai_model() for _ in range(5)]
        results2 = [fake2.ai_model() for _ in range(5)]
        assert results1 != results2

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
        tasks = faker.ai_tasks_for_model("Claude Opus 4.6")
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
        params = faker.ai_parameters_for_model("GPT-5.2")
        assert params == "1.5T"


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
        scenario = faker.model_scenario("Claude Opus 4.6")
        assert scenario["model"] == "Claude Opus 4.6"
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
        desc = faker.ai_model_description("GPT-5.2")
        assert "GPT-5.2" in desc
        assert "OpenAI" in desc
        assert "1.5T" in desc

    def test_ai_model_description_random(self, faker):
        for _ in range(10):
            desc = faker.ai_model_description()
            assert isinstance(desc, str)
            assert " by " in desc

from galtea.argilla_wrapper.models.base_fields import BaseTemplateFields

class ABTestingFields(BaseTemplateFields):
    prompt: str
    answer_a: str
    answer_b: str

import os

def test_models_file_exists():
    """Check that a Django models file is present."""
    assert os.path.isfile("models.py"), "models.py file is missing"

def test_models_contains_django_model():
    """Check that the models file defines at least one Django model."""
    with open("models.py", "r", encoding="utf-8") as f:
        content = f.read()
    # Look for a class inheriting from django.db.models.Model
    assert "models.Model" in content, "No Django model class found in models.py"

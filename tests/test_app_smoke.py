"""Smoke tests for the Streamlit application and saved model artifacts."""

from pathlib import Path

from streamlit.testing.v1 import AppTest


def test_app_loads_artifacts_and_can_make_a_prediction():
    app_path = Path(__file__).resolve().parents[1] / "app.py"
    app = AppTest.from_file(app_path, default_timeout=90).run()

    # The page reaches the input UI only after the model, vectorizer and
    # required NLTK resources have loaded successfully.
    assert len(app.text_area) == 1
    assert len(app.button) == 1
    assert not app.exception

    app.text_area[0].set_value("Congratulations! You have won a free prize. Call now!")
    app.button[0].click()
    app.run()

    # Either result is valid for a model smoke test; the assertion verifies
    # that preprocessing, vectorization and prediction completed.
    assert app.success or app.error
    assert not app.exception

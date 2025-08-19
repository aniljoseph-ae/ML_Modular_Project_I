# ./utils/evaluation_metrics.py

from matplotlib import pyplot as plt
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score,

    ConfusionMatrixDisplay,
    PrecisionRecallDisplay,
    RocCurveDisplay
)

def classification_metrics(y_test, y_pred, model = None, X_test = None):
    print(f"Classification Report: {classification_report(y_test, y_pred)}")
    print(f"Accuracy: {accuracy_report(y_test, y_pred)}")

    # confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    ConfusionMatrixDisplay(cm).plot()
    plt.title("Confusion Matrix")
    plt.show()

    # ROC & PR curves (only if the model supports predict_proba / decision_function)
    if model is not None:
        try:
            RocCurveDisplay.from_estimator(model, X_test, y_pred)
            plt.title("ROC Curve")
            plt.show()
        except Exception as e:
            print(f"(skipping ROC Curve: {e})")

        try:
            PrecisionRecallDisplay.from_estimator(model, X_test, y_pred)
            plt.title("Precision-Recall Curve")
            plt.show()
        except Exception as e:
            print(f"(skipping Precision Recall Curve: {e})")
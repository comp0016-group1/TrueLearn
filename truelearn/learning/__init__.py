"""The truelearn.learning module implements classifiers in TrueLearn paper."""

from ._base import BaseClassifier
from ._ink_classifier import INKClassifier
from ._interest_classifier import InterestClassifier
from ._knowledge_classifier import KnowledgeClassifier
from ._novelty_classifier import NoveltyClassifier
from ._engage_classifier import EngageClassifier
from ._persistent_classifier import PersistentClassifier
from ._majority_classifier import MajorityClassifier

__all__ = [
    "BaseClassifier",
    "INKClassifier",
    "InterestClassifier",
    "KnowledgeClassifier",
    "NoveltyClassifier",
    "EngageClassifier",
    "PersistentClassifier",
    "MajorityClassifier",
]

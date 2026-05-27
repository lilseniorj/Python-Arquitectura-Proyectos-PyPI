"""Data models for Platzi News."""

from dataclasses import dataclass


@dataclass
class Article:
    """Represents a news article."""

    title: str
    description: str
    url: str

    """You can add more fields like 'published_at', 'author', etc. if needed
    asdasd
    """

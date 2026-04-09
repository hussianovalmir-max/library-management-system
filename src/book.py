class Book:
    def __init__(self, title: str, author: str, isbn: str) -> None:
        if not title or not author:
            raise ValueError("Title and author are required")
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available: bool = True

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

    def __repr__(self) -> str:
        return f"Book('{self.title}', '{self.author}', '{self.isbn}')"

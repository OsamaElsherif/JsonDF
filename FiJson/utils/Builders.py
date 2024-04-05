from typing import Any

class QueryBuilder:
    """
    Base class for building SQL queries with different types (SELECT, INSERT, DELETE).
    """

    def __init__(self) -> None:
        self.query_parts = []
        self._columns: list[str] = []
        self._values: list[Any] = []
        self.table_name: str = None
        self.where_clause: str = None

    def __str__(self) -> str:
        return " ".join(self.query_parts)

    def build(self) -> str:
        pass


class SelectQueryBuilder(QueryBuilder):
    """
    Concrete class for building SELECT queries with a fluent interface.
    """

    SELECT_CLAUSE = "SELECT"
    FROM_CLAUSE = "FROM"

    def __init__(self, *columns: str) -> None:
        super().__init__()
        self.__select(columns)

    def __select(self, columns: str) -> "SelectQueryBuilder":
        """
        Selects columns for the query and returns the builder object.
        """
        self._columns.extend(columns)
        return self

    def from_(self, table_name: str) -> "SelectQueryBuilder":
        """
        Sets the table name for the query and returns the builder object.
        """
        self.table_name = table_name
        return self

    def where(self, where_clause: str) -> "SelectQueryBuilder":
        """
        Sets the WHERE clause for the query and returns the builder object.
        """
        self.where_clause = f" WHERE {where_clause}"
        return self

    def build(self) -> str:
        """
        Builds the final SELECT query string.
        """
        super().build()
        self.query_parts.append(self.SELECT_CLAUSE)
        if self._columns:
            self.query_parts.append(", ".join(self._columns))
        else:
            self.query_parts.append("*")
        self.query_parts.append(self.FROM_CLAUSE)
        self.query_parts.append(self.table_name)
        if self.where_clause:
            self.query_parts.append(self.where_clause)
        return str(self)


class InsertQueryBuilder(QueryBuilder):
    """
    Concrete class for building INSERT queries with a fluent interface.
    """

    INSERT_CLAUSE = "INSERT INTO"
    VALUES_CLAUSE = "VALUES"

    def __init__(self) -> None:
        super().__init__()

    def into(self, table_name: str) -> "InsertQueryBuilder":
        """
        Sets the table name for the query and returns the builder object.
        """
        self.table_name = table_name
        return self

    def columns(self, *columns: str) -> "InsertQueryBuilder":
        """
        Sets the columns for the INSERT query and returns the builder object.
        """
        self._columns.extend(columns)
        return self

    def values(self, *values: Any) -> "InsertQueryBuilder":
        """
        Sets the values for the INSERT query and returns the builder object.
        """
        self._values.extend(values)
        return self

    def build(self) -> str:
        """
        Builds the final INSERT query string.
        """
        super().build()
        self.query_parts.append(self.INSERT_CLAUSE)
        self.query_parts.append(self.table_name)
        self.query_parts.append("(")
        self.query_parts.append(", ".join(self._columns))
        self.query_parts.append(")")
        self.query_parts.append(self.VALUES_CLAUSE)
        self.query_parts.append("(")
        quoted_values = [f"'{val}'" for val in self._values]
        self.query_parts.append(", ".join(quoted_values))
        self.query_parts.append(")")
        return str(self)

class DeleteQueryBuilder(QueryBuilder):
    """
    Concrete class for building DELETE queries with a fluent interface.
    """

    DELETE_CLAUSE = "DELETE"
    FROM_CLAUSE = "FROM"

    def __init__(self) -> None:
        super().__init__()

    def from_(self, table_name: str) -> "DeleteQueryBuilder":
        """
        Sets the table name for the DELETE query and returns the builder object.
        """
        self.table_name = table_name
        return self

    def where(self, where_clause: str) -> "DeleteQueryBuilder":
        """
        Sets the WHERE clause for the DELETE query and returns the builder object.
        """
        self.where_clause = f" WHERE {where_clause}"
        return self

    def build(self) -> str:
        """
        Builds the final DELETE query string.
        """
        super().build()
        self.query_parts.append(self.DELETE_CLAUSE)
        self.query_parts.append(self.FROM_CLAUSE)
        self.query_parts.append(self.table_name)
        if self.where_clause:
            self.query_parts.append(self.where_clause)
        return str(self)
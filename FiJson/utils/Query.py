from Builders import InsertQueryBuilder, SelectQueryBuilder, DeleteQueryBuilder, Any, QueryBuilder
import re

class QueryAdabter:
    table_name: str = None

    def __init__(self, QueryBuilder: QueryBuilder) -> None:
        self.__Query_Builder = QueryBuilder
        self.process()
    
    def process(self):
        self.table_name = self.__Query_Builder.table_name
        if len(self.__Query_Builder._columns) != 0:
            self.columns = tuple(self.__Query_Builder._columns)
        if self.__Query_Builder.where_clause is not None:
            self.where = tuple(re.findall(r"(?<!WHERE)(?<= )\w+(?:[<>=!\*]+\w+)?|(?<= )[<>=!\*](?= )", self.__Query_Builder.where_clause.strip()))
        if len(self.__Query_Builder._values) != 0:
            self.values = tuple(self.__Query_Builder._values)

    def __getattr__(self, __name: str) -> Any:
        if __name == "where":
            raise AttributeError("There is no Where Clause in this query")
        elif __name not in ["table_name", "columns, values"]:
            raise AttributeError(f"Wrong attr name {__name} only you can find ( table_name, columns, where, values ) or there is not {__name} in the query")
        
        return self.__dict__[__name]
    
    def __repr__(self) -> str:
        return str(self.__Query_Builder)
        
class Query:
    def __init__(self) -> None:
        self._queries = ["insert", "select", "delete"]
    def __getattr__(self, __name: str) -> Any:
        if __name not in self._queries:
            raise NameError(f"{__name} isn't an exist query, supported are (insert, select, and delete)")
        
        # need some optimization
        if __name == "select":
            return eval(f"{__name.title()}QueryBuilder")
        
        return eval(f"{__name.title()}QueryBuilder()")
    
    @staticmethod
    def Adabter(queryBuilder: QueryBuilder):
        return QueryAdabter(queryBuilder)

# if __name__ == "__main__":
#     select_query = Query.Adabter(
#         Query()
#         .select("id", "name")
#         .from_("users")
#         .where("age > 20")
#         .build()
#         )
#     print(select_query.columns)

#     insert_query = Query.Adabter(
#         Query()
#         .insert
#         .into("products")
#         .columns("name", "price")
#         .values("Book", 10.99)
#         .build()
#     )
#     print(insert_query.columns)

#     delete_query = Query.Adabter(
#         Query()
#         .delete
#         .from_("orders")
#         .where("completed = 1")
#         .build()
#     )
#     print(delete_query.table_name)
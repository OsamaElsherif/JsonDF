from Builders import InsertQueryBuilder, SelectQueryBuilder, DeleteQueryBuilder, Any

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

# if __name__ == "__main__":
#     select_query = (
#         Query()
#         .select("id", "name")
#         .from_("users")
#         .where("age > 20")
#         .build()
#     )
#     print(select_query)

#     insert_query = (
#         Query()
#         .insert
#         .into("products")
#         .columns("name", "price")
#         .values("Book", 10.99)
#         .build()
#     )
#     print(insert_query)

#     delete_query = (
#         Query()
#         .delete
#         .from_("orders")
#         .where("completed = 1")
#         .build()
#     )
#     print(delete_query)
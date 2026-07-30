from app.db.neo4j import driver


class Neo4jRepository:

    def verify(self) -> bool:
        with driver.session() as session:
            result = session.run("RETURN 1 AS result")
            return result.single()["result"] == 1


    def create_paper(
        self,
        title,
        year,
        author
    ):

        query = """
        CREATE (p:Paper {
            title:$title,
            year:$year,
            author:$author
        })
        RETURN p
        """

        with driver.session() as session:
            result = session.run(
                query,
                title=title,
                year=year,
                author=author
            )

            return dict(result.single()["p"])


    def get_papers(self):

        query = """
        MATCH (p:Paper)
        RETURN p
        """

        with driver.session() as session:
            result = session.run(query)

            return [
                dict(record["p"])
                for record in result
            ]
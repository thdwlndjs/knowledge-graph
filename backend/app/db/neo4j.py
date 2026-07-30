from neo4j import GraphDatabase

from app.config import (
    NEO4J_URI,
    NEO4J_USER,
    NEO4J_PASSWORD
)


driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(
        NEO4J_USER,
        NEO4J_PASSWORD
    )
)


def verify_connection():
    try:
        with driver.session() as session:
            result = session.run(
                "RETURN 1 AS result"
            )

            return result.single()["result"] == 1

    except Exception as e:
        print(e)
        return False
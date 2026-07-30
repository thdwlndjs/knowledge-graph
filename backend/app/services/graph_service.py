from app.graph.neo4j_repository import Neo4jRepository


class GraphService:

    def __init__(self):
        self.repo = Neo4jRepository()


    def create_paper(self, paper):

        return self.repo.create_paper(
            paper.title,
            paper.year,
            paper.author
        )


    def get_papers(self):

        return self.repo.get_papers()
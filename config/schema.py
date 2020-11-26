"""Project schema"""

import graphene

from snippets.schema import Query as SnippetQuery, Mutation as SnippetMutation
from users.schema import Mutation as UserMutation


class Query(SnippetQuery, graphene.ObjectType):
    """Retrieves schema queries from apps"""


class Mutation(UserMutation, SnippetMutation, graphene.ObjectType):
    """Retrieves schema mutations from apps"""


schema = graphene.Schema(query=Query, mutation=Mutation)

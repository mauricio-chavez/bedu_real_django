"""Snippets app schema"""

import graphene
from django.shortcuts import get_object_or_404
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from .models import Snippet


class SnippetType(DjangoObjectType):
    """GraphQL Snippet Type"""

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'author', 'code']


# Queries

class Query:
    """Snippets app query object"""
    all_snippets = graphene.List(SnippetType)
    snippet = graphene.Field(SnippetType, id=graphene.Int(required=True))

    @login_required
    def resolve_all_snippets(self, info):
        """Returns all snippets"""
        author = info.context.user
        return Snippet.objects.filter(author=author)

    @login_required
    def resolve_snippet(self, info, id):
        """Retrieves a snippet"""
        author = info.context.user
        snippet = get_object_or_404(Snippet, id=id, author=author)
        return snippet


# Mutations

class CreateSnippetMutation(graphene.Mutation):
    """Creates a new snippet"""

    class Arguments:
        title = graphene.String(required=True)
        code = graphene.String(required=True)

    snippet = graphene.Field(SnippetType)

    @classmethod
    @login_required
    def mutate(cls, root, info, title, code):
        author = info.context.user
        snippet = Snippet.objects.create(title=title, code=code, author=author)
        return CreateSnippetMutation(snippet=snippet)


class UpdateSnippetMutation(graphene.Mutation):
    """Updates a snippet"""

    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        code = graphene.String()

    snippet = graphene.Field(SnippetType)

    @classmethod
    @login_required
    def mutate(cls, root, info, id, title=None, code=None):
        author = info.context.user
        snippet = get_object_or_404(Snippet, id=id, author=author)
        if title:
            snippet.title = title
        if code:
            snippet.code = code
        snippet.save()
        return UpdateSnippetMutation(snippet=snippet)


class DeleteSnippetMutation(graphene.Mutation):
    """Deletes a snippet"""

    class Arguments:
        id = graphene.Int(required=True)

    snippet = graphene.Field(SnippetType)

    @classmethod
    @login_required
    def mutate(cls, root, info, id):
        author = info.context.user
        snippet = get_object_or_404(Snippet, id=id, author=author)
        snippet.delete()
        return DeleteSnippetMutation(snippet=snippet)


class Mutation:
    """Mutation for snippets"""
    create_snippet = CreateSnippetMutation.Field()
    update_snippet = UpdateSnippetMutation.Field()
    delete_snippet = DeleteSnippetMutation.Field()

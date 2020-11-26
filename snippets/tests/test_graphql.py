"""GraphQL snippets tests"""

from django.contrib.auth.models import User

from graphql_jwt.testcases import JSONWebTokenTestCase

from ..models import Snippet


class GraphQLSnippetTests(JSONWebTokenTestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test', email='test@test.io')
        self.client.authenticate(self.user)

    def test_get_user_snippets_only(self):
        """Tests that allSnippets query shows only those snippets"""
        my_snippet = Snippet.objects.create(title='snippet', code='my code', author=self.user)

        other_user = User.objects.create_user(username='other', password='other', email='other@test.io')
        other_snippet = Snippet.objects.create(title='other snippet', code='other code', author=other_user)

        query = """
        {
          allSnippets {
            title
            code
          }
        }
        """

        response = self.client.execute(query)

        all_snippets = response.data.get('allSnippets')
        self.assertIsNotNone(all_snippets)

        expected_snippet = {'title': my_snippet.title, 'code': my_snippet.code}
        self.assertIn(expected_snippet, all_snippets)

        not_expected_snippet = {'title': other_snippet.title, 'code': other_snippet.code}
        self.assertNotIn(not_expected_snippet, all_snippets)

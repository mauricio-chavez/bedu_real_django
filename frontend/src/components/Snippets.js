import {gql, useQuery} from '@apollo/client';
import client from "../client";

const GET_SNIPPETS = gql`
    query GetSnippets {
        allSnippets {
            id
            title
            code
        }
    }
`;

export default function Snippets({authHandler}) {
  const {loading, error, data} = useQuery(GET_SNIPPETS);

  if (loading) return 'Loading...';
  if (error) return `Error! ${error.message}`;

  return (
    <div>
      <button onClick={() => {
        localStorage.removeItem('auth-token')
        client.clearStore()
        authHandler(false)
      }}>Cerrar sesión</button>
      {data.allSnippets.map(snippet => (
        <div key={snippet.id}>
          <h2>{snippet.title}</h2>
          <p>{snippet.code}</p>
        </div>
      ))}
    </div>
  );
}

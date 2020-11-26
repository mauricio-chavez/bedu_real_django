import {useState} from 'react'
import {gql, useMutation} from '@apollo/client';

const LOGIN = gql`
    mutation Login($username: String!, $password: String!) {
        tokenAuth(username: $username password: $password) {
            token
        }
    }
`;

export default function Login({authHandler}) {
  const [login, _] = useMutation(LOGIN);
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  return (
    <div>
      <form
        onSubmit={async e => {
          e.preventDefault();
          try {
            const {data} = await login({variables: {username, password}});
            const token = data.tokenAuth.token
            localStorage.setItem('auth-token', token)
            authHandler(true)
          } catch {
            alert('Credenciales incorrectas')
          }
        }}
      >
        <p>
          <label htmlFor="username">Usuario</label>
          <input type="text" id="username" value={username} onChange={e =>
            setUsername(e.target.value)
          }/>
        </p>
        <p>
          <label htmlFor="password">Contraseña</label>
          <input type="password" id="password" value={password} onChange={e =>
            setPassword(e.target.value)
          }/>
        </p>
        <button type="submit">Iniciar sesión</button>
      </form>
    </div>
  );
}

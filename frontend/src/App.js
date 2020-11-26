import {useState} from 'react'
import { ApolloProvider } from '@apollo/client';
import client from './client'

import Login from "./components/Login";
import Snippets from "./components/Snippets";

function App() {
  const isAuthenticated = !!localStorage.getItem('auth-token')
  const [authenticated, setAuthenticated] = useState(isAuthenticated)
  return (
    <ApolloProvider client={client}>
      {authenticated ?  <Snippets authHandler={setAuthenticated} /> : <Login authHandler={setAuthenticated} />}
    </ApolloProvider>
  );
}

export default App;

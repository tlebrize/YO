import React from 'react'
import { render } from 'react-dom'
import Router from './Router'
import NavBar from './components/NavBar'
import './index.scss'
import Login from './components/Login'
import useToken from './lib/hooks/useToken'

const App = () => {

  const { token, setToken } = useToken();

  if (!token) {
    return <Login setToken={setToken}/>
  }

  return (
      <Router />
  )
}

render(
  <App />,
  document.getElementById('root')
)
  
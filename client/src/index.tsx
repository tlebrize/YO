import React, { useState } from 'react'
import { render } from 'react-dom'
import Router from './Router'
import NavBar from './components/NavBar'
import './index.scss'
import Login from './components/Login'

const App = () => {

  const [token, setToken] = useState()

  if (!token) {
    return <Login />
  }

  return (
    <>
      <NavBar />
      <Router />
    </>
  )
}

render(
  <App />,
  document.getElementById('root')
)
  
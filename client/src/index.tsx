import React, { useEffect, useState } from 'react'
import { render } from 'react-dom'
import Router from './Router'
import './index.scss'
import Login from './components/Login'
import { getUser } from './services/login'

const App = () => {

  const [ token, setToken ] = useState<string | null>('');
  const [ loading, setLoading ] = useState<boolean>(true)

  useEffect(() => {
    getUser().then((user) => {
      if (user) {
        setToken(user);
        sessionStorage.setItem('token', user)
      }
    }).finally(() => {
      setLoading(false);
    })
  }, [])

  if (loading) {
    return <div></div>
  }

  if (!token) {
    return <Login setToken={(user: string) => {
      setToken(user)
      sessionStorage.setItem('token', user)
    }}/>
  }

  return (
      <Router />
  )
}

render(
  <App />,
  document.getElementById('root')
)
  
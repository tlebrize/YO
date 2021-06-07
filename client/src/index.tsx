import * as React from 'react'
import { render } from 'react-dom'
import Router from './Router'


const App = () => (
  <Router />
)

render(
  <App />,
  document.getElementById('root')
)
  
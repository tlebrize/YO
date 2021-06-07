import React from 'react'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import Episode from './components/EpisodePage'
import Homepage from './components/Homepage'
import NotFoundPage from './components/NotFoundPage'

function Router() {
  return (
    <BrowserRouter>
      <Route>
        <Switch>
          <Route exact path='/' component={Homepage} />
          <Route exact path='/episode/:uuid' component={Episode} />
          <Route component={NotFoundPage} />
        </Switch>
      </Route>
    </BrowserRouter>
  )
} 

export default Router
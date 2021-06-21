import React from 'react'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import Episode from './views/EpisodePage'
import Homepage from './views/Homepage'
import NotFoundPage from './views/NotFoundPage'

function Router() {
  return (
    <BrowserRouter>
      <Route>
        <Switch>
          <Route exact path='/' component={Homepage} />
          <Route exact path='/episode/:id' component={Episode} />
          <Route component={NotFoundPage} />
        </Switch>
      </Route>
    </BrowserRouter>
  )
} 

export default Router
import React from 'react'
import { NavLink } from 'react-router-dom'
import useToken from '../lib/hooks/useToken'
import './NavBar.scss'

const NavBar = () => {
    
    const { token, setToken } = useToken()

    return (
        <nav>
            <div className='logo'><NavLink className='logo' to='/'>YO</NavLink></div>
            <div className='greeting'>NAMASTE {token} &lt;3</div>
        </nav>
    )
  }

  export default NavBar
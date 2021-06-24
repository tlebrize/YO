import React, { useEffect, useState } from 'react'
import { NavLink } from 'react-router-dom'
import { getUser } from '../services/login'
import './NavBar.scss'

const NavBar = () => {
    
    const [user, setUser] = useState<string | null>(null)

    useEffect(() => {
        const username = sessionStorage.getItem('token')
        setUser(username)
    }, [])

    return (
        <nav>
            <div className='logo'><NavLink className='logo' to='/'>YO</NavLink></div>
            <div className='greeting'>NAMASTE {user} &lt;3</div>
        </nav>
    )
  }

  export default NavBar
import React, { ChangeEvent, useState } from 'react';
import { loginUser } from '../services/login'
import './Login.scss'

interface LoginProps {
  setToken: any
}

const Login = (props : LoginProps) => {
  const [username, setUserName] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [errorMsg, setError] = useState<string | null>();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    const user = await loginUser({ username, password })
    user ? props.setToken(user.username) : setError('Your login credentials could not be verified, please try again.')
  }

  return(
    <div className="login-wrapper">
    <h2>Please login to access YO</h2>
      <form onSubmit={handleSubmit}>
        <label>
          <p>Username</p>
          <input type="text" onChange={e => setUserName(e.target.value)}/>
        </label>
        <label>
          <p>Password</p>
          <input type="password" onChange={e => setPassword(e.target.value)}/>
        </label>
        <div className='errormsg'>
            {errorMsg}
        </div>
        <div>
          <button type="submit">Submit</button>
        </div>
      </form>
    </div>
  )
}

export default Login
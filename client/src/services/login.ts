import { API_ENDPOINT } from '../settings'

export async function loginUser(credentials: Models.Credentials) {
  return fetch(`${API_ENDPOINT}/auth/login/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      username: credentials.username,
      password: credentials.password
    })
  })
  .then(res => {
    if (res.ok) {
      return res.json()
    } else {
      return null
    }
  })
}
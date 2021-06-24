import { API_ENDPOINT } from '../settings'

export async function loginUser(credentials: Models.Credentials) {
  return fetch(`${API_ENDPOINT}/auth/login/`, {
    credentials: "include",
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

async function getCurrentUser() {
  const data = await fetch(`${API_ENDPOINT}/auth/me/`, {credentials: "include"})
    .then(res => res.status >= 400 ? null : res.json())
  return data ? data.username : null
}

export async function getUser() {
  const tokenString = sessionStorage.getItem('token')
  return tokenString ? tokenString : await getCurrentUser()
}
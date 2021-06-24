import { API_ENDPOINT } from '../settings'

export function getUserSeries() {
  return fetch(`${API_ENDPOINT}/episode/series/`, { credentials: "include" })
    .then(res => res.json())
}
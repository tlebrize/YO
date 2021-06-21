import { API_ENDPOINT } from '../settings'

export function getUserSeries() {
  return fetch(`${API_ENDPOINT}/attribute/series`)
    .then(res => res.json())
}
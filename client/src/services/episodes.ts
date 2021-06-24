import { API_ENDPOINT } from '../settings'

export function getEpisodeData(episodeId: string) {
    return fetch(`${API_ENDPOINT}/episode/${episodeId}/`, {
        credentials: "include"
      })
    .then(res => res.json())
}
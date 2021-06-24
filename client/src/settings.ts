export const ENVIRONMENTS: any = {
    production: process.env.NODE_ENV === 'production',
    local: window.location.hostname === 'localhost'
  }  

export let API_ENDPOINT: string
if (ENVIRONMENTS.local) {
  API_ENDPOINT = `http://127.0.0.1:8000`
} else {
  API_ENDPOINT = `https://yo.theof.fr`
}

import axios from 'axios'

const getAPI = axios.create({
    baseURL: 'http://127.0.0.1:5000',
    timeout: 1000,
})

const getAPI2 = axios.create({
    baseURL: 'https://cat-fact.herokuapp.com',
    timeout: 1000,
})

export {
    getAPI,
    getAPI2,
}

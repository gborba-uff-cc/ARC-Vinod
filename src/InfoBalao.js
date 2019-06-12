import axios from 'axios'

export const iniciar = balao => {
  return axios
    .get('/', {
      ip: balao.ip,
      conectado: balao.conectado
    })
    .then(response => {
      console.log("Balao Solicitado")
    })
    .catch(err => {
      console.log(err)
    })
}

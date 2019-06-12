import React, { Component } from 'react'
import { iniciar } from './InfoBalao'

class Balao extends Component {
  constructor() {
    super()
    this.state = {
      ip: '',
      conectado: ''
    }
  }

  componentDidMount() {
    this.setState({
      ip: this.ip,
      conectado: this.conectado
    })
  }

  render() {
    return (
      <div className="container">
        <div className="jumbotron mt-5">
          <div className="col-sm-8 mx-auto">
            <h1 className="text-center">Dados</h1>
          </div>
          <table className="table col-md-6 mx-auto">
            <tbody>
              <tr>
                <td>IP</td>
                <td>{this.state.ip}</td>
              </tr>
              <tr>
                <td>Conectado</td>
                <td>{this.state.conectado}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    )
  }
}

export default Balao

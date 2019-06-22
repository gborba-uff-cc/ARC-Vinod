import React from 'react';
import faker from 'faker';
import { spawn } from 'child_process';

import axios from 'axios';

class Card extends React.Component {
    state = {
        input: "",
        data: null
    }

    updateInput = (e) => {
        this.setState({ input: e.target.value });
    }

    sendInput = async () => {
        const response = await axios.get('http://localhost:5000/' + this.props.id);
        this.setState({ data: response.data });
    }

    render() {
        return (
        <div className="ui card">
            <div className="image">
                <img alt = ""  />
            </div>
            <div className="content">
                <a className="header">{this.props.name} </a>
                <div className="meta">
                </div>
                <div className="description">
                    X : {this.state.data && this.state.data.longitude}
                </div>
                <div className="description">
                    Y : {this.state.data && this.state.data.latitude}
                </div>
                <div className="description">
                    Z : {this.state.data && this.state.data.altitude}
                </div>
                <div className="ui input">
                    <input placeholder="Enter New Location" type="text" value={this.state.input} onChange={this.updateInput}/>
                    <div onClick={this.sendInput}>Clique aqui</div>
                </div>
            </div>
            <div className="extra content">
                <a>
                Modo : 
                </a>
            </div>
        </div>
        );
    }
}

export default Card;
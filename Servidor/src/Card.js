import React from 'react';
import faker from 'faker';
import { spawn } from 'child_process';
import './pages/card/styles.css';

import axios from 'axios';

class Card extends React.Component {
    state = {
        input: "",
        input2: "",
        data: null
    }

    updateInput = (e) => {
        this.setState({ input: e.target.value });
    }

    updateInput2 = (e) => {
        this.setState({ input2: e.target.value });
    }

    sendInput = async () => {
        const response = await axios.get('http://localhost:5000/' + this.props.id);
        this.setState({ data: response.data });
    }

    getInput = async () => {
        const response = await axios.get('http://localhost:5000/get' + this.state.input2);
    }

    render() {
        return (
        <div className="boxCard">
            <a> {this.props.name} </a>

            <div className="contentLocation">              
                <div className="description">
                    X : {this.state.data && this.state.data.longitude}
                </div>
                <div className="description">
                    Y : {this.state.data && this.state.data.latitude}
                </div>
                <div className="description">
                    Z : {this.state.data && this.state.data.altitude}
                </div>
            </div>
            
            <div className="boxInput2">  
                <input type="text"  className="inputText search" placeholder="Enter New Location" value={this.state.input} onChange={this.updateInput}/>
                <input onClick={this.sendInput} type="submit" className="btn submit"  value="Click"/>
            </div>
            
            <div className="boxInput2">  
                <input type="text"  className="inputText search" placeholder="get Infmation" value={this.state.input2} onChange={this.updateInput2}/>
                <input onClick={this.getInput} type="submit" className="btn submit"  value="Click"/>
            </div>


            <div className="clear"></div>

            <div className="contentModo">
                <input onClick={this.sendInput} type="submit" className="btn submit"  value="Refresh"/>
                <a>
                Modo : {this.state.data && this.state.data.modo} 
                </a>
            </div>
        </div>
        );
    }
}

export default Card;

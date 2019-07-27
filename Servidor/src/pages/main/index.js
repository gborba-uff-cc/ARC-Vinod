import React, { Component } from 'react';

import Card from '../../Card';
import './styles.css';

export default class Main extends Component {
    state = {
        baloons: [
            {
                name: `127.0.0.2`,
                id: 1
            }
        ]
    }

    renderBaloons = () => {
        return this.state.baloons.map(baloon => {
            return <Card key={baloon.id} name={baloon.name} id={baloon.id} />
        });
    }

    addBaloon = () => {
        let baloons = this.state.baloons;
        baloons.push({
            name: `127.0.0.${baloons.length+2}`,
            id: baloons.length + 1
        });
        this.setState({baloons:baloons})

    }


    render() {
        return (
            <div className="cards">
                <div className="actions">
                    <button  onClick={this.addBaloon}>
                        Add baloon
                    </button>

                    <button  onClick="">
                        Refresh
                    </button>

                    <button  onClick="">
                        Remove baloon
                    </button>
                </div>
                <div class="BoxCards">
                    { this.renderBaloons() } 
                </div>
            </div>
        );
    }
}
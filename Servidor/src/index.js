import React from 'react';
import ReactDOM from 'react-dom';
import faker from 'faker';
import CommentDetail from './CommentDetail';
import Controls from './Controls';
import Card from './Card';
import { async } from 'q';


class App extends React.Component {
    state = {
        baloons: [
            {
                name: `Balao 1`,
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
            name: `Balao ${baloons.length+1}`,
            id: baloons.length + 2
        });
        this.setState({baloons:baloons})

    }

    render(){
        return(
            <div className="ui link cards">
                <button onClick={this.addBaloon}>
                    ADD Baloon
                </button>
                { this.renderBaloons() } 
            </div>
        )
    }

}
ReactDOM.render( 
    <App />, document.querySelector('#root')
);


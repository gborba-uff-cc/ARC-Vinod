import React from 'react';
import ReactDOM from 'react-dom';
import faker from 'faker';
import CommentDetail from './CommentDetail';
import Controls from './Controls';
import Card from './Card';
import { async } from 'q';


const App = () => { 
    return (
        <div className="ui link cards">
            <Card/>
        </div>
    )
};


ReactDOM.render( 
    <App />, document.querySelector('#root')
);


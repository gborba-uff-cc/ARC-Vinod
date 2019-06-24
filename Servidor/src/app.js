import React from 'react';
import Card from './Card';
import { async } from 'q';
import Header from './components/Header';
import Main from './pages/main';
import './styles.css';

export default class App extends React.Component {
    render(){
        return(
            <div className="App">
                <Header />
                <Main />
                
            </div>
        )
    }

}
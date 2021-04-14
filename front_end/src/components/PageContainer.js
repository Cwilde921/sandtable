import React from 'react';
import Home from './pages/Home';
import PatternManager from './pages/PatternManager'
import ColorCenter from './pages/ColorCenter'

export default class PageContainer extends React.Component {
    constructor(params){
        super(params)
        this.state = {
            active: 0,
        }
    }

    set_active(num) {
        this.setState({ active: num })
    }

    render() {
        switch(this.state.active){
            case 1:
                return (
                    <PatternManager num={1} handler={this.set_active.bind(this)} />
                );
            case 2:
                return (
                    <ColorCenter num={2} handler={this.set_active.bind(this)} />
                );
            default:
                return (
                    <Home num={0} handler={this.set_active.bind(this)} />
                );

        }
        
    }
}
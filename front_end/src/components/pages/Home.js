import React from 'react';
import Card from '../common/Card'

import styles from '../../style/Home.module.css'

import pattern_img from '../../media/pattern.jpg';
import rgb_img from '../../media/rgb.jpg'
import pebble_img from '../../media/pebble.png'

export default class Home extends React.Component {
    constructor(params){
        super (params)
        this.state = {
            data: {},
        }
    }

    // componentDidMount(){
    //     let headers = {
    //         method: "GET",
    //         mode: "cors",
    //     }
    //     fetch("http://localhost:5000/api")
    //     .then( response => response.text() )
    //     .then( response => console.log(response) )
    // }

    render() {
        return (
            <div>
                <div>
                    <h1>Sand Table Home</h1>
                </div>
                <div className={styles.body} >
                    <Card name={"Manage Patterns"} img={pattern_img} num={1} handler={this.props.handler} />
                    <Card name={"Color Center"} img={rgb_img} num={2} handler={this.props.handler} />
                    <Card name={"testing"} img={pebble_img} num={2} handler={this.props.handler} />
                    <Card name={"testing"} img={pebble_img} num={2} handler={this.props.handler} />
                    <Card name={"testing"} img={pebble_img} num={2} handler={this.props.handler} />
                    <Card name={"testing"} img={pebble_img} num={2} handler={this.props.handler} />
                    <Card name={"testing"} img={pebble_img} num={2} handler={this.props.handler} />
                </div>
            </div>
        )
    }
}
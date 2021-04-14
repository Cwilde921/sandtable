import React from 'react';
import Tab from './Tab.js';
import styles from '../../style/TabContainer.module.css';

export default class TabContainer extends React.Component {
    constructor(params){
        super(params);
        this.state = {
            active: 0,
        }
    }

    set_active(num){
        if(this.state.active === num){
            num = 0;
        }
        this.setState({active: num})
    }

    render(){
        return (
            <div className={styles.tabcontainer}>
                <div className={styles.tabs}>
                    <Tab num={1} name={"Manage Patterns"} active={this.state.active} handler={this.set_active.bind(this)} />
                    <Tab num={2} name={"Change Lights"} active={this.state.active} handler={this.set_active.bind(this)} />
                    <Tab num={3} name={"Table Settings"} active={this.state.active} handler={this.set_active.bind(this)} />
                </div>
                <div></div>
            </div>
        )
    }
}
import React from 'react';

import styles from '../../style/Card.module.css'

export default class Card extends React.Component{
    render () {
        return (
        <div className={styles.card} onClick={ () => this.props.handler(this.props.num) } >
            <img className={styles.img} src={this.props.img} alt={"my media here"}></img>
            <h3>{this.props.name}</h3>
        </div>
        )
    }
}
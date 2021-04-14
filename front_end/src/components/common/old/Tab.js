import React from 'react';
import cx from 'classnames';

import styles from '../../style/Tab.module.css'

export default class Tab extends React.Component {

    get_class_name () {
        if (this.props.active == this.props.num) {
            return cx( styles.tab, styles.active );
        } else {
            return cx( styles.tab, styles.basic );
        }
    }

    render () {
        return (
            <div className={this.get_class_name()} onClick={ () => this.props.handler(this.props.num) } >
                <h3>{this.props.name}</h3>
            </div>
        )
    }
}
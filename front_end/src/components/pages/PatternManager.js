import React from 'react'

import styles from '../../style/PatternManager.module.css'

export default class PatternManager extends React.Component {
    render(){
        return (
            <div className={styles.body}>
                <h1>Pattern Manager</h1>
                <p>Make patterns with sandify and upload them here in thr format.</p>
                <form>
                    <label htmlFor={"pattern_file"} className={styles.inpt} > Upload Pattern </label>
                    <input id={"pattern_file"} className={styles.inpt} type={"file"} />

                    <hr/>
                    {/* <br/> */}
                    <button className={styles.inpt} onClick={ () => this.props.handler(0) }>Home</button>
                    <input type={"submit"} className={styles.inpt} value={"Submit Pattern"} />
                    <button className={styles.inpt} onClick={ () => window.location.href="https://sandify.org" } >Go To Sandify</button>
                </form>
            </div>
        )
    }
}